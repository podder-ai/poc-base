from app import Task
from podder_task_base import Context

DAG_ID = 'dag_id'

'''
*** DO NOT DELETE!! ***
At least one unit test should be executed to pass building docker image job.
'''
def test_if_execute_method_exit():
    context = Context(DAG_ID)
    task = Task(context)
    task.execute([])
