from pymongo import MongoClient
import json

# -----------------------------------
# CONNECT TO MONGODB
# -----------------------------------

client = MongoClient("mongodb://localhost:27017/")

db = client["store_intelligence"]

events_collection = db["events"]
anomalies_collection = db["anomalies"]

# -----------------------------------
# CLEAR OLD DATA
# -----------------------------------

events_collection.delete_many({})
anomalies_collection.delete_many({})

# -----------------------------------
# LOAD EVENTS
# -----------------------------------

with open("outputs/events.json", "r") as f:
    events = json.load(f)

if events:
    events_collection.insert_many(events)

# -----------------------------------
# LOAD ANOMALIES
# -----------------------------------

with open("outputs/anomalies.json", "r") as f:
    anomalies = json.load(f)

if anomalies:
    anomalies_collection.insert_many(anomalies)

# -----------------------------------
# SUMMARY
# -----------------------------------

print("\n===== MONGODB STORAGE =====\n")

print(
    f"Events Stored: "
    f"{events_collection.count_documents({})}"
)

print(
    f"Anomalies Stored: "
    f"{anomalies_collection.count_documents({})}"
)

print("\nMongoDB Integration Successful")