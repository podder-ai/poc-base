from app.task import Task
from podder_task_foundation import Context, settings, MODE

DAG_ID = "___dag_id___"


def main() -> None:
    context = Context(MODE.CONSOLE, DAG_ID)
    task = Task(context)
    task.handle()


if __name__ == "__main__":
    main()
