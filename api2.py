from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_db = {
    1: {"name": "tanish", "age" : 22},
    2: {"name": "Sourabh", "age" : 22},
    3: {"name": "Krishna", "age": 23}
}

class User(BaseModel):
    name: str
    age: int


@app.put("/update/{user_id}")
def update_user(user_id: int, user: User):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        return {"message" : "User updated successfully"}
    else:
        return {"message": "User not found"}


@app.delete("/delete'{user_id}")
def delete_user(user_id: int):
    if user_id in user_db:
        del user_db[user_id]
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}