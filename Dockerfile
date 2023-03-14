# Slim version of Python
FROM python:3.8.12-slim

COPY . /app

WORKDIR /app

# Download Package Information
RUN apt-get update -y

# Install Tkinter
RUN apt-get install tk -y

RUN pip install -r requirements.txt

