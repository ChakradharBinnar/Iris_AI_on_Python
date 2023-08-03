import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning chikku!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon chikku!")

    else:
        speak("Good Evening chikku!")

    speak("I am iris. Please tell me how may I help you.")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'play' in query:
            query = query.replace("play", "")
            speak('playing' + query)
            pywhatkit.playonyt(query)

        elif 'open youtube' in query:
            speak('ok. i am opening youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('ok. i am opening google')
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            speak('ok. i am opening gmail')
            webbrowser.open("gmail.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(strTime)

        elif 'hello iris' in query:
            speak("yesss.")

        elif 'what are you doing' in query:
            speak("nothing. just tocking with you.")

        elif 'how are you' in query:
            speak("i am fine. tell me how can i help you")

        else:
            speak("please repeate the command")

