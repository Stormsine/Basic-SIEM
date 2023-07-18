import time

def collect_logs():
    # Simulate log collection from various sources
    logs = [
        {"source": "Server 1", "event": "Unauthorized access attempt"},
        {"source": "Network Device 1", "event": "DDoS attack detected"},
        {"source": "Application 1", "event": "Invalid login attempt"},
        {"source": "Server 2", "event": "File integrity violation"},
    ]
    return logs

def analyze_logs(logs):
    # Simulate event correlation and analysis
    for log in logs:
        source = log["source"]
        event = log["event"]
        if "unauthorized" in event.lower():
            print(f"[ALERT] Unauthorized access detected from {source}: {event}")
        elif "ddos" in event.lower():
            print(f"[ALERT] DDoS attack detected on {source}: {event}")
        else:
            print(f"[INFO] Log received from {source}: {event}")

# Main SIEM loop
while True:
    logs = collect_logs()
    analyze_logs(logs)
    time.sleep(5)  # Wait for 5 seconds before collecting logs again
