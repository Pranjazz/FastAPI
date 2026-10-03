from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todos(BaseModel):
    id:int
    task:str
    status:bool

@app.post("/todos")
def create_todo(todo_item: Todos):
    todos.append(todo_item)
    return {"message":"Todo added","data":todo_item}

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo_id == todo.id:
            return todo
    return {"ERROR":"todo_id not found"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,updated_todo:Todos ):
    for index,todo in enumerate(todos):
        if todo_id == todo.id:
            todos[index] = updated_todo
            return {
                "message":"data updated",
                "data":updated_todo
            }
    return {"ERROR":"todo_id not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
        if(todo.id == todo_id):
            todos.pop(index)
            return{
                "message":"data deleted"
            }
    return {"ERROR":"todo_id not found"}
