import cv2

path = input("Demoo.png")
image = cv2.imread(path)
print("WHICH ACTION YOU WANT TO PERFORM : ")
print("1 SHOW   ,  2 GREY_IMAGE    ,   3 SAVE_IMAGE")
type = input("ENTER NUMERIC INTEGER INPUT : ")
if type == "1":
    if image is not None:
        cv2.imshow("image_showing" ,image)
        cv2.waitkey(0)
        cv2.destroyAllWindows() 
    else:
        print("COULD NOT LOAD THE IMAGE")
elif type == "2":
    if image is not None:
        gray=cv2.cvtColor(image , cv2.COLORBGR2GRAY)
        cv2.imshow("GRAY_IMAGE" , image)
        cv2.waitkey(0)
        cv2.destroyAllWindows()
    else:
        print("COULD NOT LOAD THE IMAGE")
elif type == "3":
    save_path = input("ENTER YOUR SAVE PATH NAME: ")
    if image is not None:
            success = cv2.write(save_path , image)
            if success:
                print("IMAGE SAVES AS",save_path)
            else:
                print("FAILED TO SAVE")
            
else:
    print("INVALID NUMERIC INTEGER INPUT")