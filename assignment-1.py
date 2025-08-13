# Question 1

from urllib.request import Request
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class Multiply_model(BaseModel):
    a: int
    b: int

def multiply(a: int, b: int):
    return a * b

@app.post("/multiply")
def multiply_endpoint(model: Multiply_model):
    return {"result": multiply(model.a, model.b)}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for err in exc.errors():
        field_name = " - ".join(str(loc) for loc in err["loc"] if isinstance(loc, str))
        errors.append(f"{field_name} must be a valid integer")
    
    return JSONResponse(
        status_code=422,
        content={"detail": errors}
    )


# Question 2
from fastapi import HTTPException
class Calculator(BaseModel):
    a: float
    b: float
    operation: str

def calculate(a:float,b:float,operation:str):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            raise HTTPException(status_code=400,detail="Division by zero is not allowed")
        return a / b
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

@app.post("/calculator")
def calculator(data: Calculator):
    result = calculate(data.a,data.b,data.operation)
    return result


# Question 3
from pydantic import EmailStr, Field
from typing import List 

registered_users = []

class User(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(...,min_length=8)


@app.post("/register")
def register_user(user: User):
    for u in registered_users:
        if u.email == user.email:
            raise HTTPException(status_code=400, detail="Email already registered")
    registered_users.append(user)
    return {"message": "User registered successfully"}


@app.get("/users")
def get_users():
    return registered_users
