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

**Draft**

- [ ] Use Poetry for execute `Build` and `Test` commands.
- [ ] Refactor service logger setup and configurations, sidecar container and add logger samples.
- [ ] Add `Rate limiting` sample.
- [ ] Setup `Uvicorn`, `Gunicorn` and `Hypercorn`.
- [ ] Add sample test cases.
- [ ] Refactor `.github/workflows`.
- [ ] Setup and Refactor `GitHub Action`.
- [ ] Setup separate environment for `development`, `stage` and `production`.

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
