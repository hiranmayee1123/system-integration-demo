# System Integration Demo: Real-Time Identity Provisioning

> A full-stack simulation of an identity and access management (IAM) system using **FastAPI**, **Streamlit**, **SQLite**, and **Pandas**.

---

## Live Demo Links

- 📊 **Dashboard (Streamlit):**  
[https://system-integration-demo-app.streamlit.app](https://system-integration-demo-app.streamlit.app)

- 🌐 **API Docs (Swagger UI):**  
  [https://system-integration-demo.onrender.com/docs](https://system-integration-demo.onrender.com/docs)




## Project Overview

This project simulates how organizations (like universities or companies) manage user identities by integrating HR and student systems into a single workflow.

It includes:
- ✅ Simulated HR + student data sources
- ✅ Identity lifecycle logic (active, pending, student_worker)
- ✅ REST APIs to onboard new users
- ✅ A unified provisioning queue
- ✅ A live dashboard for real-time insights

---

## 📁 Folder Structure

```bash
system-integration-demo/
├── data/
│   ├── employee_data.csv         # Mock HR dataset
│   └── student_roles.db          # SQLite database with all tables
│
├── scripts/
│   ├── 01_generate_employee_data.ipynb   # Generate employee data
│   ├── 02_generate_student_db.ipynb      # Create student dataset
│   ├── 03_etl_job.ipynb                  # ETL pipeline
│   └── 04_identity_sync.ipynb            # Status sync + provision queue
│
├── api/
│   └── api_server.py             # FastAPI backend with live endpoints
│
├── dashboard/
│   └── dashboard_app.py          # Streamlit dashboard for provisioning view
│
├── requirements.txt              # Python dependencies
└── README.md                     # You're reading it!
```

## ⚙️ What Each File Does

### 📁 data/
- **employee_data.csv** –  
  Auto-generated mock employee dataset using Faker. Contains fields like `id`, `name`, `email`, `role`, `department`, and `start_date`.

- **student_roles.db** –  
  The central SQLite database where all ETL operations store their outputs. Includes tables like:
  - `employee_records`
  - `student_roles`
  - `provision_queue` (merged and synced table of active users)

---

### 📁 scripts/

- **01_generate_employee_data.ipynb** –  
  Generates 100+ mock employee records using Python's `Faker` library.  
  Saves the data into a CSV file: `data/employee_data.csv`.  
  Used as the HR system simulation source.

- **02_generate_student_db.ipynb** –  
  Simulates student data including roles such as `"Student"`, `"Teaching Assistant"`, and `"Research Assistant"`.  
  Stores the records directly into `data/student_roles.db` in a table called `student_roles`.  
  Used as the academic system source.

- **03_etl_job.ipynb** –  
  Reads the employee CSV and student DB.  
  Cleans and standardizes both datasets.  
  Loads both datasets into `student_roles.db` as separate tables: `employee_records` and `student_roles`.

- **04_identity_sync.ipynb** –  
  Adds a `status` column to each user (`active`, `pending`, or `student_worker`) based on business logic.  
  Combines `employee_records` and `student_roles` into a single table called `provision_queue`.  
  This table powers the dashboard and APIs.

---

### 📁 api/

- **api_server.py** –  
  A FastAPI server with two main endpoints:
  - `POST /add-employee` – Adds a new employee record into the `employee_records` table and triggers a sync.
  - `POST /add-student` – Adds a new student record into the `student_roles` table and refreshes the provision queue.  
  🔁 After each API call, it re-runs the provisioning logic and updates the `provision_queue` table in the database.

---

### 📁 dashboard/

- **dashboard_app.py** –  
  A Streamlit-based dashboard that:
  - Reads data from the `provision_queue` table in `student_roles.db`
  - Allows filtering by `user type`, `department`, and `role`
  - Shows summary stats (number of active users, students vs employees)
  - Allows users to preview data and export it as CSV



---

## 🔁 Identity Sync Logic

| User Type | Status Logic                              |
|-----------|-------------------------------------------|
| Employee  | `active` if `start_date` is in the past   |
| Student   | `active` if enrolled, else `pending`      |
| TA/RA     | Always set as `student_worker`            |

➡️ Only users with `status == active` are added to the `provision_queue`.

---

## 🛠️ Technologies Used

- **Python 3.10** – Core programming language  
- **Pandas** – Data transformation and ETL logic  
- **SQLite** – Embedded local database for storing unified data  
- **FastAPI** – REST API backend for employee/student integration  
- **Streamlit** – Interactive dashboard to visualize provisioned identities  
- **Uvicorn** – ASGI server to run FastAPI  
- **Jupyter Notebooks** – Used for data simulation and pipeline prototyping  

### 🖥️ Deployment & Hosting

- **Render** – Used to deploy and host the live FastAPI backend (API + Swagger UI)  
- **Streamlit Community Cloud** – Used to deploy and host the real-time dashboard
---

## 🔬 Try It Yourself

- 🌐 Open the dashboard:  
  [`https://system-integration-demo-app.streamlit.app/`](https://system-integration-demo-app.streamlit.app/)

- 📡 Test the API live:  
  [`https://system-integration-demo.onrender.com/docs`](https://system-integration-demo.onrender.com/docs)

🧪 Add users using the API and watch them appear instantly in the dashboard.

---

## ✨ Future Enhancements

- [ ] Add `GET` endpoints for viewing employee/student records  
- [ ] Token-based authentication for API access  
- [ ] Support for PostgreSQL/Supabase for scalable DB  
- [ ] Deactivation and audit tracking (provisioning history)  
- [ ] CI/CD automation via GitHub Actions  

---

## 👩‍💻 Author

**Venkata Subbu Sai Hiranmayee Machavolu**  
📧 venkatamachavolu1123@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/hiranmayee1123)
