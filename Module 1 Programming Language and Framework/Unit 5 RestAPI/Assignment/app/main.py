from fastapi import FastAPI, HTTPException, Depends
from database import cursor, conn
from models import Employee, EmployeeCreate

app = FastAPI()

@app.on_event("startup")
# Create a Table 

@app.get("/employees/")
# return table

@app.get("/employees/{employee_id}")
# return table based on employee id

@app.post("/employees/")
# insert data into the table

@app.delete("/employees/{employee_id}")
# delete data from a table using employee_id 

@app.put("/employees/{employee_id}/{column}/{new_value}")
# update the table using employeeid and set new value of a column