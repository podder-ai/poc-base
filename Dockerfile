FROM ubuntu:18.04

RUN apt-get update \
&& apt-get install -y python3.6 \
&& apt-get install -y python3-pip \
&& apt-get install -y mysql-client \
&& apt-get install -y libmysqlclient-dev \
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
RUN python ./run_codegen.py

ENV PYTHONPATH "${PYTHONPATH}:/usr/local/python/app:/usr/local/python/framework"
ENV GRPC_ERROR_LOG="/var/log/grpc_server_error.log"
ENV GRPC_LOG="/var/log/grpc_server.log"

CMD python framework/api/grpc_server.py; tail -f $GRPC_ERROR_LOG
