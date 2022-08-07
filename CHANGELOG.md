# Change Logs

## Format

```
Release <Date> - v<Version>

- [x] Change 1
- [x] Change 2
```

### Notes

* Always keep latest changes on top

## Changes

Release 7th Aug 2022 - v1.0.0

- [x] Use [FastAPI](https://fastapi.tiangolo.com/) as base framework to build the `REST` microservice.
- [x] Use [Poetry](https://python-poetry.org/docs/) as a tool for dependency management and packaging in Python.
- [x] Predefined `project scaffolding` like files and directories, event handlings, routers, middlewares etc.
- [x] Comes with `default configurations` for hostname, port, environment etc. Each of these configuration can be `customize` as per microservice needs.
- [x] Predefined common `logger` for application logging.
- [x] Preconfigured special routes `/info` and `/health`.
- [x] Use `Docker` to make it easy to run the app on container and shift it.
- [x] Predefined `GitHub Actions` for workflows for `PyLint`, `Python-Package`, `CodeQL`, and `Label`.
