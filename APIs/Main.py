from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "Hello World"}

@app.get("/about")
def about():
    return {"name": "Gelan", "role": "Full Stack AI Engineer"}