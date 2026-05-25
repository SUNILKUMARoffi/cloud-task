from fastapi import Depends
from fastapi import FastAPI
from sqlalchemy.orm import Session

from app.database import Base
from app.database import engine
from app.database import get_db

from app.models import Task

from app.schemas import TaskCreate
from app.schemas import TaskResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Task API Running"}


@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):

    tasks = db.query(Task).all()

    return tasks


@app.post("/tasks", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):

    new_task = Task(title=task.title)

    db.add(new_task)

    db.commit()

    db.refresh(new_task)

    return new_task


@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return {"error": "Task not found"}

    db.delete(task)

    db.commit()

    return {"message": "Task deleted successfully"}