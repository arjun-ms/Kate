import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit
import datetime
import wikipedia


# this instance recognises the speech
charlotte = sr.Recognizer()
# this instance is for initializing speech synthesis
engine = tts.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    # engine.say("I am charlotte, your personal assistant")
    # engine.say("What can I do for you")

def take_command():
    try:
        with sr.Microphone() as source :
            talk("Listening now")
            print("Listening...")
            voice = charlotte.listen(source)
            command = charlotte.recognize_google(voice)
            command = command.lower()
            print(command)       
            if "hello" and "charlotte" in command:
                print("What can I do for you")
                talk("What can I do for you")
                
            
    except:
        pass

    return command

def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))

def run_charlotte():
    command = take_command()
    if "play" in command:
        song = command.split(" ")[1:]
        song = listToString(song)
        # print(song)
        talk("Playing "+song)
        print("Playing "+song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print("Current time is "+time)
        talk("Current time is "+time)
    elif "who is" in command:
        person = command.replace("who is","")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "how are you" in command:
        talk("I am doing great. What about you?")

run_charlotte()