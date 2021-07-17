import cv2
import numpy as np
def blend(i):
    switcher={
        1:cv2.imread("background1.jpg"),
        2:cv2.imread("background2.jpg"),
        3:cv2.imread("background3.jpg"),
        4:cv2.imread("background4.jpg"),
        5:cv2.imread("background5.jpg"),
        6:cv2.imread("background6.jpg")
    }
    return switcher.get(i, "Invalid option")
j=int(input("Enter the number of image you want in background: 1 to 6: "))
image=blend(j)
cap=cv2.VideoCapture(0)
# print(image)
while True:
    flag,frame=cap.read()
    if not flag:
        print("Couldn't access the camera")
        break
    if(image=="Invalid option"):
        print(image)
        break
    image=cv2.resize(image, (frame.shape[1], frame.shape[0]))
    blended_frame= cv2.addWeighted(frame, 0.5, image, 0.5, 0.2)
    cv2.imshow("Blended frame", blended_frame)
    if(cv2.waitKey(10) & 0xff==ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
