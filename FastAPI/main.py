from fastapi import FastAPI
from schemas import Todo as TodoSchema

app = FastAPI()

#Dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#POST - Create TODO
@app.post("/todos",response_model=TodoSchema)
def create(todo: TodoSchema, db: Session = Depends(get_db)):
    db_todo = Todo(title=todo.title, description=todo.description, completed=todo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo