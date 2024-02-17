from fastapi import Body, FastAPI

api = FastAPI()

@api.get("/hello_world")
def hello_world():
    return {"message": "Hello World"}