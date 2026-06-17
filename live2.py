from ultralytics import YOLO
import cv2

# Load model (use a custom-trained model for crop disease/pest detection if available)
model = YOLO("yolov8n.pt")  # replace with "best.pt" for custom agriculture model

# Classes of interest (COCO ids): 0=person, others depend on custom model for crops
TARGET_CLASSES = {0: "Human"}  # extend with custom class ids e.g. {0:"Human", 1:"Crop_Healthy", 2:"Crop_Diseased", 3:"Pest"}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)
    annotated_frame = results[0].plot()

    # Custom logic for detected objects
    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        if cls_id in TARGET_CLASSES:
            label = f"{TARGET_CLASSES[cls_id]} {conf:.2f}"
            cv2.putText(annotated_frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            if TARGET_CLASSES[cls_id] == "Human":
                cv2.putText(annotated_frame, "ALERT: Human in field!", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("Agriculture Crop & Human Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()