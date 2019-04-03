FROM ubuntu:18.04

RUN apt-get update -y \
&& apt-get install -y python3.6 \
&& apt-get install -y python3-pip \
&& apt-get install -y mysql-client \
&& apt-get install -y libmysqlclient-dev \
&& apt-get install -y wget \
&& apt-get install -y locales \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/* \
&& cd /usr/local/bin \
&& ln -s /usr/bin/python3 python \
&& pip3 install --upgrade pip

# locale setting
RUN locale-gen en_US.UTF-8
ENV LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    PYTHONIOENCODING=utf-8

# setting environments
ENV POC_BASE_ROOT=/usr/local/poc_base
ENV PYTHONPATH="${PYTHONPATH}:${POC_BASE_ROOT}/app" \
    GRPC_ERROR_LOG="/var/log/grpc_server_error.log" \
    GRPC_LOG="/var/log/grpc_server.log" \
    GRPC_MAX_WORKERS=10 \
    GRPC_PID_FILE="/var/run/poc_base.pid"

# install
RUN pip3 install 'podder-task-base>=0.1.7,<0.2.0'

# Task Initializer
WORKDIR ${POC_BASE_ROOT}
RUN python -m podder_task_base.task_initializer init podder-task

# python packages(default)
RUN pip3 install -r ${POC_BASE_ROOT}/requirements.default.txt

COPY ./requirements.txt ${POC_BASE_ROOT}/requirements.txt
RUN pip3 install -r ${POC_BASE_ROOT}/requirements.txt

# work directory
COPY . ${POC_BASE_ROOT}
WORKDIR ${POC_BASE_ROOT}

# Compile .proto file for gRPC
RUN python ./run_codegen.py

RUN chmod +x ./scripts/entrypoint.sh
CMD ["./scripts/entrypoint.sh"]
