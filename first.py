from fastapi import FastAPI,Path
import json

app = FastAPI()
def load_data():
    with open('users.json','r') as f:
        data = json.load(f)
    return data

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

    return {"message": "User not found"}
