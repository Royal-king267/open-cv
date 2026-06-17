import cv2

# Read video
cap = cv2.VideoCapture("Umar.MP4")

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create output video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(
    "output.mp4",
    fourcc,
    fps,
    (width, height)
)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Example processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # Write frame
    out.write(frame)

    # Display
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()