import json

import pipeline_framework_pb2
import pipeline_framework_pb2_grpc
from app import Task
from framework import Context


class TaskApi(pipeline_framework_pb2_grpc.TaskApiServicer):
    def execute(self, request, _context):
        dag_id = request.dag_id
        context = Context(dag_id)
        inputs = self._convert_to_input_data(request)
        outputs = Task(context).execute(inputs)
        task_response = self._convert_to_task_response(dag_id, outputs)
        return task_response

    def _convert_to_input_data(self, request):
        inputs = []
        for result in request.results:
            inputs.append({
                'resource_id': result.resource_id,
                'content': json.loads(result.content)
            })
        return inputs

    def _convert_to_task_response(self, dag_id: str, outputs):
        task_response = pipeline_framework_pb2.TaskResponse()
        task_response.dag_id = dag_id
        for output in outputs:
            task_response.results.add(
                resource_id=output['resource_id'],
                content=json.dumps(output['content']))
        return task_response
