"""
DO NOT MODIFY THIS FILE.
"""

import os

from app import Task
from podder_task_base.api.grpc_server import run_grpc_server

if __name__ == '__main__':
    """
    Run gRPC server.
    """
    stdout = open(os.environ.get("GRPC_LOG"), 'a')
    stderr = open(os.environ.get("GRPC_ERROR_LOG"), 'a')
    pidfile = os.environ.get("GRPC_PID_FILE")
    run_grpc_server(stdout, stderr, pidfile, Task)
