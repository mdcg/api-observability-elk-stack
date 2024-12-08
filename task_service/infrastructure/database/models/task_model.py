from sqlalchemy import Boolean, Column, Integer, String

from task_service.domain.entities.task import Task
from task_service.infrastructure.database.connection import Base


class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    is_completed = Column(Boolean, default=False)

    def to_entity(self):
        return Task(id=self.id, title=self.title, description=self.description, is_completed=self.is_completed)
