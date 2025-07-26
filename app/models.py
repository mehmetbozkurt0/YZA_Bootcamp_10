from pydantic import BaseModel

class TaskModel(BaseModel):
    text: str
    completed: bool = False

class TaskUpdateModel(BaseModel):
    task_id:int
    completed: bool