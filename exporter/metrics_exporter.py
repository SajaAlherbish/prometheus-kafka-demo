from prometheus_client import start_http_server, Gauge
import time
import random

# Create Prometheus metrics
avg_in = Gauge("avgThroughputIn", "Average throughput in")
avg_out = Gauge("avgThroughputOut", "Average throughput out")
last_in = Gauge("lastThroughputIn", "Last throughput in")
last_out = Gauge("lastThroughputOut", "Last throughput out")
max_in = Gauge("maxThroughputIn", "Max throughput in")
max_out = Gauge("maxThroughputOut", "Max throughput out")
total_in = Gauge("totalBytesIn", "Total bytes in")
total_out = Gauge("totalBytesOut", "Total bytes out")
total_conns = Gauge("totalConnections", "Total connections")
max_conns = Gauge("maxTotalConnections", "Max total connections")

connections_file = Gauge("connections_file", "Connections file")
connections_hlsv3 = Gauge("connections_hlsv3", "Connections hlsv3")
connections_llhls = Gauge("connections_llhls", "Connections llhls")
connections_ovt = Gauge("connections_ovt", "Connections ovt")
connections_push = Gauge("connections_push", "Connections push")
connections_srt = Gauge("connections_srt", "Connections srt")
connections_thumbnail = Gauge("connections_thumbnail", "Connections thumbnail")
connections_webrtc = Gauge("connections_webrtc", "Connections webrtc")

def set_mock_data():
    # Set static/mock data here
    avg_in.set(14576272)
    avg_out.set(0)
    last_in.set(1822034)
    last_out.set(0)
    max_in.set(39001208)
    max_out.set(38818856)
    total_in.set(72597103866)
    total_out.set(30761366477)
    total_conns.set(0)
    max_conns.set(1)

    connections_file.set(0)
    connections_hlsv3.set(0)
    connections_llhls.set(0)
    connections_ovt.set(0)
    connections_push.set(0)
    connections_srt.set(0)
    connections_thumbnail.set(0)
    connections_webrtc.set(0)

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        set_mock_data()
        time.sleep(10)