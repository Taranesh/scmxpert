
# Base image
FROM python:3.8.10


# Set the working directory
WORKDIR ./socket
# Copy the socket server file to the container
COPY . /socket

# # Copy the socket server file to the container
# COPY ./scmxpertlite/scmxpert/app/socket/server.py .
RUN pip3 install kafka-python
# Expose the port on which the socket server will run
EXPOSE 12345

# Run the socket server
CMD ["python3", "server.py"]



