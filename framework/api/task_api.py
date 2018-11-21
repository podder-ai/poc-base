import pipeline_framework_pb2
import pipeline_framework_pb2_grpc

from app import Task
from framework import Context


class TaskApi(pipeline_framework_pb2_grpc.TaskApiServicer):

    def execute(self, request, _context):
        context = Context()
        inputs = self._convert_to_input_data(request)
        outputs = Task(context).execute(inputs)
        task_response = self._convert_to_task_response(outputs)
        return task_response

    def _convert_to_input_data(self, request):
        inputs = []
        for result in request.results:
            inputs.append({'group_id': result.group_id, 'content': result.content})
        return inputs

    def _convert_to_task_response(self, outputs):
        task_response = pipeline_framework_pb2.TaskResponse()
        for output in outputs:
            task_response.results.add(group_id=output['group_id'], content=output['content'])
        return task_response
