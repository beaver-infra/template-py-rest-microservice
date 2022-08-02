# Template Python REST Microservice

![License](https://img.shields.io/badge/License-MIT-blue)

The repository is a `project template` for REST microservice built using FastAPI (Python). The latest version supports Python 3.8 and above.

## Features

List of features that comes with default template

- [x] Use `FastAPI` as base framework to build the `REST` microservice.
- [x] Predefined `project scaffolding` like files and directories, event handlings, routers, middlewares etc.
- [x] Comes with `default configurations` for hostname, port, environment etc. Each of these configuration can be `customize` as per microservice needs.
- [x] Predefined common `logger` for application logging.
- [x] Preconfigured special routes `/info` and `/health`.
- [x] Use `Docker` to make it easy to run the app on container and shift it.
- [x] Predefined `GitHub Actions` for workflows for `PyLint`, `Python-Package`, `CodeQL`, and `Label`.

## Install

```console
python install -r requirements.txt
```

Run on local/dev env
```console
python app/main.py
```

Open browser or postman and type below APIs to see the response
```console
http://127.0.0.1:8000/api/v1/info
```

```console
http://127.0.0.1:8000/api/v1/health
```
