import os

import daemon
from daemon import pidfile

GRPC_PID_FILE = os.environ.get("GRPC_PID_FILE")

from podder_task_base.api.grpc_server import serve
from app import Task

if __name__ == '__main__':
    stdout = open(os.environ.get("GRPC_LOG"), 'a')
    stderr = open(os.environ.get("GRPC_ERROR_LOG"), 'a')
    pidfile = daemon.pidfile.PIDLockFile(GRPC_PID_FILE)
    with daemon.DaemonContext(
            stdout=stdout, stderr=stderr, pidfile=pidfile,
            detach_process=True):
        serve(execution_task=Task)
