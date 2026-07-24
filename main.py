from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

todos = []

class Todo(BaseModel):
    id : int
    title : str
    completed : bool