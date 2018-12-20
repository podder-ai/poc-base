from grpc_tools import protoc

protoc.main((
    '',
    '-I./framework/api/protos',
    '--python_out=./framework/api',
    '--grpc_python_out=./framework/api',
    './framework/api/protos/pipeline_framework.proto',
))
