from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return {"Message" : "Hello there Welcome!"}


@app.get("/about")
def about():
    return {"Message" : "This is my second simple main project"}