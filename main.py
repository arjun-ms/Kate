import speech_recognition as sr
import pyttsx3 as tts

# this instance recognises the speech
kate = sr.Recognizer()
# this instance is for initializing speech synthesis
engine = tts.init()

engine.say("I am Kate, your personal assistant")
engine.say("What can I do for you")
engine.runAndWait()

try:
    with sr.Microphone() as source :
        print("Listening...")
        voice = kate.listen(source)
        command = kate.recognize_google(voice).lower()
        print(command)       
        if "kate" in command:
            engine.say("What can I do for you")
            engine.runAndWait()
            print("What can I do for you")
except:
    pass

