import cv2
import keyboard
import CameraToText

cap = cv2.VideoCapture(2)

while(cap.isOpened()):
     
    ret, frame = cap.read()
    ret,buffer=cv2.imencode('.jpg',frame)
    frame1=buffer.tobytes()

    cv2.imwrite("framex.jpg", frame)
    framex = "framex.jpg"

    if keyboard.is_pressed("m"):
        text = CameraToText.textConverter(framex)  
        print(text)      


    cv2.imshow('Frame', frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break