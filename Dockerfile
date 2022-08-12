# Set the base image from the public repositories.
FROM python:3.8-slim

# Copy new files or directories
COPY ./app ./code/app
COPY ./requirements.txt /code/requirements.txt
COPY ./logging.conf ./code/logging.conf

# Set the working directory
WORKDIR /code

# Execute commands to install required packages
RUN pip install --no-cache-dir -r /code/requirements.txt

EXPOSE 8000

CMD uvicorn app.main:app --proxy-headers --host 0.0.0.0 --port 8000
