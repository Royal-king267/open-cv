import cv2

image = cv2.imread("Demoo.png")

if image is not None:
    success = cv2.imwrite("output_demoo.png",image)
    if success:
        print("image saved successfully as 'output_demoo.png' ")
    else:
        print("failed to save an image")
   