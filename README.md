# Python Lab

This is a small Python practice project.

## What this does

This script uses the `requests` library to access a test HTTP API.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python hello_requests.py
```

## Run with Docker

Build the Docker image:

```bash
docker build -t python-lab .
```

Run the container:

```bash
docker run --rm python-lab
```

The script sends a request to httpbin.org.
Depending on the remote server status, the result may be HTTP 200, HTTP 503, or a timeout.

