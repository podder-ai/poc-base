FROM ubuntu:18.04

RUN apt-get update \
&& apt-get install -y python3.6 \
&& apt-get install -y python3-pip \
&& apt-get install -y mysql-client \
&& apt-get install -y libmysqlclient-dev \
&& apt-get install -y wget \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/* \
&& cd /usr/local/bin \
&& ln -s /usr/bin/python3 python \
&& pip3 install --upgrade pip

# locale setting
RUN apt-get update \
    && apt-get install -y locales
RUN locale-gen en_US.UTF-8
ENV LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    PYTHONIOENCODING=utf-8

# python packages
COPY ./requirements/requirements.txt /root/requirements.txt
RUN pip3 install -r /root/requirements.txt

# work directory
ENV POC_BASE_ROOT=/usr/local/poc_base
COPY . ${POC_BASE_ROOT}
WORKDIR ${POC_BASE_ROOT}

ENV PYTHONPATH="${PYTHONPATH}:${POC_BASE_ROOT}/app" \
    GRPC_ERROR_LOG="/var/log/grpc_server_error.log" \
    GRPC_LOG="/var/log/grpc_server.log"

# Compile .proto file for gRPC
RUN python ./run_codegen.py

RUN chmod +x ./scripts/entrypoint.sh
CMD ["./scripts/entrypoint.sh"]
