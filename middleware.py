from fastapi import FastAPI , Request

app = FastAPI()

@app.middleware("https")
async def my_middleware(request: Request , call_next):
    print("request recieved")

    response = await call_next(request)

    print("response sent")

    return response

