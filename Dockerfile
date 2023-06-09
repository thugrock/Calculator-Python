# Slim version of Python
FROM ubuntu:latest

COPY . /app

WORKDIR /app

# Download Package Information
RUN apt-get update -y

RUN apt-get install python3-pip -y

RUN pip install -r requirements.txt
CMD ["/bin/bash"]
