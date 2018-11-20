from concurrent import futures
import time
import daemon

import grpc
# import pipeline_framework_pb2
import pipeline_framework_pb2_grpc

from framework.api.task_api import TaskApi

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pipeline_framework_pb2_grpc.add_TaskApiServicer_to_server(TaskApi(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC server is listening to port: '[::]:50051'")
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    stdout = open('/var/log/grpc_server.log', 'a')
    stderr = open('/var/log/grpc_server_error.log', 'a')
    with daemon.DaemonContext(stdout=stdout, stderr=stderr, detach_process=True):
        serve()
