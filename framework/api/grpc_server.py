import time
import os
from concurrent import futures

import daemon
import grpc
from daemon import pidfile

import pipeline_framework_pb2_grpc
from framework.api.task_api import TaskApi

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
GRPC_PID_FILE = '/var/run/grpc_server.pid'


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pipeline_framework_pb2_grpc.add_TaskApiServicer_to_server(TaskApi(), server)
    server.add_insecure_port('[::]:50051')
    print("[{}] gRPC server is listening to port: '[::]:50051'".format(time.strftime("%Y-%m-%d %H:%m:%S")))
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    stdout = open(os.environ.get("GRPC_LOG"), 'a')
    stderr = open(os.environ.get("GRPC_ERROR_LOG"), 'a')
    pidfile = daemon.pidfile.PIDLockFile(GRPC_PID_FILE)
    with daemon.DaemonContext(stdout=stdout, stderr=stderr, pidfile=pidfile, detach_process=True):
        serve()
