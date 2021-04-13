
FROM python:3.7-slim-buster
COPY . /src
WORKDIR /src
RUN pip3 install -r /src/requirements.txt
ENV PYTHONUNBUFFERED=TRUE
ENTRYPOINT ["python3"]
