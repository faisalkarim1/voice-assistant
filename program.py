import speech_recognition as sr
from gtts import gTTS
import os

def SpeakText(command):
    tts = gTTS(text=command, lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")

r = sr.Recognizer()

while(1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("You Said "+MyText)
            SpeakText(MyText)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")