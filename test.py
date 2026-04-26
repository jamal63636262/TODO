from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

todos = []
next_id = 1 

now = datetime.now()

created_at = now.strftime("%Y-%m-%d-%M-%S")

@app.post("/todos")
def creat_todo(title: str): 
    global next_id
    todo = {"id":next_id, "title": title, "done": False, "created_at": created_at}
    todos.append(todo)
    next_id += 1 
    return todo 

@app.get("/todos")
def get_all_todos(): 
    return todos

@app.get("/todos/{todo_id}")
def get_one_todo(todo_id: int):
    for todo in todos: 
        if todo["id"] == todo_id: 
            return todo 
    return{"error": "Дело не найдено"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, title: str = None, done:bool = None):
    for todo in todos:
        if todo["id"] == todo_id: 
            if title is not None: 
                todo["title"] = title
            if done is not None: 
                todo["done"] = done 
            return todo 
    return {"error": "Дело не найдено"}

@app.delete("/todos/{todo_id}") 
def delete_todo(todo_id: int): 
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id: 
            todos.pop(i)
            return {"message": f"Дело {todo_id} удалено"}
    return {"error":"Дело не найдено"}

@app.delete("/todos") 
def del_all_todos():
    global todos 
    todos.clear()
    return {"message": "Список дел очищен!"}

@app.get("/todos/count")
def count_todos():
    return {"Всего задач": len(todos)}

@app.get("/todos")
def get_done_or_not(done: bool = None):
    if done is None: 
        return todos 
    if done is True: 
        result = []
        for todo in todos: 
            if todo["done"] == True: 
                result.append(todo)
        return result   
    if done is False: 
        result = []
        for todo in todos:
            if todo["done"] == False: 
                result.append(todo) 
        return result
    
@app.get("/todos")
def get_all_todos(done: bool = None, sort: str = None):
    result = todos  

    if done is not None: 
        result = [todo for todo in result if todo["done"] == done]

    if sort == "created_at": 
       result = sorted(result, key=lambda x: x["created_at"], reverse = True) 

    if limit is not None: 
        result = result[offset:offset + limit]

    return result


    
    
