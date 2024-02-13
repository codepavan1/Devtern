import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr



recognizer = sr.Recognizer()


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't get that. Can you please repeat?")
        return listen()
    except sr.RequestError as e:
        speak("Could not request results from Google Speech Recognition service; {0}".format(e))

def main():
    speak("Hello Pawan! I am your voice assistant. How can I help you?")
    while True:
        query = listen()
        if "hello" in query:
            speak("Hi there! How can I assist you today?")
        elif "time" in query:
            # Get current time
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The current time is " + current_time)
        elif "date" in query:
            # Get current date
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak("Today's date is " + current_date)
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")
        elif "open chrome" in query:
            webbrowser.open("https://www.chrome.com")
            speak("Opening Chrome")
        elif "open amazon" in query:
            webbrowser.open("https://www.amazon.com")
            speak("Opening Amazon")
        elif "open flipkart" in query:
            webbrowser.open("https://www.flipkart.com")
            speak("Opening Flipkart")
        elif "search" in query:
            speak("What do you want me to search for pawan?")
            search_query = listen()
            webbrowser.open("https://www.google.com/search?q=" + search_query)
            speak("Here are the search results for " + search_query)
        elif "open website" in query:
            speak("What website do you want me to open?")
            website = listen()
            webbrowser.open("https://" + website)
            speak("Opening " + website)

        elif "exit" in query:
            speak("Thank You, Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that.")


if __name__ == "__main__":
    main()
