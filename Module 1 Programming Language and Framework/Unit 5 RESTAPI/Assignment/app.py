import streamlit as st
import pandas as pd

if 'employee_data' not in st.session_state:
    st.session_state.employee_data = pd.DataFrame(
        columns=['Empno', 'Empname', 'Job', 'Deptno'])

if 'department_data' not in st.session_state:
    st.session_state.department_data = pd.DataFrame(
        columns=['Deptno', 'Dname', 'Loc'])

EMPLOYEE_PAGE = "Employee page"
DEPARTMENT_PAGE = "Department page"
VISUALISE_PAGE = "Visualise data"


def render_employee():
    st.title("Employee Details")
    st.header("Enter details of Employee")
    Empno = st.number_input("Enter Employee Number: ")
    Empname = st.text_input("Enter Employee Name : ")
    Job = st.text_input("Enter Employee job: ")
    Deptno = st.number_input("Enter Department Number: ")

    if st.button("Add Employee"):
        if Empno and Empname and Job and Deptno:
            st.session_state.employee_data.loc[
                len(st.session_state.employee_data)] = [Empno, Empname,
                                                        Job, Deptno]
            st.success("Employee added successfully!")
        else:
            st.error("All fields are required for adding an employee.")


def render_department():
    st.title("Department Details")
    st.header("Enter details of Department")
    Deptno = st.number_input("Enter Department Number: ")
    Dname = st.text_input("Enter Department Name : ")
    Loc = st.text_input("Enter Department location: ")

    if st.button("Add Departmenat"):
        if Deptno and Dname and Loc:
            st.session_state.department_data.loc[
                len(st.session_state.department_data)] = [Deptno, Dname, Loc]
            st.success("Department added successfully!")
        else:
            st.error("All fields are required for adding a department.")


def visualise_data():
    st.title("Visualise data")

    joined_data = pd.merge(st.session_state.employee_data,
                           st.session_state.department_data,
                           on='Deptno', how='inner')
    st.dataframe(joined_data)

    

def main():
    st.sidebar.title('Navigation')
    page_selection = st.sidebar.radio('Go to', [EMPLOYEE_PAGE, DEPARTMENT_PAGE, VISUALISE_PAGE])

    if page_selection == EMPLOYEE_PAGE:
        render_employee()
    elif page_selection == DEPARTMENT_PAGE:
        render_department()
    elif page_selection == VISUALISE_PAGE:
        visualise_data()
        
if __name__ == "__main__" :
    main()
   