from fastapi import FastAPI,Path,HTTPException,Query
from pydantic import BaseModel, Field
from typing import Annotated
import json
from datetime import datetime
from fastapi.responses import JSONResponse

app = FastAPI()

class user(BaseModel):
    name: Annotated[str, Field(..., description="User name")]
    email: Annotated[str, Field(..., description="Email id")]
    phone: Annotated[str, Field(..., description="Enter phone number")]
    check_in_date: Annotated[datetime, Field(..., description="Check-in date")]
    check_out_date: Annotated[str, Field(..., description="Enter check_out_date")]
    total_guest:Annotated[int, Field(..., description="Number of guest")]

user_info = {'name':'khushi', 'age': 12, 'contact_details':{'email':'abc@gmail.com','phone':'23456780'} , 'check_in_date':2-06-2025, 'check_out_date': 5-06-2025 ,'total_guest':6}    

user1 = user(**user_info)


def load_data():
    with open('users.json','r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('users.json','w') as f:
        json.dump(data,f)

@app.get("/")
def hello():
    return {"message": "User Management System"}

@app.get("/about")
def about():
    return {"message": "Fully Functional API to manage user management System"}

@app.get("/test")
def test():
    return {"msg": "test working"}

@app.get('/view')
def view():
    data = load_data()
    return data['customers']



@app.get('/view/{user_id}')
def view_user(user_id: int = Path(..., description="The ID of the user to retrieve", example=1)):
    data = load_data()
    customers = data["customers"]   # access customers list

    for user in customers:
        if user["customer_id"] == user_id:
            return user

    raise HTTPException(status_code=404, detail="User not found")

@app.get('/sort')
def sort_users(sort_by: str = Query(..., description="The field to sort by (customer_id, name, email, age)", example="name"), order: str = Query("asc", description="Sort order (asc or desc)", example="asc")):
    data = load_data()
    customers = data["customers"]

    if sort_by not in ["customer_id", "name", "email", "age"]:
        raise HTTPException(status_code=400, detail="Invalid sort field")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid sort order")

    sorted_users = sorted(customers, key=lambda x: x.get(sort_by, 0), reverse=(order == "desc"))
    return sorted_users

@app.post('/create')
def create_user(user:user):
        data = load_data

        if user.id.data:
            raise HTTPException(status_code=400,detail='User already existing')
        
        #new user adding
        data[user.id]=user.model_dump(exclude=['id'])

        #save into json file 

        save_data(data)
        return JSONResponse(status_code=201,content={'message':'patient created successfuly'})


