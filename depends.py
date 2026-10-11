from fastapi import FastAPI , Depends

app = FastAPI()

def common_logic():
    return {
        "message":"common logic executed"
    }

@app.get("/home")
def home(data = Depends(common_logic)):
    return data

def get_curr_user():
    return {
        "user":"connection successful"
    }

@app.get("/profile")
def profile (user = Depends(get_curr_user)):
    return user

@app.get("/dashboard")
def dashboard(user = Depends(get_curr_user)):
    return user

