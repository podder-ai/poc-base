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

# work directory
COPY . /usr/local/python/

WORKDIR /usr/local/python/

RUN pip3 install -r requirements.txt
