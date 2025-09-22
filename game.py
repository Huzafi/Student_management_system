import streamlit as st
import csv
import pandas as pd
import os

# CSV filename
FILENAME = "students.csv"

# Load existing students from CSV
def load_students():
    if os.path.exists(FILENAME):
        return pd.read_csv(FILENAME).values.tolist()
    return []

# Save students to CSV
def save_students(students):
    with open(FILENAME, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Roll Number", "Grade"])  # header
        writer.writerows(students)

# Streamlit App
st.title("🎓 Student Management System")

# Load students in session state
if "students" not in st.session_state:
    st.session_state.students = load_students()

# Tabs
tab1, tab2, tab3 = st.tabs(["➕ Add Student", "📋 View Students", "💾 Save to CSV"])

with tab1:
    st.header("Add Student")
    name = st.text_input("Enter student name")
    roll_number = st.text_input("Enter roll number")
    grade = st.text_input("Enter grade")
    if st.button("Add Student"):
        if name and roll_number and grade:
            st.session_state.students.append([name, roll_number, grade])
            st.success(f"Student {name} added successfully!")
        else:
            st.error("Please fill all fields!")

with tab2:
    st.header("View Students")
    if st.session_state.students:
        df = pd.DataFrame(st.session_state.students, columns=["Name", "Roll Number", "Grade"])
        st.table(df)
    else:
        st.info("No students in the database yet.")

with tab3:
    st.header("Save Data")
    if st.button("Save to CSV"):
        save_students(st.session_state.students)
        st.success(f"Student data saved to {FILENAME}")

