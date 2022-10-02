from TextToSummary import TextSummarizer
import CameraToText
import TextToVoice
import cv2
from flask import Flask

app = Flask(__name__)

cap = cv2.VideoCapture(1)

@app.route('/')
def imageToVoice():
    while(cap.isOpened()):
        
        ret, frame = cap.read()
        cv2.imshow('Frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('m'):
            try:
                cv2.imwrite("framex.jpg", frame)
                # filename = "framex.jpg"
                text = CameraToText.textConverter('test.png')        
                print("-----------------text-----------------")
                print(text)
                print("--------------------------------------")
                ts = TextSummarizer()
                ts.input_text(text)
                words = ts.tokenize_sentence()
                freqTable = ts.cal_freq(words)
                sentenceValue = ts.compute_sentence(freqTable)
                avg = ts.sumAvg(sentenceValue)
                summary = ts.print_summary(sentenceValue,avg)

                print("----------------summary------------")
                print(summary)
                print("--------------------------------------")
                
                TextToVoice.voice(summary, 'f')

            except:
                print("An exception occurred")

        if cv2.waitKey(25) & 0xFF == ord('q'):
            return "hello"


if __name__ == '__main__':
	app.run()

