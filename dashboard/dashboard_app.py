import streamlit as st
import pandas as pd
import sqlite3

# Connect to database
conn = sqlite3.connect("data/student_roles.db")
df = pd.read_sql_query("SELECT * FROM provision_queue", conn)
conn.close()

# Page setup
st.set_page_config(page_title="Provisioning Dashboard", layout="wide")
st.title("🛂 Identity Provisioning Dashboard")

# Sidebar filters
st.sidebar.header("🔍 Filter Users")
user_type = st.sidebar.selectbox("User Type", options=["All", "employee", "student"])
departments = st.sidebar.multiselect("Departments", options=sorted(df["department"].unique()), default=sorted(df["department"].unique()))

# Apply filters
filtered_df = df.copy()
if user_type != "All":
    filtered_df = filtered_df[filtered_df["type"] == user_type]

filtered_df = filtered_df[filtered_df["department"].isin(departments)]

# Metrics
st.markdown("### 📊 Key Metrics")
col1, col2 = st.columns(2)
col1.metric("Total Active Users", len(filtered_df))
col2.metric("Departments", filtered_df["department"].nunique())

# Data Table
st.markdown("### 👥 Provisioning Queue (Live)")
st.dataframe(filtered_df, use_container_width=True)

# Export CSV
st.download_button("📥 Download CSV", data=filtered_df.to_csv(index=False), file_name="provision_queue.csv", mime="text/csv")
