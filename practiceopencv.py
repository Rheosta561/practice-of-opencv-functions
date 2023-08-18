import cv2 as cv

def imreader():# creating functions for ease of flow
    loc=input("enter the location of your file or the name if this program is in the same folder ")# an approach to get user input for accessing the code.
    pic=cv.imread(loc)
    cv.imshow("output",pic)
    cv.waitKey(0)
    print("image is displayed , if you do not find out on your screen see the taskbar")
def vidreader():
    y=input("enter the location of your video")
    cap=cv.VideoCapture(y)
    while True:
        success , img=cap.read()
        cv.imshow("image",img)
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
def camreader():
    cap=cv.VideoCapture(0)
    cap.set(3,1280) # setting the width
    cap.set(4,720) # setting the height 
    while True:
        success , img=cap.read()
        cv.imshow("video",img)
        if cv.waitKey(1) & 0xFF==ord('q'): # press q to quit the webcam display
            break

print("opencv module imported successfully ") #importing module

while True:
    print("Enter your choice \n")
    print("1.reading an image \n")
    print("2.reading a video \n")
    print("3.Accessing the cams(webcam)")
    x=int(input("enter your desicion : \t "))
    if x==1:
        imreader()
        choice=input("do you wanna continue , y/n")
        if choice.upper()=="Y":
            continue
        else:
            break
    if x==2:
        vidreader()
        choice=input("do you wanna continue , y/n")
        if choice.upper()=="Y":
            continue
        else:
            break
    if x==3:
        camreader()
        choice=input("do you wanna continue , y/n")
        if choice.upper()=="Y":
            continue
        else:
            break

        



        
