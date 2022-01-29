#pyinstaller ./Arrow-Bot.py --onefile --noconsole --add-binary "./images/mic.png;./images" --add-binary "./images/enter.png;./images" --add-binary "./images/arrow.png;./images" --add-binary "./images/logo.png;./images" --add-binary "./images/Notes.txt;./images --icon=images/logo1.ico"   
import pyttsx3 
import speech_recognition as sr     
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pywhatkit
import math
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import threading
import random
import sys

q=''
chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'
webbrowser.get(chrome_path)
engine = pyttsx3.init('sapi5')
engine.setProperty('rate',210)
voices = engine.getProperty('voices')
voiceid=0
voice='male'
engine.setProperty('voice', voices[voiceid].id)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

def speak(audio):
    print(audio)
    ai.configure(text=audio)
    engine.say(audio)
    engine.runAndWait()

def callback(input):
    global q
    q=''
    if len(input):     
        q=input
        button.configure(image=ph2)
        return True
    else:
        q=""
        button.configure(image=ph)
        return True

def RegisterCall():
    reg = root.register(callback)
    entry.config(validate ="key", 
         validatecommand =(reg, '%P'))


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Arrow Sir. Please tell me how may I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        ai.configure(text="Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        ai.configure(text="Listening...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return 'None'
    
    return query.lower()

class calculate:
    def __init__(self,str):
        self.str=str
        li=[]
        for i in str:
            try:
                li.append(int(i))
            except ValueError:
                continue
        try:
            self.a,self.b=li[0],li[1]
        except:
            pass
    def gcd(self):
        speak(math.gcd(self.a,self.b))
    
    def lcm(self):
        speak(math.lcm(self.a,self.b))
        
    def root(self):
        speak("{:.3f}".format(self.b**(1/self.a)))
    
    def power(self):
        speak(self.a**self.b)
    
    def add(self):    
        speak(self.a+self.b)
    
    def sub(self):
        speak(self.a-self.b)
    
    def mul(self):
        speak(self.a*self.b)
    
    def div(self):
        speak("{:.2f}".format(self.a/self.b))
    
    def mod(self):
        speak("{:.2f}".format(self.a % self.b))

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('goelbhavya2007@gmail.com', 'bhavyagoel2007')
    server.sendmail('goelbhavya2007@gmail.com', to, content)
    server.close()

class notes:
    def __init__(self):
        self.notePath=resource_path("images/Notes.txt")
        self.file=open(self.notePath,'r')
        self.count=0
        Content = self.file.read()
        CoList = Content.split("\n")
        for i in CoList:
            if i:
                self.count += 1
        self.file.close()
        
    def append(self,note):
        self.file=open(self.notePath,'a')
        n=self.count+1
        self.file.write(f'Note {n}: {note}')
        self.file.write('\n')
        self.file.close()
        
    def readlines(self):
        self.file=open(self.notePath,'r')
        lines=self.file.readlines()
        self.file.close()
        for line in lines:
            speak(line.strip())
        
    
    def readAline(self):
        self.file=open(self.notePath,'r')
        lines=self.file.readlines()
        line=lines[-1]
        speak(line)
        self.file.close()
        
def appendnote():
    note=ans
    try:
        notes().append(note)
        speak('Note added successfully')
    except Exception as e:
        print(e)
        speak('Failed to add note') 

def playvid():
    vid=ans
    speak(f"Playing {vid} on YouTube")
    pywhatkit.playonyt(vid)
 
def searchstack():
    search=ans.replace(" ", "+")
    os.system(f"start \"\" https://stackoverflow.com/search?q={search}&sort=relevance")

def searchgoogle():
    search=ans.replace(' ','+')
    os.system(f"start \"\" https://www.google.com/search?q={search}")

def searchstr(str,operations):
    try:
        operations[str.upper()]()
    except:
        return 'unable to calculate this operation'

def sendmail():
    try:
        content = ans
        to = "bhavyagoel2july@gmail.com"    
        sendEmail(to, content)
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry,I am not able to send this email") 

def getq(func):
    global ans
    ans=' '
    if len(entry.get()):
        ans=entry.get()
    else:
        ans=takeCommand()
    user.configure(text=ans)
    func()
    button.configure(command=ChangeText)
    entry.delete(0,'end')
    

#while True:
def main(query):
    query=query.replace(' arrow','')
    #query = takeCommand()
    find=calculate(query)
    operations={'ADD':find.add,'+':find.add,'PLUS':find.add,'SUM':find.add,'ADDITION':find.add,
        '-':find.sub,'SUB':find.sub,'SUBTRACT':find.sub, 'MINUS':find.sub,
        'DIFFERENCE':find.sub,'LCM':find.lcm,'LOWESTCOMMONFACTOR':find.lcm,
        'HCF':find.gcd,'HIGHESTCOMMONFACTOR':find.gcd,'x':find.mul,'into':find.mul,
        'PRODUCT':find.mul, 'MULTIPLY':find.mul,'MULTIPLICATION':find.mul,
        '/':find.div,'DIVISION':find.div,'DIVIDED':find.div,'MOD':find.mod,'REMAINDER'
        :find.mod,'MODULAS':find.mod,'ROOT':find.root}
    for word in query.split(' '):
        if word.upper() in operations.keys():               
            searchstr(word.upper(),operations)
            return
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        try:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        except:
            speak("I could not find any valid wikipedia articles")

    elif 'open' in query and 'youtube' in query:
        os.system("start \"\" http://youtube.com")

    elif 'play' in query or 'youtube' in query:
        speak('What should i play')
        button.configure(command=lambda: getq(playvid))
        

    elif 'open' in query and 'google' in query:
        os.system("start \"\" http://google.com")

    elif 'open' in query and 'stackoverlow' in query in query:
        os.system("start \"\" http://stackoverflow.com")   

    elif 'search' in query and 'stackoverflow' in query:
        speak('What should i search on stackoverflow?')
        button.configure(command= lambda: getq(searchstack))
           
    elif 'search' in query and 'google' in query:
        speak('What should i search on google?')
        button.configure(command= lambda: getq(searchgoogle))

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%I:%M:%S")    
        print(strTime)
        speak(f"Sir, the time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\\Users\\bhavy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'email' in query and 'self' in query:
        speak("What should I say?")
        button.configure(command= lambda: getq(sendmail))
            
    elif ('open note' in query or 'read note' in query or 'check note' in query):
        notes().readlines()

    elif ('open latest note' in query or 'read latest note' in query or 'check latest note' in query or 'open recent note' in query or 'read recent note' in query or 'check recent note' in query):
        notes().readAline()

    elif ('add a note'in query or 'make a note' in query or 'write a note' in query):
        speak('What note shall I make?')
        button.configure(command= lambda: getq(appendnote))
        
    elif query=='hello' or query=='hi' or query=='hey':
        Time = datetime.datetime.now()
        hellos=['hello','hey','hi']
        hello=random.choice(hellos)
        if Time.hour>4 and Time.hour<12:
            g="good morning"
        elif Time.hour>12 and Time.hour<17:
            g="good afternoon"
        else:
            g="good evening"
        speak(f'{hello} sir, {g} to you')
    
    elif 'end' in query:
        #break
        speak('OK')

    elif 'change' in query and 'voice' in query:
        global voiceid
        if voiceid==1:
            voiceid=0
            voice='male'
        else:
            voiceid=1
            voice='female'
        engine.setProperty('voice', voices[voiceid].id)
        speak(f'voice changed to {voice}')     
        
    elif 'full form' in query or 'stands for' in query:
        speak("ARROW stands for 'A Rather Resiliant Other Worldy-intelligence', and accuracy too")   
    
    else:
        speak('Sorry, I did not get that')


    
    
def ChangeText():
    user.place(x=5,y=110)
    ai.place(x=45,y=195)
    if len(q):
        user.configure(text=q)
        main(q)
    else:
        '''ai.configure(text="Listening...") 
        user.configure(text="...")''' 
        query=takeCommand()
        user.configure(text=query)
        main(query)
    entry.delete(0,'end')
    #x.join()
    
        
BackgroundColor="#004B49"
SecondColor="#27d27e"
Gray="#B2BEB5"
   
root=Tk()
root.geometry('350x310')
root.title("--ARROW->")
root.configure(background=BackgroundColor)
root.configure(borderwidth="1")
root.configure(relief="sunken")
root.configure(highlightbackground="white")
root.configure(highlightcolor="white")

photoPath=resource_path("images/logo.png")
p1 = PhotoImage(file = photoPath)
root.iconphoto(False, p1)

photoPath1=resource_path("images/mic.png")
im=Image.open(photoPath1)
im = im.resize((30, 30))
ph=ImageTk.PhotoImage(im)

photoPath2=resource_path("images/enter.png")
im2 = Image.open(photoPath2)
im2=im2.resize((30, 30))
ph2 = ImageTk.PhotoImage(im2)

photoPath3=resource_path("images/arrow.png")
im3=Image.open(photoPath3)
im3=im3.resize((320,70))
ph3=ImageTk.PhotoImage(im3)

style = ttk.Style()
style.configure('TEntry', foreground = BackgroundColor)

Heading=Label(root,image=ph3,background=BackgroundColor)
Heading.place(x=10,y=10)

entry=ttk.Entry(root,background=Gray,font = ('courier', 12, 'bold'),width=30)
entry.place(x=5,y=280)

user=Label(root,text="...",font="garamand 12 bold",background=Gray,wraplength=300,justify="left")
#user.place(x=5,y=110)

ai=Label(root,text="...",font="garamand 12 bold",background=SecondColor,wraplength=300,justify="right")
#ai.place(x=45,y=195)
button=Button(root,image=ph,background=SecondColor,borderwidth=0,relief="raised",command=ChangeText)
button.place(x=315,y=275)
RegisterCall()
root.mainloop()
