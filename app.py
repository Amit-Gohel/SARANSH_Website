from flask import Flask,render_template,Response
import cv2
import keyboard
import summrizerMain

app=Flask(__name__)
camera=cv2.VideoCapture(1)
text = "Amit"
summary = "Gohel"
def generate_frames():
    while True:

        ## read the camera frame
        success,frame=camera.read()
        if keyboard.is_pressed("m"):
            cv2.imwrite("framex.jpg", frame)
            framex = "framex.jpg"
            try:
                text, summary = summrizerMain.mainFun(framex)
            except:
                pass

        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
            # print("hello")
            # if keyboard.is_pressed("m"):

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html', text=text, summary=summary)

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)

