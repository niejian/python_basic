# _*_ utf-8 _*_
# @time: 2024/2/26 
# @author: nj
# @file: main
# @project: python_basic2

from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
async def index():
    return "index"

@app.get("/hello/{name}")
async def name(name: str, resp: Response):
    msg = f"hello, {name}"
    print(msg)
    resp.headers["Content-type"] = "application/json"
    return {"msg": msg}

class User(BaseModel):
    name: str
    age: int
    def __init__(self, name, age):
        super().__init__(name=name, age=age)


@app.get("/user/{name}/{age}")
async def get_user(name: str, age: int):
    user = User(name, age)
    return user


