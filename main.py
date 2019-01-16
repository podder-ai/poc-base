import json
import uuid
from typing import List

from app import Task
from framework import Context
from framework.services import InputsService

DAG_ID = "dag_id"

def execute() -> None:
    context = Context(DAG_ID)
    task = Task(context)
    inputs = InputsService.create(context)
    task.execute(inputs)

if __name__ == "__main__":
    execute()
