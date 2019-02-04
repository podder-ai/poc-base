"""
DO NOT MODIFY THIS FILE.
"""

import os

from app import Task
from podder_task_base.api.grpc_server import run_grpc_server

DEFAULT_GRPC_PID_FILE = "/var/run/poc_base.pid"
DEFAULT_PORT = 50051
DEFAULT_MAX_WORKERS = 10

if __name__ == '__main__':
    """
    Run gRPC server.
    """
    stdout = open(os.getenv("GRPC_LOG"), 'a')
    stderr = open(os.getenv("GRPC_ERROR_LOG"), 'a')
    pidfile = os.getenv("GRPC_PID_FILE", DEFAULT_GRPC_PID_FILE)
    max_workers = os.getenv("GRPC_MAX_WORKERS", DEFAULT_MAX_WORKERS)
    port = os.getenv("GRPC_PORT", DEFAULT_PORT)

    run_grpc_server(stdout, stderr, pidfile, Task, max_workers, port)
