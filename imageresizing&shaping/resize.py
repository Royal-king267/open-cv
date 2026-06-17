import cv2

image = cv2.imread("Demoo.png")

if image is None:
    print ("image is not found")
else:
    print ("image loaded successfully")
    #width,height
    resized = cv2.resize(image,(700,400))

    cv2.imshow("original image",image)
    cv2.imshow("resized image",resized)


    cv2.imwrite("resized_output.png",resized)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()