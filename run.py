import speech_recognition as sr
import pyaudio
import pywhatkit
from gtts import gTTS
from playsound import playsound


def speech(a):
    print(a)
    language = "en"
    output = gTTS(text=a, lang=language, tld='co.uk', slow=False)

    output.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")


def get_audio():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something....")
        audio = recorder.listen(source)

        say = recorder.recognize_google(audio, language='en-IN')
        print("I thinks you said '" + recorder.recognize_google(audio) + "'")
        return say


text = get_audio()

if "youtube" in text.lower():
    speech("Okay, I will bring that up for you on youtube")
    pywhatkit.playonyt(text)
elif "joke" in text.lower():
    speech("no joke for you")
else:
    pywhatkit.search(text)
