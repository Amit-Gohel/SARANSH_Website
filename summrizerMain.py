import time
from TextToSummary import TextSummarizer
import CameraToText
import TextToVoice

def mainFun(framex):
    time.sleep(2)
    try:
        text = CameraToText.textConverter(framex)        
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

        return text, summary 

    except:
        TextToVoice.voice("An exception occurred", 'f')
        # print("An exception occurred")