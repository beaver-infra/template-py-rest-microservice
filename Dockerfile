# Set the base image from the public repositories.
FROM python:3.8-slim as base

# Set the environment variables
ENV POETRY_VERSION=1.1.14
ENV PORT=8000
    
# Set the working directory
WORKDIR /berver-ai

# Copy new files or directories
COPY ./app ./app
COPY pyproject.toml poetry.lock README.md logging.conf ./

# Execute commands to install required packages
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION" uvicorn gunicorn
RUN poetry install --no-dev

# HEALTHCHECK --interval=5m --timeout=3s \
#   CMD curl -f "http://localhost:$PORT/api/v1/health" || exit 1

EXPOSE 8000

CMD ["poetry", "run", "start"]
