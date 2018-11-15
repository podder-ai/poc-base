import pipeline_framework_pb2_grpc

from app import Task
from framework import Context


class TaskApi(pipeline_framework_pb2_grpc.TaskApiServicer):

    def execute(self, request, _context):
        context = Context()
        res = Task(context).execute(request.results)
        return request
