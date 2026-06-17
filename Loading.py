import cv2

image = cv2.imread("Demoo.png")

if image is None:
    print("error: not found")
else:
    print("loaded successfully")