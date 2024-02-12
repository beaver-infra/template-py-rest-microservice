# Set the base image from the official Python 3.8 slim image.
FROM python:3.8-slim

# Set environment variables
ENV SERVER_PORT=3000

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt ./

# Update package lists and install necessary dependencies
RUN apt-get update -y \
    && apt-get install -y curl \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire local directory to the working directory
COPY . .

# Expose the container's specified network ports at runtime
EXPOSE $SERVER_PORT

# Healthcheck to verify container is still working
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s \
    CMD curl --fail http://localhost:$SERVER_PORT/api/v1/health || exit 1

# Default command to execute when the container starts
CMD gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 127.0.0.1:3000
