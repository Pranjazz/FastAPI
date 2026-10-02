from fastapi import FastAPI

app = FastAPI()

#post api
@app.post("/create_user")
def create_user(name:str,age=int):
    return{
        "name":name,
        "age":age
    }