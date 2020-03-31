FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY setup.py /code/
RUN pip install -e .
COPY . /code/
