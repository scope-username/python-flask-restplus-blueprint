FROM ubuntu:latest
MAINTAINER Scope Username "46004421+scope-username@users.noreply.github.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]