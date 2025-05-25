# System Integration Demo: Real-Time Identity Provisioning

> A full-stack simulation of an identity and access management (IAM) system using **FastAPI**, **Streamlit**, **SQLite**, and **Pandas**.

---

## Live Demo Links

- 📊 **Dashboard (Streamlit):**  
  [https://your-streamlit-app.streamlit.app](https://your-streamlit-app.streamlit.app)

- 🌐 **API Docs (Swagger UI):**  
  [https://your-fastapi-app.onrender.com/docs](https://your-fastapi-app.onrender.com/docs)

> Replace the links above with your actual deployed URLs.

---

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

## ⚙️ What Each File Does

### scripts/
- `01_generate_employee_data.ipynb` – Create mock employee records  
- `02_generate_student_db.ipynb` – Add students, TAs, RAs  
- `03_etl_job.ipynb` – ETL pipeline into a unified database  
- `04_identity_sync.ipynb` – Add lifecycle status and build the provision queue  

### api/
- `api_server.py` –  
  - `POST /add-employee`  
  - `POST /add-student`  
  ➕ Adds users and updates the `provision_queue` automatically  

### dashboard/
- `dashboard_app.py` –  
  📊 Real-time dashboard with filters, summary stats, and CSV export  

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

- Python 3.10  
- **Streamlit** – dashboard UI  
- **FastAPI** – REST API for integration  
- **SQLite** – embedded database  
- **Pandas** – data transformation and ETL logic  

---

## 🔬 Try It Yourself

- 🌐 Open the dashboard:  
  [`https://your-streamlit-app.streamlit.app`](https://your-streamlit-app.streamlit.app)

- 📡 Test the API live:  
  [`https://your-fastapi-app.onrender.com/docs`](https://your-fastapi-app.onrender.com/docs)

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
