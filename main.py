from app import Task
from framework import Context
from framework.services import InputsService
from framework import settings

DAG_ID = "dag_id"


def execute() -> None:
    settings.init()
    context = Context(DAG_ID)
    task = Task(context)
    inputs = InputsService(context).create()
    task.execute(inputs)


if __name__ == "__main__":
    execute()
