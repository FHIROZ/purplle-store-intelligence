import json
import os

ANOMALY_THRESHOLD = 5.0

with open(
    "outputs/zone_analytics.json",
    "r"
) as f:
    analytics = json.load(f)

anomalies = []

for key, data in analytics.items():

    if data["dwell_seconds"] > ANOMALY_THRESHOLD:

        anomalies.append({
            "visitor_id": data["visitor_id"],
            "zone": data["zone"],
            "event_type": "ANOMALY",
            "reason": "High Dwell Time",
            "dwell_seconds": data["dwell_seconds"]
        })

os.makedirs("outputs", exist_ok=True)

with open(
    "outputs/anomalies.json",
    "w"
) as f:

    json.dump(
        anomalies,
        f,
        indent=4
    )

print("\n===== ANOMALIES =====\n")

for anomaly in anomalies:
    print(anomaly)

print(f"\nTotal Anomalies: {len(anomalies)}")
print("Saved: outputs/anomalies.json")