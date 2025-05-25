# 🔄 System Integration Demo: Real-Time Identity Provisioning

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
