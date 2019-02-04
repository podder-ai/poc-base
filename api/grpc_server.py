"""
DO NOT MODIFY THIS FILE.
"""

import os

from api.task_api import PocBaseApi
from app import Task
from podder_task_base.api.grpc_server import GrpcServer
from protos import pipeline_framework_pb2_grpc

DEFAULT_GRPC_PID_FILE = "/var/run/poc_base.pid"
DEFAULT_PORT = 50051
DEFAULT_MAX_WORKERS = 10

if __name__ == '__main__':
    """
    Run gRPC server.
    """
    GrpcServer(
        stdout=open(os.getenv("GRPC_LOG"), 'a'),
        stderr=open(os.getenv("GRPC_ERROR_LOG"), 'a'),
        pidfile=os.getenv("GRPC_PID_FILE", DEFAULT_GRPC_PID_FILE),
        max_workers=os.getenv("GRPC_MAX_WORKERS", DEFAULT_MAX_WORKERS),
        port=os.getenv("GRPC_PORT", DEFAULT_PORT),
        execution_task=Task,
        add_servicer_method=pipeline_framework_pb2_grpc.add_PocBaseApiServicer_to_server,
        task_api_class=PocBaseApi).run()
