from app import Task
from framework import Context


def execute() -> None:
    dag_id = 'dag_id'
    context = Context(dag_id)
    task = Task(context)
    inputs = context.config.get('inputs')
    task.execute(inputs)


if __name__ == "__main__":
    execute()
