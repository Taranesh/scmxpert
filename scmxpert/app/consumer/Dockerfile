
# Base image
FROM python:3.8.10

# Set the working directory
WORKDIR /app/consumer

# Copy the socket server file to the container
COPY . /app/consumer

RUN pip install -r requirements.txt 

CMD python -u consumer.py

