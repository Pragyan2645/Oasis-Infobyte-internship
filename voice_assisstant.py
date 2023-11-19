import speech_recognition as sr
import pyaudio
import subprocess as sp
from datetime import datetime as dt


voice_recogniser = sr.Recognizer()

def voice_capture():
    with sr.Microphone() as source:
        print("listening...")
        audio = voice_recogniser.listen(source,timeout=3)
    return audio

def convert_speech_to_text(voice):
    try:
        text = voice_recogniser.recognize_google(voice)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("I didn't understand!!")
    except sr.RequestError:
        print("Request error!!")
    return text


def web_searching(query):
    try:
        from googlesearch import search
    except ImportError: 
        print("No module named 'google' found")
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        print(j)

def process_commands(commands):
    if commands == "hello":
        print("hii! How can I help you?")
    elif commands.lower() == "open chrome":
        sp.run("C:\Program Files\Google\Chrome\Application\chrome.exe",shell=True)
    elif "time" in commands.lower() or "date" in commands.lower():
        current_datetime = dt.now()
        print("Current Date and Time:",current_datetime)
    else:
        web_searching(commands)


if __name__ == "__main__":
    while True:
        _audio = voice_capture()
        _text = convert_speech_to_text(_audio)
        if "quit" in _text.lower() or "thank you" in _text.lower():
            break
        else:
            process_commands(_text)
