from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "hello world"}

@app.get("/about")
def about():
    return {"message": "this api project"}

@app.get("/test")
def test():
    return {"msg": "test working"}