# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3
import time
from selenium import webdriver 
 

# Initialize the recognizer
r = sr.Recognizer()

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
            return query        
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
        
        
        
        
    
		
			
# while(1):
SpeakText("ROBO Version1.1 ")
while(1):
    print(command())

# Loop infinitely for user to
# speak

# while(1):
	
# 	# Exception handling to handle
# 	# exceptions at the runtime
# 	try:
		
# 		# use the microphone as source for input.
# 		with sr.Microphone() as source2:
# 			print("lisening.....")
# 			r.adjust_for_ambient_noise(source2, duration=0.2)
# 			audio2 = r.listen(source2,1,5)
# 			print("Recognizing......")
# 			MyText = r.recognize_google(audio2)
# 			MyText = MyText.lower()			            
# 			print("Did you say ",MyText)
# 			SpeakText(MyText)		
# 	except sr.RequestError as e:
# 		print("Could not request results; {0}".format(e))	
# 	except sr.UnknownValueError:
# 		print("unknown error occurred")

