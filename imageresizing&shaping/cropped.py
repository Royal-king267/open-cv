import cv2

image = cv2.imread("Demoo.png")

if image is not None:
    cropped = image[100:200,25:175]

    cv2.imshow("Original image",image)
    cv2.imshow("cropped",cropped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()