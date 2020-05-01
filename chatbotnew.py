import pyttsx3
import wikipedia
import datetime
import webbrowser
import os
import pyjokes
import random
import requests
import speech_recognition as sr
import time
import geocoder

# To retrieve your own IP address
g = geocoder.ip('me')

# For Voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        print("Good Afternoon!")
        speak("Good Afternoon!")

    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("What is your name ?")
    speak("What is your name ?")
    name = takeCommand().lower()
    print(f"Hello {name}, I am a chatbot. What can I do for you ? ...")
    speak(f"Hello {name}, I am a chatbot. What can I do for you ?...")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 7000
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def time_sleep(sleep=0.6):
    time.sleep(sleep)


def weather_data(query):
    res = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?' + query + '&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')
    return res.json()


def print_weather(result, city):
    print("{}'s temperature: {}°C ".format(city, result['main']['temp']))
    speak("{}'s temperature: {}°C ".format(city, result['main']['temp']))
    print("Wind speed: {} m/s".format(result['wind']['speed']))
    speak("Wind speed: {} m/s".format(result['wind']['speed']))
    print("Description: {}".format(result['weather'][0]['description']))
    speak("Description: {}".format(result['weather'][0]['description']))
    print("Weather: {}".format(result['weather'][0]['main']))
    speak("Weather: {}".format(result['weather'][0]['main']))


def weather():
    print('Which City:')
    speak('Which City:')
    city = takeCommand().lower()
    print()
    try:
        if city == 'my location' or city == 'none':
            g = geocoder.ip('me')

            query = 'q=' + g.city;
            w_data = weather_data(query);
            print_weather(w_data, g.city)
            print()
        else:
            query = 'q=' + city;
            w_data = weather_data(query);
            print_weather(w_data, city)
            print()
    except:
        print('City name not found...')
        speak("City name not found...")


def google_search(query):
    if 'search' in query:
        if 'search for' in query:
            query = query.replace("search for", "")
        else:
            query = query.replace("search", "")
        webbrowser.open("https://google.com/search?q=%s" % query)

    elif 'open' in query:
        if 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
        elif 'open maps' in query:
            webbrowser.open("https://www.google.com/maps")
        elif "open chrome" in query:
            ChromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(ChromePath)
        else:
            query = query.replace("open", "")
            webbrowser.open("https://google.com/search?q=%s" % query)


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "the time" in query or "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is : {strTime}")
            speak(f"The time is : {strTime}")
            time_sleep()

        elif "the date" in query or 'what is the date' in query or 'what date is today' in query or 'date' in query:
            print(time.strftime(" %A, %B %e, %Y"))
            speak(time.strftime(" %A, %B %e, %Y"))
            time_sleep()

        elif 'you were created in which language' in query:
            print("Python")
            speak("Python")
            time_sleep()

        elif 'open calculator' in query or 'open the calculator' in query or 'open calculator application' in query:
            CalculatorPath = "C:\\Users\\Asus\\PycharmProjects\\chatbot\\Calculator.exe"
            os.startfile(CalculatorPath)
            time_sleep(7)

        elif 'play' in query and ('music' in query or 'songs' in query or 'song' in query):
            music_dir = "D:\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            rand_msuic = random.randint(0, 8)
            os.startfile((os.path.join(music_dir, songs[rand_msuic])))
            time_sleep(5)

        elif 'wikipedia' in query:
            print('Searching Wikipedia...')
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print("According to Wikipedia")
            speak("According to Wikipedia")
            print(results)
            speak(results)
            time_sleep()

        elif "where am i" in query or "what is my current location" in query or "what is my location" in query:
            g = geocoder.ip('me')
            print("[Latitude,Longitude] = ", g.latlng)
            # print(g.postal)
            print("You are in", g.address)
            speak("You are in")
            speak(g.address)
            print("Your IP Address is: ", g.ip)
            speak("Your IP Address is: ")
            speak(g.ip)
            time_sleep()

        elif "weather" in query:
            weather()
            time_sleep()

        elif 'tell me a joke' in query or 'joke' in query:
            rand = (pyjokes.get_joke())
            print(rand)
            speak(rand)
            time_sleep()

        elif "random number" in query or 'random no.' in query:
            print("Random Number is ", random.randint(1, 9999))
            speak("Random Number is ")
            time_sleep()

        elif "bye" in query or "goodbye" in query or "stop" in query:
            print("GoodBye, Have a nice day.")
            speak("GoodBye, Have a nice day.")
            exit()

        elif 'search' in query or 'open' in query:
            google_search(query)
            time_sleep()

        elif 'thanks' in query or 'thank you' in query:
            print("You're Welcome.")
            speak("You're welcome ")
            time_sleep()
