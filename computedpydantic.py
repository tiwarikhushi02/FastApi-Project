from pydantic import BaseModel, EmailStr, Field,computed_field
from typing import List, Dict ,Optional, Annotated

class Users(BaseModel):
    name:str = Field(max_length=50)
    age:int = Field(gt=0,lt=120)
    email: EmailStr     
    weight:float #kg
    height:float #mts
    gender:str
    married:bool
    contact_details:dict[str,str]
    address:Annotated[str,Field(max_length=100,title="Please enter address",description='give correct address',example=['los angles'])]

def insert_users_data(user: Users):
    print(user.name)
    print(user.age)
    print("inserted")

def update_users_data(user: Users):
    print(user.name)
    print(user.age)
    print('BMI',user.calculate_bmi)
    print("updated")    

@computed_field
@property
def calculated_bmi(self) -> float:
    return round(self.weight / (self.height ** 2), 2)

users_info = {'name':'khushi', 'age': 12, 'gender':'female','married':'no', 'contact_details':{'email':'abc@gmail.com','phone':'23456780'} }    

user1 = Users(**users_info)

insert_users_data(user1)
