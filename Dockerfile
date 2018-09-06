FROM ubuntu:latest
MAINTAINER tuantranf "tuantranf@gmail.com"

# Python 3.5
#
# For convenience, alias (but don't sym-link) python & pip to python3 & pip3 as recommended in:
# http://askubuntu.com/questions/351318/changing-symlink-python-to-python3-causes-problems

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN pip3 install --no-cache-dir --upgrade pip setuptools && \
    echo "alias python='python3'" >> /root/.bash_aliases && \
    echo "alias pip='pip3'" >> /root/.bash_aliases

# work directory
COPY . /usr/local/python/

WORKDIR /usr/local/python/

RUN pip install -r requirements.txt

CMD python main.py
