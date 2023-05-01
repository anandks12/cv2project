import cv2
import glob

gimg = glob.glob("*.jpeg") + glob.glob("*.png") + glob.glob("*.jpg")
detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
for i in gimg :
    image = cv2.imread(i)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = detect.detectMultiScale(gray,1.25,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)


    cv2.imshow("Result of the detctor",image)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()