# Set the base image from the public repositories.
FROM python:3.8-slim

# Sets the environment variable
ENV PORT=8000

# Copy new files or directories
COPY ./app ./code/app
COPY ./requirements.txt /code/requirements.txt
COPY ./logging.conf ./code/logging.conf

# Set the working directory
WORKDIR /code

# Execute commands to install required packages
RUN pip install --no-cache-dir -r /code/requirements.txt
RUN apt-get update -y
RUN apt-get install curl -y

EXPOSE $PORT

HEALTHCHECK --interval=5m --timeout=1s CMD curl --fail http://localhost:$PORT/api/v1/health || exit 1

CMD uvicorn app.main:app --proxy-headers --host 0.0.0.0 --port $PORT
