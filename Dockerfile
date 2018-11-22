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

COPY ./requirements.txt /root/requirements.txt
RUN pip3 install -r /root/requirements.txt

# work directory
COPY . /usr/local/python/
WORKDIR /usr/local/python/

# Compile .proto file
RUN wget https://raw.githubusercontent.com/podder-ai/pipeline-framework/master/modules/app/api/protos/pipeline_framework.proto -P /usr/local/python/framework/api/protos/
RUN python ./run_codegen.py

ENV PYTHONPATH "${PYTHONPATH}:/usr/local/python/app:/usr/local/python/framework"
ENV POC_BASE_ROOT=/usr/local/python
ENV GRPC_ERROR_LOG="/var/log/grpc_server_error.log"
ENV GRPC_LOG="/var/log/grpc_server.log"
ENV GRPC_MAX_WORKERS=10

CMD python framework/api/grpc_server.py; tail -f $GRPC_LOG & tail -f $GRPC_ERROR_LOG
