import cv2

face_cascade =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap =cv2.VideoCapture(1)

img1 = cv2.resize(img1,(700,700))
while True:
    success, img1 = cap.read()
    imgcopy=img1
    gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    anya = cv2.imread("elon.png")

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        x=x-50
        y=y-50
        w=w+70
        h=h+70

        anya = cv2.resize(anya,(w, h))

        img1[y:y+h,x:x+w]=anya[0:h,0:w]
    cv2.imshow("insan", img1)
    cv2.imshow("e", imgcopy)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
