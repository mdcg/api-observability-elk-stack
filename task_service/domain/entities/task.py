from typing import Optional

from pydantic import BaseModel


class Task(BaseModel):
    id: Optional[int] = None
    is_completed: Optional[bool] = False
    title: str
    description: str
