from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, MetaData, Table, create_engine
from databases import Database
import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

database = Database(DATABASE_URL)
metadata = MetaData()

tasks = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("description", String),
    Column("completed", Boolean, default=False),
)

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

class TaskIn(BaseModel):
    title: str
    description: str
    completed: bool = False

class TaskOut(TaskIn):
    id: int

@app.get("/")
async def root():
    return {"mensagem": "API FastAPI com PostgreSQL no Docker"}

@app.get("/tasks", response_model=list[TaskOut])
async def get_tasks():
    query = tasks.select()
    return await database.fetch_all(query)

@app.post("/tasks", response_model=TaskOut)
async def create_task(task: TaskIn):
    query = tasks.insert().values(
        title=task.title,
        description=task.description,
        completed=task.completed,
    )
    task_id = await database.execute(query)
    return {**task.model_dump(), "id": task_id}

@app.put("/tasks/{task_id}", response_model=TaskOut)
async def update_task(task_id: int, task: TaskIn):
    query = tasks.update().where(tasks.c.id == task_id).values(
        title=task.title,
        description=task.description,
        completed=task.completed,
    )
    result = await database.execute(query)
    if result == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    # Retorna a task atualizada
    query = tasks.select().where(tasks.c.id == task_id)
    updated_task = await database.fetch_one(query)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    result = await database.execute(query)
    if result == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return None
