FROM python:3.10-slim

WORKDIR /app

# Install pip requirements directly, no apt needed
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --break-system-packages opentelemetry-sdk opentelemetry-exporter-prometheus

COPY metrics_exporter.py .

CMD ["python", "metrics_exporter.py"]
