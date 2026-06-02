import json
import os

os.makedirs("outputs", exist_ok=True)

with open(
    "outputs/zone_analytics.json",
    "r"
) as f:
    analytics = json.load(f)

events = []

for _, data in analytics.items():

    events.append({
        "visitor_id": data["visitor_id"],
        "zone": data["zone"],
        "event": "ZONE_VISIT",
        "dwell_seconds": data["dwell_seconds"]
    })

with open(
    "outputs/events.json",
    "w"
) as f:
    json.dump(events, f, indent=4)

print("events.json created")