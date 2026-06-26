FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY hello_requests.py .

CMD ["python", "hello_requests.py"]
