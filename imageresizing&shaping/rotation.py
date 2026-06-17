import cv2

image = cv2.imread("Demoo.png")

if image is None:
    print ("image is not found")
else:
    (h,w) = image.shape[:2]

    centre = (w//2,h//2)
    M = cv2.getRotationMatrix2D(centre,90,1.0)
    rotated = cv2.warpAffine(image,M,(w,h))

    cv2.imshow("Original",image)
    cv2.imshow("Rotated image by 90 degree ",rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()