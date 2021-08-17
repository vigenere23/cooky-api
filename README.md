# Cooky

[![Build (master)](https://github.com/vigenere23/Cooky/actions/workflows/build-master.yml/badge.svg)](https://github.com/vigenere23/Cooky/actions/workflows/build-master.yml)

Welcome to Cooky, the amazing recipe sharing app that let's you buy ingredients on the go!

![cooky](https://user-images.githubusercontent.com/32545895/78456681-1858a280-7673-11ea-9ddd-ba089f6616f3.png)

## Setup

### Requirements

- [Taskfile](https://taskfile.dev/#/) for managing task commands
- [Docker](https://docs.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) for managing machine environments

### Quick start

To start all 3 services with their setups, run

```shell
task start+logs
```

A bunch of other commands are available to start in background, rebuild and setup single services. Use `task --list` to list all available tasks.

**Exposed ports**:

- UI : 8080
- API : 8081
- DB : 8082

**Test credentials**:

- username: test
- password: test

## API Documentation

Available [here](./api_doc/README.md).

## Contributors

- Gabriel St-Pierre ([@vigenre23](https://github.com/vigenere23))
- Olivier Gingras ([@olgin2](https://github.com/olgin2))

## Screenshots

![Cooky screenshot 1](https://user-images.githubusercontent.com/32545895/72568296-d2ffb280-3885-11ea-8338-9c9d1f03b47c.png)
![Cooky screenshot 2](https://user-images.githubusercontent.com/32545895/72568223-a055ba00-3885-11ea-84c2-daaf5780dd19.png)
![Cooky screenshot 3](https://user-images.githubusercontent.com/32545895/72568425-1f4af280-3886-11ea-9a93-9b5053651ffd.png)
![Cooky screenshot 4](https://user-images.githubusercontent.com/32545895/72568500-499cb000-3886-11ea-8934-d37a8fdbb822.png)
