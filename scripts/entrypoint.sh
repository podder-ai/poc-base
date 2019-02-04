#!/usr/bin/env bash

rm -f $GRPC_PID_FILE
python api/grpc_server.py; tail -f $GRPC_LOG & tail -f $GRPC_ERROR_LOG
