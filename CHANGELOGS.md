# Change Logs

## Format

```
**Release <Date> - v<Version>**

- [x] Change 1
- [x] Change 2
```

### Notes

* Always keep latest changes on top.

## Changes

**Release 16th Feb 2024 - v1.1.6**

- [x] Add configuration to create K8s `Deployment`, `Pods` and `service` on K8s - verified on single instance (Minikube).

**Release 13th Feb 2024 - v1.1.5**

- [x] Fix docker execution for dev and prod env.
- [x] Fix docker publish config. Switch from GitHub Container Register to DockerHub.

**Release 12th Feb 2024 - v1.1.4**

- [x] Refactor codebase inline comments using GPT-3.5-Turbo model.
- [x] Improve readme documentation.
- [x] Refactor Dockerfile configuration for dev and prod.
- [x] Add `docker-image` and `docker-publish` actions workflow.
- [x] Use `Uvicorn` only for dev env.
- [x] Add support for `Gunicorn with Univorn 4 Workers` for prod env.

**Release 17th Feb 2023 - v1.1.3**

- [x] Format *.py files via `Black` and `isort`.
- [x] Generate `poetry.lock` file.
- [x] Format version in pyproject.toml file.

**Release 13th Dec 2022 - v1.1.2**

- [x] Refactor User APIs downstream data calls
- [x] Setup separate environment for `development`, `stage` and `production`.

**Release 14th Aug 2022 - v1.1.1**

- [x] Fix PyLint errors and warnings.
- [x] Fix `fastapi import error` on PyLint Action job.
- [x] Refactor service scaffolding.
- [x] Fix PyLint, License Tag status reference.

**Release 12th Aug 2022 - v1.1.0**

- [x] Add `Docker` support and document the commands to build the Docker image and run the service.
- [x] Add `Health Check API` interval on Dockerfile config.

**Release 10th Aug 2022 - v1.0.1**

- [x] Use Poetry to `Start the server`.
- [x] Refactor packages path.

**Release 7th Aug 2022 - v1.0.0**

- [x] Use [FastAPI](https://fastapi.tiangolo.com/) as base framework to build the `REST` microservice.
- [x] Use [Poetry](https://python-poetry.org/docs/) as a tool for dependency management and packaging in Python.
- [x] Predefined `project scaffolding` like files and directories, event handlings, routers, middlewares etc.
- [x] Comes with `default configurations` for hostname, port, environment etc. Each of these configuration can be `customize` as per microservice needs.
- [x] Predefined common `logger` for application logging.
- [x] Preconfigured special routes `/info` and `/health`.
- [x] Use `Docker` to make it easy to run the app on container and shift it.
- [x] Add configuration files for workflows includes `GitHub Actions`, `PyLint`, `Python-Package`, `CodeQL`, and `Label`.
