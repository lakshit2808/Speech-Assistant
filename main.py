import random
from time import ctime # get time details
import webbrowser # open browser
import ssl
import certifi
import time
import os # to remove created audio files
from PIL import Image
import subprocess
import pyautogui #screenshot
import pyttsx3
import bs4 as bs
import urllib.request
import requests
import wikipedia
import psutil
from instaloader import Instaloader, Profile
import pyjokes
import easyimap as e
from send_email import sendEmail
import sys
from paths import *
from speak_reco import *
from day_wishing import day

class person:
    name = ''
    def setName(self, name):
        self.name = name



def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def respond(voice_data):
    # 1: greeting
    if there_exists(['hey','hi','hello']):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        reglin_speak(greet)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):

        if person_obj.name:
            reglin_speak(f"My name is Reglin, {person_obj.name}") #gets users name from voice input
        else:
            reglin_speak(f"My name is Reglin. what's your name?") #incase you haven't provided your name.

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        reglin_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name) # remember name in person object
    
    if there_exists(["what is my name"]):
        reglin_speak("Your name must be " + person_obj.name)

    # greeting
    if there_exists(["how are you","how are you doing"]):
        reglin_speak("I'm very well, thanks for asking " + person_obj.name)


    if there_exists(['Okay', 'thankyou', 'thanks' ,'ok']):
        reglin_speak('Is there anything else I can do for you?')


    if there_exists(["spelling of"]):
        x = voice_data.split()[-1].upper()
        y = voice_data.split()[-1]
        z = []
        for i in x:
            z += i
        reglin_speak(f"Spelling for {y} is {z}")


    # time
    if there_exists(["what's the time","tell me the time","what time is it","what is the time"]):
        timez = ctime()[11:20]
        reglin_speak("The time is " + timez)


    #search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        reglin_speak("Here is what I found for" + search_term + "on google")
    
    if there_exists(["search"]) and 'youtube' not in voice_data:
        search_term = voice_data.replace("search","")
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        reglin_speak("Here is what I found for" + search_term + "on google")

    #search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        search_term = search_term.replace("on youtube","").replace("search","")
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        reglin_speak("Here is what I found for " + search_term + "on youtube")

     #get stock price
    if there_exists(["price of" , 'stock']):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        reglin_speak("Here is what I found for " + search_term + " on google")
    
    # logout
    if there_exists(['logout' , 'log out']):
        reglin_speak('Do you want to logout from the device?')
        ans = record_audio()
        if 'yes' in ans:
            try:
                reglin_speak("Okay, GoodBye...")
                shut = os.system('shutdown /l')
            except Exception:
                reglin_speak("Sorry, I can't logout of your device now, please try it again.")
        else:
            reglin_speak("Okay, So what else can I do for you?")





     #weather
    if there_exists(["weather" , 'temperature']):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        reglin_speak("Here is what I found for on google")
     

     #stone paper scisorrs
    if there_exists(["game" , "Let's play a game","Stone paper scissor"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves=["rock", "paper", "scissor"]
    
        cmove=random.choice(moves)
        pmove=voice_data
        

        reglin_speak("I choose " + cmove)
        reglin_speak("You choose " + pmove)
        #reglin_speak("hi")
        if pmove==cmove:
            reglin_speak("the match is draw")
        elif pmove== "rock" and cmove== "scissor":
            reglin_speak("You Won, Congratulation")
        elif pmove== "rock" and cmove== "paper":
            reglin_speak("I Won")
        elif pmove== "paper" and cmove== "rock":
            reglin_speak("You Won, Congratulation")
        elif pmove== "paper" and cmove== "scissor":
            reglin_speak("I Won")
        elif pmove== "scissor" and cmove== "paper":
            reglin_speak("You Won, Congratulation")
        elif pmove== "scissor" and cmove== "rock":
            reglin_speak("I Won")

     #toss a coin
    if there_exists(["toss","flip","coin"]):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        reglin_speak("I choose " + cmove)

     #calc
    if there_exists(["plus","minus","multiply", "into","divide" ,"power of","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            reglin_speak(float(voice_data.split()[0]) + float(voice_data.split()[2]))
        elif opr == '-':
            reglin_speak(float(voice_data.split()[0]) - float(voice_data.split()[2]))
        elif opr == 'multiply' or 'x':
            reglin_speak(float(voice_data.split()[0]) * float(voice_data.split()[2]))
        elif opr == 'divide':
            reglin_speak(float(voice_data.split()[0]) / float(voice_data.split()[2]))
        elif opr == 'power of':
            reglin_speak(float(voice_data.split()[0]) ** float(voice_data.split()[2]))
        else:
            reglin_speak("Wrong Operator")
        


    #Wikipedia Summary
    elif 'wikipedia' in voice_data:
        wiki = record_audio('What do you want to search for?')
        summary = wikipedia.summary(wiki)
        if summary in voice_data:
            reglin_speech("According to Wikipedia " + summary)
            print(summary)
        else:
            reglin_speak("I'm sorry I can't find anything for " + summary + "Please try web search")
    
    #exit


    # screenshot
    if there_exists(['screenshot', 'screenshots']):
        x = 1
        reglin_speak("How many screenshots you want to take?")
        try:
            ans = int(record_audio())  
        except Exception:
            reglin_speak("Sorry you have given wrong input please try again.")
            exit()  
        reglin_speak("Okay, So You will get 5 seconds to take each screenshot.")
        while x <= ans:
            time.sleep(5)
            pyautogui.screenshot(SS_Location() +'screenshot' + str(x) +'.png' )
            reglin_speak("Screenshot number " + str(x) + " has been taken") 
            x+=1
        reglin_speak("Okay, your all screenshots has been taken. Is there anything else I can do for you?")          

    # Current location
    if there_exists(["where am i" , "What's my current location" , "what is my current location"]):
        Ip_info = requests.get('https://api.ipdata.co?api-key=test').json()
        loc = Ip_info['region']
        reglin_speak(f"You must be somewhere in {loc}")    

        reglin_speak("Do you want me to show it on map?")
        answer = record_audio()
        if 'yes' in answer:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            reglin_speak("You must be somewhere near here, as per Google maps")
        else:
            reglin_speak("Okay, Do you need any other help?")
            ans = record_audio()
            if 'yes' in ans:
                reglin_speak('How can I help you?')
            else:
                reglin_speak("Okay, Cool")
                exit()

    #Any Location
    if 'where is' in voice_data:
        location = voice_data.split("is")[-1]
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url) # to search for the term in browser
        reglin_speak('Here is the location of ' + location) 

    #Open application 
    if 'application' in voice_data:
        open_file = record_audio('Which Application you want to Open?')
        app = open_file
        try:
            os.startfile(app)
            reglin_speak('Here is what I found')
        except Exception:
            reglin_speak("Sorry, There is no application with this name.")

    # Send Email
    if 'send email' in voice_data:
        try:
            reglin_speak("What should be the subject of this email?")
            subject = record_audio()
            reglin_speak("What should I Say?")
            content = record_audio()
            reglin_speak("Please Enter Reciever's Email Address")
            to = sys.stdin.readline()
            msg = f'Subject: {subject}\n\n{content}'
            sendEmail(to , msg)
            reglin_speak("Your Email has been sent!")

        except Exception:
            reglin_speak("Sorry, due to some issues I was unable to send the Email, Please try again.") 
            exit()
    # Read Email
    if "read email" in voice_data:
        reglin_speak("Okay, just give me a second.")
        passwd = '8930305010'
        user = 'kanwalakshit@gmail.com'
        server = e.connect("imap.gmail.com" , user, passwd)
        server.listids()
        email = server.mail(server.listids()[0])
        reglin_speak("Subject of the latest email is: " + email.title)
        reglin_speak("It was sent by, " + email.from_addr)
        reglin_speak("Do you want to read the message?")
        ans = record_audio()
        if 'yes' in ans:
            reglin_speak("And the Body of the email is: " + email.body) 
        else:
            reglin_speak("Okay, Is there anything Else I can do for you?")



    # Device ShutDowm
    if "shutdown" in voice_data:
        reglin_speak('Do you want to shutdown the device?')
        ans = record_audio()
        if 'yes' in ans:
            reglin_speak("After how much time you want it to shutdown? Say immediately if you want to turn off now. Or say, after 10 seconds if you want to turn off after 10 seconds.")
            anz = record_audio()
            if anz == 'immediately':
                shut = os.system('shutdown /s /t 0')
            else:
                try:
                    seconds = anz.split()[-2]
                    shut = 'shutdown /s /t ' + seconds
                    shutdown = os.system(shut)
                except Exception:
                    reglin_speak("Sorry, I can't turnoff your device now, please try it again.")
        else:
            reglin_speak("Okay, So what else can I do for you?")

    # restart
    if "restart" in voice_data:
        reglin_speak('Do you want to restart the device?')
        ans = record_audio()
        if 'yes' in ans:
            try:
                reglin_speak("Okay, GoodBye...")
                shut = os.system('shutdown /r')
            except Exception:
                reglin_speak("Sorry, I can't Restart your device now, please try it again.")
        else:
            reglin_speak("Okay, So what else can I do for you?")


    # Instagram   
    if there_exists(["instagram" ,"How many following" ,"How many follower" , "followers" , "followers" ,"on instagram" , "How many followers you have on instagram","How many follower you have on instagram" ,"How many followers" , "insta" , "on insta"]):
        loader = Instaloader()
        #reglin_speak("Please Enter your username.")
        userz = "xneuropy"
        profile = Profile.from_username(loader.context, userz)

        num_followers = str(profile.followers)
        reglin_speak("Okay, You have " + num_followers + " Followers on instagram.")
        reglin_speak("Do you wanna know about your Following?")
        ans = record_audio()
        if 'yes' in ans:
            num_following = str(profile.followees)
            reglin_speak("You have " + num_following + " Following on instagram.")
        else:
            reglin_speak("Okay fine, Is there anything else I can do for you?")


    # Battery
    if "battery" in voice_data:
        battery = psutil.sensors_battery()
        persent = str(battery.percent)
        plugged = battery.power_plugged
        plugged = "and your charger is plugged in." if plugged else "and your charger is not plugged in."
        reglin_speak("Your Device is " + persent + "%" + " charged, " + plugged)    

    # Joke
    if there_exists(["tell me a joke" , "joke" , "jokes" , "make me laugh"]):
        jokzz = pyjokes.get_joke()
        reglin_speak(jokzz)
        reglin_speak("Do you want another one?")
        ans = record_audio()
        if 'yes' not in ans:
            jok = pyjokes.get_joke()
            reglin_speak(jok)
        else:
            reglin_speak("Okay, What else can I do for you?")

    
    # Notes taking
    if there_exists(['note' , 'notes']) :
        Folder = Folder_Location()
        reglin_speak("Do you want to take notes in existing note. Or want to create a new note?")
        ans = record_audio()
        def listdir(dir):
            fileName = os.listdir(dir)
            return fileName
        files = listdir(Folder)

        if 'existing' in ans:
            reglin_speak("What's the file name?")
            x = record_audio()
            name = x + ".txt"
            if name in files:
                path = 'Notes/' + name
                filez = open(path, 'a')
                note = record_audio("What Should I type: ")
                filez.write("\n" + note)
                filez.close()
                reglin_speak("Your notes are successfully created.")
                reglin_speak("Do you want to Open this note?")
                ans = record_audio()
                if 'yes' in ans:
                    filepath = Folder_Location() + name
                    os.startfile(filepath)
                    reglin_speak("Here are your notes")
                    exit()

            else:
                reglin_speak("Sorry, there is no note with this name. Please create a new one.")
                exit()

        if 'new' in ans:
            reglin_speak("What should be the note name?") 
            x = record_audio()
            name = x + ".txt"

            if name not in files:
                path = 'Notes/' + name
                filez = open(path, 'w')
                note = record_audio("What Should I type: ")
                filez.write(note)
                filez.close()
                reglin_speak("Your notes are successfuly created.")
                reglin_speak("Do you want to Open these notes?")
                ans = record_audio()
                if 'yes' in ans:
                    filepath = Folder_Location() + name
                    os.startfile(filepath)
                    reglin_speak("Here are your notes")
                    exit()
                else:
                    reglin_speak("Okay, fine")
                    exit()
            else:
                reglin_speak("Sorry This File Already Exists")
                
    annzzz = ['bye' , "exit" , "quit" , "nothing", "goodbye" ,'no']
    if there_exists(annzzz) :
        reglin_speak('Okay bye, see you again.')
        exit()

time.sleep(1)

person_obj = person()
person_obj.name = ""
engine = pyttsx3.init()



reglin_speak('Initializing Reglin')
reglin_speak(str(day()) +" " + str(user()) + ' How can I Help you?')



while(1):
    voice_data = record_audio("Listening...") # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data) # respond


