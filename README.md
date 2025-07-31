# Prometheus → Telegraf → Kafka Pipeline

This project simulates a **metrics pipeline** where custom Python metrics are exposed to **Prometheus**, processed by **Telegraf**, forwarded into **Kafka**, and also stored in **InfluxDB** using Prometheus `remote_write`.  
With **Chronograf**, you can visualize and explore the metrics in a user-friendly UI.


## 🚀 Architecture

<img width="1180" height="462" alt="image" src="https://github.com/user-attachments/assets/d801a12f-929d-46ce-8a33-6638699612cd" />


### Flow Description

 - Python Exporter — Generates synthetic metrics and exposes them on an HTTP endpoint

 - Prometheus — Scrapes the metrics from the exporter using the config in prometheus.yml

 - Telegraf — Collects metrics from Prometheus and forwards them to Kafka

 - Kafka — Receives the metrics stream for analytics, monitoring, or logging

 - InfluxDB — Stores Prometheus metrics using the remote_write feature

 - Chronograf — Visualizes and queries metrics stored in InfluxDB
   

## 📂 Project Structure

```
prometheus-kafka/
├── docker-compose.yml         # Orchestrates all services
├── prometheus.yml             # Prometheus scraping configuration
├── telegraf.conf              # Telegraf configuration (forwarding metrics)
├── telegraf-python.Dockerfile # Custom Telegraf build
├── requirements.txt           # Root Python dependencies
└── exporter/
    ├── metrics_exporter.py    # Custom Python metrics exporter
    ├── Dockerfile             # Dockerfile for the exporter
    └── requirements.txt       # Exporter dependencies
```

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/USERNAME/prometheus-kafka-demo.git
cd prometheus-kafka-demo
```

### 2. Start the Services

```bash
docker-compose up --build -d
```

### 3. Access the Components

- **Prometheus UI** → http://localhost:9090
- **Exporter Metrics** → http://localhost:8000/metrics
- **Prometheus Targets** → Navigate to Status → Targets in the Prometheus UI
- **Chronograf UI** → http://localhost:8888

### 4. Consume Metrics from Kafka

To verify that metrics are flowing into Kafka:

```bash
# Open a shell inside the Kafka container
docker exec -it kafka /bin/bash

# Inside the Kafka container, run the consumer
kafka-console-consumer \
  --bootstrap-server localhost:9092 \
  --topic prometheus-metrics \
  --from-beginning
```

You should see metrics being streamed in real time from Prometheus → Telegraf → Kafka.

## 📊 Metrics Exposed

The exporter provides the following metrics:

### 🔹 Throughput Metrics

- `avgThroughputIn` — Average inbound throughput
- `avgThroughputOut` — Average outbound throughput
- `lastThroughputIn` — Last recorded inbound throughput
- `lastThroughputOut` — Last recorded outbound throughput
- `maxThroughputIn` — Maximum inbound throughput observed
- `maxThroughputOut` — Maximum outbound throughput observed

### 🔹 Data Counters

- `totalBytesIn` — Total bytes received
- `totalBytesOut` — Total bytes sent

### 🔹 Connection Metrics

- `totalConnections` — Current total active connections
- `maxTotalConnections` — Maximum allowed connections
- `connections_file` — File-based stream connections
- `connections_hlsv3` — HLSv3 stream connections
- `connections_llhls` — Low-latency HLS connections
- `connections_ovt` — OVT stream connections
- `connections_push` — Push protocol connections
- `connections_srt` — SRT stream connections
- `connections_thumbnail` — Thumbnail stream connections
- `connections_webrtc` — WebRTC connections
