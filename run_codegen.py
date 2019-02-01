from grpc_tools import protoc

protoc.main((
    '',
    '-I./api/protos',
    '--python_out=./api',
    '--grpc_python_out=./api',
    './api/protos/pipeline_framework.proto',
))
