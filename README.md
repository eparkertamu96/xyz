# XYZ API Project

This project builds the XYZ Python FastAPI API application.

## Requiremenst
This project has the following requirements.
- Python 3
- Docker

## Steps to build
To build the Docker image, you can run the following command.

```docker build -t xyz .```

To run the docker image, excute the following command.

```docker run -d --name xyz -p 80:80 xyz``` 