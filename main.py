import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser as wb

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alex' in command:
                command = command.replace('alex', '')
                print(command)
    except:
        pass
    return command
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon!")

    else:
        talk("Good Evening!")

if __name__ == '__main__':




    wishMe()
    print("HI I am Alex!! ...")
    print("How may I help you ")
    talk("HI I am Alex!! ...")
    talk("How may I help you ")
    while True:
       command = take_command()
       #print(command)
       if 'how are you' in command:
           print('I am fine , how are you?')
           talk('I am fine , how are you?')
       elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
       elif 'time' in command:
         time = datetime.datetime.now().strftime('%I:%M %p')
         talk('Current time is ' + time)
         print(time)
       elif 'who the heck is' in command:
         person = command.replace('who the heck is', '')
         info = wikipedia.summary(person, 1)
         print(info)
         talk(info)
       elif 'wikipedia' in command:
           talk('Searching Wikipedia...')
           command = command.replace("wikipedia", "")
           results = wikipedia.summary(command, sentences=2)
           talk("According to Wikipedia")
           print(results)
           talk(results)
       elif 'date' in command:
         talk('sorry, I have a headache')
       elif 'are you single' in command:
        print('I am in a relationship with the Wi-fi')
        talk('I am in a relationship with the Wi-fi')

       elif 'joke' in command:
         talk(pyjokes.get_joke())
       elif 'open instagram' in command:
           wb.open('https://www.instagram.com')

       elif 'open youtube' in command:
           wb.open('https://www.youtube.com')

       elif 'open google' in command:
           wb.open('https://www.google.com')

       elif 'open facebook' in command:
           wb.open('https://www.facebook.com')

       elif 'quit'  in command:
           print('Stopping...')
           talk('Thank You for being with me ')

           exit(0)
       else:
           print("Sorry I coudn't catch that")
           print('Please say the command again.')
           talk('Please say the command again.')



