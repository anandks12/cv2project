import cv2
detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
while True:
    res,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=detect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),3)
    cv2.imshow("VideoFrame",img)


    if cv2.waitKey(100) and cv2.getWindowProperty('VideoFrame', cv2.WND_PROP_VISIBLE) < 1:  # exit if window closed
        break
cap.release()
cv2.destroyAllWindows()




