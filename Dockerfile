FROM ubuntu:18.04

RUN apt-get update \
&& apt-get install -y python3.6 \
&& apt-get install -y python3-pip \
&& apt-get install -y mysql-client \
&& apt-get install -y libmysqlclient-dev \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# work directory
COPY . /usr/local/python/

WORKDIR /usr/local/python/

RUN pip install -r requirements.txt

CMD python main.py
