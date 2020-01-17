FROM python:3.6
MAINTAINER wangdachui2014@hotmail.com
WORKDIR /home/Work

# install linux packages
RUN apt-get -o Acquire::Check-Valid-Until=false update \
    && apt-get install -y gunicorn \
    && apt-get clean

# install supporting packages
COPY requirements.txt ./
RUN pip install -r requirements.txt

# copy files
COPY configs configs
COPY auth auth
COPY flaskweb flaskweb
COPY logs logs
COPY services services
COPY static static
COPY templates templates
COPY boot.sh gunicorn_config.py wsgi.py ./

RUN chmod a+x ./boot.sh ./wsgi.py
ENV PYTHONPATH /home/Work

ENTRYPOINT ["./boot.sh"]