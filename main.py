from fastapi import FastAPI

app = FastAPI()


#query params default value
@app.get("/products")
def get_user(limit: int = 10):
    return {"limit":limit}

#query multiple params
@app.get("/items")
def get_user(name: str = None,price: int = 0):
    return {
        "name":name,
        "PRICE":price
        }

#quert params
"""@app.get("/users")
def get_user(name: str = None):
    return {"name":name}"""