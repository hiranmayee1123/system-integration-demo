from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from datetime import datetime
import pandas as pd

app = FastAPI()
DB_PATH = "data/student_roles.db"  # Adjust if your path is different

# 📦 Input model for employees
class Employee(BaseModel):
    id: int
    name: str
    email: str
    role: str
    department: str
    start_date: str  # Format: YYYY-MM-DD

# 📦 Input model for students
class Student(BaseModel):
    student_id: int
    name: str
    email: str
    department: str
    start_date: str
    role: str  # "Student", "Teaching Assistant", "Research Assistant"

# 🔄 Add employee endpoint
@app.post("/add-employee")
def add_employee(emp: Employee):
    year = int(emp.start_date.split("-")[0])
    current_year = datetime.today().year
    status = "active" if year <= current_year else "pending"

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO employee_records (id, name, email, role, department, start_date, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (emp.id, emp.name, emp.email, emp.role, emp.department, emp.start_date, status))
    conn.commit()

    rebuild_provision_queue(conn)
    conn.close()

    return {
        "message": "✅ Employee added successfully",
        "status": status,
        "provisioned": status == "active"
    }

# 🔄 Add student endpoint
@app.post("/add-student")
def add_student(stu: Student):
    year = int(stu.start_date.split("-")[0])
    current_year = datetime.today().year
    if stu.role == "Student":
        status = "active" if year <= current_year else "pending"
    else:
        status = "student_worker"

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO student_roles (student_id, name, email, department, start_date, role, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (stu.student_id, stu.name, stu.email, stu.department, stu.start_date, stu.role, status))
    conn.commit()

    rebuild_provision_queue(conn)
    conn.close()

    return {
        "message": "✅ Student added successfully",
        "status": status,
        "provisioned": status == "active"
    }

# 🔄 Shared function to rebuild provision_queue
def rebuild_provision_queue(conn):
    try:
        emp_df = pd.read_sql_query("SELECT * FROM employee_records WHERE status = 'active';", conn)
        emp_df["type"] = "employee"
        emp_df = emp_df[["id", "name", "email", "department", "start_date", "type"]]
    except:
        emp_df = pd.DataFrame(columns=["id", "name", "email", "department", "start_date", "type"])

    try:
        stu_df = pd.read_sql_query("SELECT * FROM student_roles WHERE status = 'active';", conn)
        stu_df = stu_df.rename(columns={"student_id": "id"})
        stu_df["type"] = "student"
        stu_df = stu_df[["id", "name", "email", "department", "start_date", "type"]]
    except:
        stu_df = pd.DataFrame(columns=["id", "name", "email", "department", "start_date", "type"])

    provision_queue = pd.concat([emp_df, stu_df], ignore_index=True)
    provision_queue.to_sql("provision_queue", conn, if_exists="replace", index=False)


