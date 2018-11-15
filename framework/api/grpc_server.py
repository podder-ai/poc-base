from concurrent import futures
import time

import grpc
import pipeline_framework_pb2
import pipeline_framework_pb2_grpc

# from app import Task

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Task(pipeline_framework_pb2_grpc.TaskServicer):

    def execute(self, request, context):
        # for input in request:
        # task_output = pipeline_framework_pb2.TaskOutput(group_id=request.group_id, content=request.content)
        return request


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pipeline_framework_pb2_grpc.add_TaskServicer_to_server(Task(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC server is listening to port: '[::]:50051'")
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
