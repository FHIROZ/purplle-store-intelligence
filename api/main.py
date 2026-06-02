from fastapi import FastAPI
import json

app = FastAPI(
    title="Purplle Store Intelligence API"
)

@app.get("/")
def home():
    return {"message": "Store Intelligence API Running"}

@app.get("/analytics")
def analytics():

    with open("outputs/zone_analytics.json") as f:
        data = json.load(f)

    return data

@app.get("/events")
def events():

    with open("outputs/events.json") as f:
        data = json.load(f)

    return data

@app.get("/zones")
def zones():

    with open("outputs/zone_analytics.json") as f:
        data = json.load(f)

    summary = {}

    for item in data.values():

        zone = item["zone"]

        summary[zone] = summary.get(zone, 0) + 1

    return summary
@app.get("/health")
def health():
    return {"status": "healthy"}
@app.get("/anomalies")
def anomalies():

    with open("outputs/anomalies.json") as f:
        data = json.load(f)

    return data


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "Purplle Store Intelligence API"
    }