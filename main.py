import json
from typing import List

from app import Task
from framework import Context

DAG_ID = "dag_id"

def read_inputs_json(context: Context) -> List:
    path = context.config.get('inputs')[0]
    inputs = []
    with open(path) as f:
        inputs = json.load(f)
    return inputs


def execute() -> None:
    context = Context(DAG_ID)
    task = Task(context)
    inputs = read_inputs_json(context)
    task.execute(inputs)

if __name__ == "__main__":
    execute()
