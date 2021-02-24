import speech_recognition
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = speech_recognition.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_request():
    request = ""
    try:
        with speech_recognition.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            request = listener.recognize_google(voice)
            request = request.lower()
            if 'musa' in request:
                request = request.replace('musa', '')
                print(request)
    except:
        pass
    if request == "":
        take_request()
    return request


def run_musa():
    instruction = take_request()
    print(instruction)
    if 'play' in instruction:
        song = instruction.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in instruction:
        person = instruction.replace('who is', '')
        information = wikipedia.summary(person, 1)
        print(information)
        talk(information)
    elif 'joke' in instruction:
        talk(pyjokes.get_joke())
    elif 'stop' in instruction:
        talk("ok, bye ")
        exit()
    else:
        talk('Please say the command again.')


while True:
    run_musa()