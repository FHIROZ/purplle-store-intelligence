from ultralytics import YOLO
import cv2
import json
from collections import defaultdict

# -----------------------------
# LOAD MODEL
# -----------------------------
model = YOLO("yolov8n.pt")

video_path = "data/videos/floor_camera_2.mp4"

cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)

# -----------------------------
# ZONES
# -----------------------------
zones = {
    "ALPS": (250, 250, 550, 950),
    "SWISS_BEAUTY": (550, 250, 850, 950),
    "LAKME": (850, 250, 1150, 950),
    "FACES_CANADA": (1150, 250, 1450, 950),
    "MAYBELLINE": (1450, 250, 1850, 950),
}

# -----------------------------
# ANALYTICS
# -----------------------------
visitor_zone = {}
visitor_frames = defaultdict(int)
zone_visits = defaultdict(set)

frame_count = 0

# -----------------------------
# MAIN LOOP
# -----------------------------
while cap.isOpened():

    success, frame = cap.read()

    if not success:
        break

    frame_count += 1

    # Process every 5th frame only
    if frame_count % 5 != 0:
        continue

    results = model.track(
        frame,
        persist=True,
        classes=[0],
        verbose=False
    )

    annotated_frame = results[0].plot()

    # -----------------------------
    # DRAW ZONES
    # -----------------------------
    for zone_name, (x1, y1, x2, y2) in zones.items():

        cv2.rectangle(
            annotated_frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            annotated_frame,
            zone_name,
            (x1 + 10, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    # -----------------------------
    # TRACK PEOPLE
    # -----------------------------
    if results[0].boxes.id is not None:

        boxes = results[0].boxes.xyxy.cpu().numpy()
        ids = results[0].boxes.id.cpu().numpy().astype(int)

        for box, track_id in zip(boxes, ids):

            x1, y1, x2, y2 = map(int, box)

            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            cv2.circle(
                annotated_frame,
                (center_x, center_y),
                5,
                (0, 0, 255),
                -1
            )

            current_zone = None

            for zone_name, (zx1, zy1, zx2, zy2) in zones.items():

                if (
                    zx1 <= center_x <= zx2 and
                    zy1 <= center_y <= zy2
                ):
                    current_zone = zone_name
                    break

            if current_zone:

                visitor_zone[track_id] = current_zone

                visitor_frames[
                    (track_id, current_zone)
                ] += 1

                zone_visits[current_zone].add(track_id)

                dwell_seconds = (
                    visitor_frames[
                        (track_id, current_zone)
                    ] / fps
                )

                cv2.putText(
                    annotated_frame,
                    f"{current_zone} {dwell_seconds:.1f}s",
                    (x1, y1 - 25),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 255),
                    2
                )

    # -----------------------------
    # LIVE DASHBOARD
    # -----------------------------
    y = 30

    for zone_name in zones.keys():

        count = len(zone_visits[zone_name])

        cv2.putText(
            annotated_frame,
            f"{zone_name}: {count}",
            (20, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        y += 30

    cv2.imshow(
        "Store Intelligence",
        annotated_frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# -----------------------------
# CLEANUP
# -----------------------------
cap.release()
cv2.destroyAllWindows()

# -----------------------------
# SUMMARY
# -----------------------------
print("\n===== ZONE VISITS =====\n")

analytics = {}

for zone_name in zones.keys():

    count = len(zone_visits[zone_name])

    print(f"{zone_name}: {count}")

for (visitor_id, zone_name), frames in visitor_frames.items():

    dwell = frames / fps

    analytics[
        f"visitor_{visitor_id}_{zone_name}"
    ] = {
        "visitor_id": int(visitor_id),
        "zone": zone_name,
        "dwell_seconds": round(dwell, 2)
    }

# -----------------------------
# SAVE JSON
# -----------------------------
import os

os.makedirs("outputs", exist_ok=True)

with open(
    "outputs/zone_analytics.json",
    "w"
) as f:

    json.dump(
        analytics,
        f,
        indent=4
    )

print("\nAnalytics saved:")
print("outputs/zone_analytics.json")