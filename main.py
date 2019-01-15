import json
import uuid
from typing import List

from app import Task
from framework import Context

DAG_ID = "dag_id"

def read_inputs_json(context: Context) -> List:
    json_path = context.config.get('inputs')[0]
    with open(json_path) as f:
        return json.load(f)

def generate_inputs(context: Context) -> List:
    json_data = read_inputs_json(context)
    inputs = []
    for index, job_data in enumerate(json_data):
        inputs.append({
            "job_id": str(uuid.uuid4()),
            "job_data": job_data
        })
    return inputs


def execute() -> None:
    context = Context(DAG_ID)
    task = Task(context)
    inputs = generate_inputs(context)
    task.execute(inputs)

if __name__ == "__main__":
    execute()
