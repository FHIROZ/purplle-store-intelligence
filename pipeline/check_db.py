from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["store_intelligence"]

print("Events:", db.events.count_documents({}))
print("Anomalies:", db.anomalies.count_documents({}))