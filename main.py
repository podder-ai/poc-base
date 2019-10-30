from app.task import Task
from podder_task_foundation import MODE, Context

DAG_ID = "___dag_id___"


def main() -> None:
    context = Context(MODE.CONSOLE, DAG_ID)
    task = Task(MODE.CONSOLE)
    task.handle(DAG_ID)


if __name__ == "__main__":
    main()
