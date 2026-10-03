from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    email:str

@app.post("/create_User")
def create_User(user:User):
    return {
        "message":"User is created",
        "data":User
    }