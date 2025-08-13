from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def add(a:int,b:int):
    return a + b

@app.get("/tanish")
def multiply(a:int,b:int):
    return a * b 

class Dividemodel(BaseModel):
    a:int
    b:int

def divide(a:int,b:int):
    return a / b if b!= 0 else "Division by zero is not allowed"

@app.post("/tanish/divide")
def divide_endpoint(model: Dividemodel):
    return divide(model.a,model.b)