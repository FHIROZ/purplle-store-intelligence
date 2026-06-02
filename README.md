# Purplle Store Intelligence Platform

## Overview

Purplle Store Intelligence Platform is an AI-powered retail analytics system that transforms CCTV footage into actionable business insights.

The platform detects and tracks customers inside a retail store, analyzes customer behavior across product zones, calculates dwell time, identifies anomalies, stores analytics data in MongoDB, exposes REST APIs through FastAPI, and visualizes insights through an interactive Streamlit dashboard.

---

## Key Features

### Computer Vision

* Customer Detection using YOLOv8
* Multi-Person Tracking
* Real-Time Visitor Monitoring
* Zone-Based Customer Analytics

### Analytics Engine

* Zone Visit Tracking
* Dwell Time Calculation
* Customer Movement Analysis
* Event Generation Pipeline

### Anomaly Detection

* High Dwell Time Detection
* Suspicious Customer Activity Identification
* Automated Anomaly Logging

### Data Management

* Event Storage in MongoDB
* Analytics Persistence
* Structured JSON Event Schema

### APIs

* FastAPI-based REST Services
* Swagger/OpenAPI Documentation
* Analytics Endpoints
* Event Endpoints
* Zone Analytics Endpoints
* Anomaly Endpoints
* Health Monitoring Endpoint

### Dashboard

* Interactive Streamlit Dashboard
* KPI Metrics
* Zone Analytics Visualization
* Dwell Time Insights
* Business Recommendations
* Raw Event Explorer

---

## System Architecture

```text
CCTV Video
     │
     ▼
YOLOv8 Detection
     │
     ▼
Multi-Person Tracking
     │
     ▼
Zone Analytics
     │
     ▼
Event Generation
     │
     ├── Zone Visits
     ├── Dwell Time
     └── Anomaly Detection
     │
     ▼
MongoDB Storage
     │
     ▼
FastAPI Services
     │
     ▼
Streamlit Dashboard
```

---

## Technology Stack

### AI & Computer Vision

* YOLOv8
* OpenCV
* ByteTrack

### Backend

* Python
* FastAPI

### Data Storage

* MongoDB
* JSON

### Visualization

* Streamlit
* Plotly

---

## API Endpoints

| Endpoint     | Description        |
| ------------ | ------------------ |
| `/`          | Home Endpoint      |
| `/analytics` | Analytics Summary  |
| `/events`    | Event Data         |
| `/zones`     | Zone Analytics     |
| `/anomalies` | Detected Anomalies |
| `/health`    | Health Check       |

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Dashboard Metrics

The dashboard provides:

* Total Visitors
* Total Events
* Anomaly Count
* Top Performing Zone
* Average Dwell Time
* Zone Visit Distribution
* Business Insights
* Raw Event Analytics

---

## Project Structure

```text
store-intelligence/
│
├── api/
│   └── main.py
│
├── app/
│   └── dashboard.py
│
├── pipeline/
│   ├── detect.py
│   ├── events.py
│   ├── anomaly.py
│   └── database.py
│
├── outputs/
│   ├── events.json
│   ├── anomalies.json
│   └── zone_analytics.json
│
├── docs/
│   ├── architecture.svg
│   ├── detection.jpeg
│   ├── dashboard.jpeg
│   ├── api.jpeg
│   └── mongodb.jpeg
│
├── requirements.txt
├── README.md
├── Dockerfile
└── docker-compose.yml
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Detection Pipeline

```bash
python pipeline/detect.py
```

---

## Generate Events

```bash
python pipeline/events.py
```

---

## Detect Anomalies

```bash
python pipeline/anomaly.py
```

---

## Store Analytics in MongoDB

```bash
python pipeline/database.py
```

---

## Run FastAPI Server

```bash
uvicorn api.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Run Dashboard

```bash
streamlit run app/dashboard.py
```

---

## Results

* Customer Detection and Tracking
* Zone-Based Visitor Analytics
* Dwell Time Analysis
* Automated Event Generation
* Anomaly Detection
* MongoDB Data Storage
* FastAPI REST APIs
* Interactive Dashboard

---

## Screenshots

Screenshots are available in the `docs/` directory:

* Detection Output
* Dashboard Analytics
* FastAPI Swagger Documentation
* MongoDB Integration
* System Architecture Diagram

---

## Future Enhancements

* Multi-Camera Synchronization
* Real-Time Streaming Analytics
* Cloud Deployment (AWS/Azure/GCP)
* Customer Path Analysis
* Heatmap Generation
* Product Recommendation Insights
* Real-Time WebSocket Dashboard

---

## Author

Developed as part of the Purplle Store Intelligence Challenge using Computer Vision, AI Analytics, FastAPI, MongoDB, and Streamlit.
