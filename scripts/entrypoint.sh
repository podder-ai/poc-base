#!/usr/bin/env bash

echo "Starting process..."

kill_grpc_process() {
    echo "gRPC pid file already exists."
    ps -ef | grep python | grep -v grep | awk '{print $2}' | xargs kill
    rm -f $GRPC_PID_FILE
    echo "Stopped existing gRPC process."
}

if [ -f $GRPC_PID_FILE ]; then
    kill_grpc_process
    echo "Restarting gRPC server..."
    python api/grpc_server.py
else
    echo "Starting gRPC server..."
    python api/grpc_server.py; tail -f $GRPC_LOG & tail -f $GRPC_ERROR_LOG
fi
