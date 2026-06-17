import cv2

video = cv2.VideoCapture("Umar.MP4")

if not video.isOpened():
    print("ERROR: Could not open video!")
else:
    width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps    = int(video.get(cv2.CAP_PROP_FPS))

    print(f"Width: {width}")
    print(f"Height: {height}")
    print(f"Frames: {frames}")
    print(f"FPS: {fps}")

video.release()
