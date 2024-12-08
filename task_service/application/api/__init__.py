from fastapi import FastAPI

from task_service.application.api.routers.task_router import router as tasks

app = FastAPI()

app.include_router(tasks)
