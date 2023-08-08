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







@app.put("/employees/{employee_id}", response_model=Employee)
async def update_employee(employee_id: int, employee_update: EmployeeCreate):
    cursor.execute("SELECT id FROM employee WHERE id=?", (employee_id,))
    existing_employee = cursor.fetchone()
    if not existing_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    cursor.execute(
        "UPDATE employee SET name=?, department=? WHERE id=?",
        (employee_update.name, employee_update.department, employee_id),
    )
    conn.commit()
    return {"id": employee_id, **employee_update.dict()}

@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):
    cursor.execute("SELECT id FROM employee WHERE id=?", (employee_id,))
    existing_employee = cursor.fetchone()
    if not existing_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    cursor.execute("DELETE FROM employee WHERE id=?", (employee_id,))
    conn.commit()
    return {"message": "Employee deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


