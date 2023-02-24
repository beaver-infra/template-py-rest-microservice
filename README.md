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

## Code Structure

Feel free to modify the layout of the repo as much as you want but the given structure is as follows:

```
app/
├── __init__.py
├── main.py
├── api.py
├── metadata.py
├── configs/
│   └── development.py
│   └── production.py
│   └── stage.py
├── core/
│   └── common_handlers.py
├── endpoints/
│   └── health.py
│   └── info.py
│   └── router.py
│   └── users.py
├── middlewares/
│   └── validation.py
└── models/
    └── users.py
├── test_main.py
```

* `__init__.py` defines and initializes the app configuration.

* `main.py` defines the FastAPI application, adds middleware, includes routers, and creates the Mangum handler.

## Setup

### Environment Variables

```console
export <Name>=<Value>

For example:
export BEAVER_API_SYS_INS_TYPE="DEVELOPMENT"
```

:warning: No space before and after `=` sign.

| Name | Purpose | Possible Values |
|:---|:---|:---|
| BEAVER_API_SYS_INS_TYPE | Help to identify system instance type on which the app service is running | `DEVELOPMENT`, `STAGE` and `PRODUCTION` |

### Development

```console
export BEAVER_API_SYS_INS_TYPE="DEVELOPMENT"
```

**Install all dependencies using Pip**

```console
pip install -r requirements.txt
```

**Run the service**

```console
uvicorn "app.main:app" --host="0.0.0.0" --port=8000 --reload
```

**Build & Run the service using Docker**

```console
docker build -t pyrest .
docker run -d -p 8000:8000 pyrest
```

**Run the tests**

```console
pytest
```

**Run the Swagger API Docs**

```console
http://localhost:<PORT>/api/v1/docs
```

**Run the lint**

Run pylint before committing the changes and ensure code quality at least 9.30/10

```console
pylint --rcfile .pylintrc $(git ls-files '*.py')
```

**Run the formatter**

Run black & isort before committing the changes

```console
black app
isort **/*.py
```

### Stage

```console
export BEAVER_API_SYS_INS_TYPE="STAGE"
```

**Install only dependencies (exclude dev-dependencies) using Poetry**
```console
poetry install --no-dev
```

**Run the service**

```console
uvicorn "app.main:app" --host="<STAGE_HOST_IP>" --port=<STAGE_PORT> --workers 2
```

**Run the Swagger API Docs**

```console
http://<STAGE_BASE_URL>:<STAGE_PORT>/api/v1/docss
```

### Production

```console
export BEAVER_API_SYS_INS_TYPE="PRODUCTION"
```

**Install only dependencies (exclude dev-dependencies) using Poetry**
```console
poetry install --no-dev
```

**Run the service**

```console
uvicorn "app.main:app" --host="<PRODUCTION_HOST_IP>" --port=<PRODUCTION_PORT> --workers 4
```

**Run the Swagger API Docs**

```console
http://<PRODUCTION_BASE_URL>:<PRODUCTION_PORT>/api/v1/docs
```

## References

* [Change Logs](CHANGELOGS.md)
* [PyLint Errors](https://vald-phoenix.github.io/pylint-errors/#list-of-errors)
