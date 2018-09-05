from app import Task
from framework import Context


def execute() -> None:
    context = Context()
    Task(context).execute()


if __name__ == "__main__":
    execute()
