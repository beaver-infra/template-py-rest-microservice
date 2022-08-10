# Template Python REST Microservice

![License](https://img.shields.io/badge/License-MIT-blue)

[![CodeQL](https://github.com/beaver-ai/template-py-rest-microservice/actions/workflows/codeql.yml/badge.svg)](https://github.com/beaver-ai/template-py-rest-microservice/actions/workflows/codeql.yml)

The repository is a `project template` for REST microservice built using FastAPI (Python). The latest version supports Python 3.8 and above.

## Prerequisite

Required

* [Python 3.8 or above](https://www.python.org/downloads/).
* [Poetry](https://python-poetry.org/)

Optional

* [Docker](https://www.docker.com/)

## Features

List of features that comes with default template

- [x] Use [FastAPI](https://fastapi.tiangolo.com/) as base framework to build the `REST` microservice.
- [x] Use [Poetry](https://python-poetry.org/docs/) as a tool for dependency management and packaging in Python.
- [x] Predefined `project scaffolding` like files and directories, event handlings, routers, middlewares etc.
- [x] Comes with `default configurations` for hostname, port, environment etc. Each of these configuration can be `customize` as per microservice needs.
- [x] Predefined common `logger` for application logging.
- [x] Preconfigured special routes `/info` and `/health`.
- [x] Use `Docker` to make it easy to run the app on container and shift it.
- [x] Predefined `GitHub Actions` for workflows for `PyLint`, `Python-Package`, `CodeQL`, and `Label`.

## Install

Install dependencies
```console
poetry install
```

Pass `--no-dev` to install without dev dependencies.

Install dependencies via Docker
```console
docker build -t beaver-ai/py-rest-template .
```

## Run the app

**Dev environment**

Run directly
```console
poetry run start
```

Run via Docker
```console
docker run -it -d -p 8000:5000 beaver-ai/py-rest-template
```

## Tests

```console
pytest
```

## References

* [Change Logs](CHANGELOG.md)
