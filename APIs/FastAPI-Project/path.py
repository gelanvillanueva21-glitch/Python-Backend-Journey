from fastapi import FastAPI

app = FastAPI()

# @app.get("/users/{user_id}")
# def read_user(user_id: int):
#     return {"User" : user_id}


@app.get("/users/")
def getBook(name: str, user_id: int=None):
    return {"username" : name, "user_id" : user_id}


@app.get("/info/{user_id}/details")
def getInfo(user_id: int, include_email: bool=False):
    if include_email:
        return {"users" : user_id, "include email" : "email include"}
    else:
        return {"users" : user_id, "include email" : "email not include"}
        