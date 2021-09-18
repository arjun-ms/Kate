import speech_recognition as sr
import pyttsx3 as tts

# this instance recognises the speech
kate = sr.Recognizer()
# this instance is for initializing speech synthesis
engine = tts.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    # engine.say("I am Kate, your personal assistant")
    # engine.say("What can I do for you")

def take_command():
    try:
        with sr.Microphone() as source :
            talk("Listening now")
            print("Listening...")
            voice = kate.listen(source)
            command = kate.recognize_google(voice)
            command = command.lower()
            print(command)       
            if "hello" and "kate" in command:
                print("What can I do for you")
                talk("What can I do for you")
                take_command()
            
    except:
        pass

    return command

def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))

def run_kate():
    command = take_command()
    if "play" in command:
        song = command.split(" ")[1:]
        song = listToString(song)
        print(song)
        talk("Playing "+song)
        print("Playing "+song)

run_kate()