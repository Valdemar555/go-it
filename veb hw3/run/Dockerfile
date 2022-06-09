FROM python:latest

MAINTAINER Vladimir Cherevko "volodumurcherevko555@gmail.com"

WORKDIR /run

COPY . /run

RUN pip install pipenv
RUN pipenv install


ENTRYPOINT ["pipenv", "run","python","main.py"]
