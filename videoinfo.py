import cv2

video = cv2.VideoCapture("Umar.MP4")

width= int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
frames=int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps= int(video.get(cv2.CAP_PROP_FPS))

print(width,height,frames,fps)