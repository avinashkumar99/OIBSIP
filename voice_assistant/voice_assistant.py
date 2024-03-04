import pyttsx3 
import speech_recognition as sr
import pyjokes
import requests
from bs4 import BeautifulSoup
import datetime

# creating engine, setting voice property and adjusting the voice rate(speed)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 120)

# speak function has been created
def assistant_speaks(text):
    engine.say(text)
    engine.runAndWait()

# listen and convert speech into text 
def listening():
    r = sr.Recognizer()
    m = sr.Microphone()
    print("Wait a moment please.")
    with m as source :
        r.adjust_for_ambient_noise(source)
        try:
            print("Now Speak")
            audio =  r.listen(source,timeout=5, phrase_time_limit=6)
        
        except Exception as e:
            message = "Unable to process!"
            print(message)
            return "none"
        
        try: 
            text = r.recognize_google(audio)
            print("Processing ...")
            print(f"User said: {text}")
        except Exception as e:
            text = "Say that again!"
        return text


# Greet function 
def greet():
    assistant_speaks("Hello! How can i help you.")

# Getting weather report of different states
def weatherReport():
    assistant_speaks("Weather for which state?")
    state = listening()
    states = [
    'Andhra Pradesh',       
    'Arunachal Pradesh',
    'Assam',
    'Bihar',
    'Chhattisgarh',
    'Delhi',
    'Goa',
    'Gujarat',
    'Haryana',
    'Himachal Pradesh',
    'Jharkhand',
    'Karnataka',
    'Kerala',
    'Madhya Pradesh',
    'Maharashtra',
    'Manipur',
    'Meghalaya',
    'Mizoram',
    'Nagaland',
    'Odisha',
    'Punjab',
    'Rajasthan',
    'Sikkim',
    'Tamil Nadu',
    'Telangana',
    'Tripura',
    'Uttar Pradesh',
    'Uttarakhand',
    'West Bengal',
    ]

    if state in states:
        # creating url and requests instance
        url = "https://www.google.com/search?q="+"weather"+state
        html = requests.get(url).content

        # getting raw data 
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

        # formatting data
        data = str.split('\n')
        time = data[0]
        sky = data[1]
         
        # getting all div tag
        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
        strd = listdiv[5].text
         
        # getting other required data
        pos = strd.find('Wind')
        other_data = strd[pos:]
         
        # printing all data
        print("Temperature is", temp)
        assistant_speaks(f"Temperature is {temp}")
        
        print("Time: ", time)
        assistant_speaks(f"Current day and time is {time}")

        print("Sky Description: ", sky)
        assistant_speaks(f"Sky is {sky}")


# Function for current date and time
def date_time(data):
    if data == 'date':
        return datetime.date.today()
    elif data == 'time':
        current_time = datetime.datetime.now()
        hours, mins = current_time.strftime("%H %M").split()
        if int(hours) > 12 :
            hour = str(int(hours) - 12)

            return f"{hour}:{mins} pm"
        else :
            return f"{hours}:{mins} am"
    elif data == 'day':
        current_time = datetime.datetime.now()
        print(current_time.strftime("%d %m %y"))
        week_day = current_time.weekday()
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        print(weekdays[week_day])
        return weekdays[week_day]

# main function which handles all conditions
def main(text):
    if 'hello' in text:
        greet()
    elif 'joke' in text:
        assistant_speaks("Sure , here is the joke for you.")
        assistant_speaks(pyjokes.get_joke('en', 'neutral'))
     
    elif 'good' in text:
        assistant_speaks(text+ "How can i help you ?")
    
    elif 'weather' in text:
        weatherReport()
    
    elif 'current date' in text :
        current_date = date_time('date')
        print(datetime.date.today())
        assistant_speaks(current_date)
    
    elif 'current time' in text:
        current_time = date_time('time')
        print(current_time)
        assistant_speaks(current_time.replace(":", " "))
    
    elif 'current day' in text:
        current_day = date_time('day')
        assistant_speaks(f"It's {current_day}.")

    elif 'you are awesome' in text or 'amazing' in text:
        assistant_speaks("Thank You! I appreciate it.")
    
    else :
        message = "Sorry! I am not able to understand."
        print(message)
        assistant_speaks(message)

# Assistant introduction
assistant_speaks("Hello, I am Alice, your virtual assistant. How can I help you?")

# Infinite interation for voice assistant
while(True):
    text = listening()
    main(text)


