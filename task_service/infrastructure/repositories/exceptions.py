class TaskNotFoundError(Exception):
    def __init__(self, task_id: int):
        super().__init__(f"Tarefa com ID {task_id} não foi encontrada.")
