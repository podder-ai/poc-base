from app import Task
from framework import Context


def execute() -> None:
    context = Context()
    task = Task(context)
    inputs = context.config.get('inputs')
    task.execute(inputs)


if __name__ == "__main__":
    execute()
