FROM python:3.11-slim

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir flask requests

CMD ["python", "app.py"]

