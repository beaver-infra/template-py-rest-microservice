# Template Python REST Microservice

[![Pylint](https://github.com/beaver-ai/template-py-rest-microservice/actions/workflows/pylint.yml/badge.svg)](https://github.com/beaver-ai/template-py-rest-microservice/actions/workflows/pylint.yml) [![CodeQL](https://github.com/beaver-ai/template-py-rest-microservice/actions/workflows/codeql.yml/badge.svg)](https://github.com/beaver-ai/template-py-rest-microservice/actions/workflows/codeql.yml) [![License](https://img.shields.io/badge/License-MIT-blue)](https://github.com/beaver-ai/template-py-rest-microservice/blob/main/LICENSE)

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
- [x] Predefined `GitHub Actions` for workflows for `PyLint` and `CodeQL`.

## Setup

### Global Environment Variables

```console
export BEAVER_API_SYS_INS_TYPE="DEVELOPMENT"
```
Possible values - `DEVELOPMENT`, `STAGE` and `PRODUCTION`.


### Install

#### Using Poetry

```console
poetry install
```

Pass `--no-dev` to install without dev dependencies.

#### Using Pip

```console
pip install -r requirements.txt
```

### Build

#### Using Docker

```console
docker build -t pyresttemplate .
```

### Run the app

#### Using Uvicorn in Dev env

```console
uvicorn "app.main:app" --host="0.0.0.0" --port=8000 --reload
```

#### Using Docker in Dev env

```console
docker run -d -p 8000:8000 pyresttemplate
```

### Run the tests

#### On Dev env

```console
pytest
```

### Run the API Swagger Docs

#### On Dev env

```console
http://localhost:<PORT>/api/v1/docss
```

## Other useful commands

Any new package installation, should generate the requirements.txt as well. Generate `requirements.txt` from `poetry.lock`
```console
poetry export --output requirements.txt
```

Validate pyproject.toml
```console
poetry check
```

(!) Avoid using, Docker will reset and all image cache will be cleaned.
```console
docker system prune -a
```

## References

* [Change Logs](CHANGELOG.md)
* [PyLint Errors](https://vald-phoenix.github.io/pylint-errors/#list-of-errors)
