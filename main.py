import json
from typing import List

from app import Task
from framework import Context

DAG_ID = "dag_id"
RESOURCE_ID = "resource_id"

def read_inputs_json(context: Context) -> List:
    path = context.config.get('inputs')[0]
    contents = []
    with open(path) as f:
        contents = json.load(f)
    return contents

def generate_inputs(context: Context) -> List:
    contents = read_inputs_json(context)
    inputs = []
    for index, content in enumerate(contents):
        input = {
            "resource_id": RESOURCE_ID + "_" + str(index),
            "content": content
        }
        inputs.append(input)
    return inputs


def execute() -> None:
    context = Context(DAG_ID)
    task = Task(context)
    inputs = generate_inputs(context)
    task.execute(inputs)

if __name__ == "__main__":
    execute()
