FROM python:3.8-slim-buster

# set work directory
WORKDIR /forcode

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get update
RUN apt-get install -y python3-dev gcc libc-dev libffi-dev
RUN apt-get -y install libpq-dev gcc 

# # install dependencies
# COPY requirements.txt .
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

COPY Pipfile Pipfile.lock /forcode/
RUN pip install pipenv && pipenv install --system --deploy
ADD . /forcode

COPY entry.sh /entry.sh
RUN chmod +x /entry.sh
COPY . /forcode
 