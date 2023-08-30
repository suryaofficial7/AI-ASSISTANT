# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3
import time
from selenium import webdriver 
from datetime import datetime



# Initialize the recognizer
# r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
	



def command():
    try:
        r= sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=0.2)
            SpeakText("Lisening....")
            print("Lisening")
            audio = r.listen(source,1,3)
            print("Recognizing....")
            query = r.recognize_google(audio,language="en-in")
            print(f"you said :{query}")
            SpeakText(query)
            query = query.lower()
            return query       
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        command()
    except sr.UnknownValueError:
        print("unknown error occurred")
        command()
        
        
        
        
def what_is_time():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time) 
    SpeakText(current_time)
    return "done"
    
     
def openyt():
    driver = webdriver.Chrome()
    SpeakText("openning youtube")
    driver.get("https://youtube.com")
    SpeakText("opened successfully")
    i = input("waiting :. . . . . ")
def openWiki():
    driver = webdriver.Chrome()
    SpeakText("openning youtube")
    driver.get("https://wikipedia.com")
    SpeakText("opened successfully")
    i = input("waiting :. . . . . ")    

        
def wiki():
    pass    
   
def nothing():
    pass	

def note():
    pass	
def close():
    SpeakText("byeee byeeee")
def lang_info():
    SpeakText("i know Tamil, English ,Kannada, Malyalam, Hindi etc")		
# while(1):
# SpeakText("Version1.1 ")
l = [
    ["open youtube",openyt],
    ["open notepad",note],
    ["shutdown",close],
    ["stop",close],
    ["what is the time",what_is_time],
    ["which language do you know",lang_info],
    ["who are you","Surya's A I"],
    ["open wikipwdia",openWiki],
    ["wiki",wiki],
    
    
    ["last","nothing"],
    ]


def m():
    while(1):
        o = command()
        
        print(o)
        for i in l:           
            if i[0] in o:
                print("it is present")
                if i[0] == o:
                    try:
                        SpeakText(i[1])
                        print(i[1]())
                    except:
                        print("exception . . . . . .")
                    finally:
                        print(i[1])
                elif "wiki" in o:
                    print("wiki....")
                    search = "who is the kinf of arebia"
                    SpeakText("search")
                                      
                
                else:
                    SpeakText("say properly, or no command")
                break
            elif i[0] =="last":
                SpeakText('no Command found')
                break
            
                

m()

