from fastapi import FastAPI , status , HTTPException

app = FastAPI()

@app.post("/create_user",status_code = status.HTTP_201_CREATED)
def created_user():
    return {
        "message":"user created"
    }

@app.get("/user")
def get_user():
    return{
        "status":"success",
        "message":"user fetched",
        "data":{
            "name":"pranjal",
             "age": 21
        }
    }
#HTTP EXCEPTION HANDLING OR CUSTOM EXCEPTION HANDLING
@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=" User not found"
        )
    return {
        "id":1,
        "name":"Pranjal"
    }

#here we learnt the http exception  

