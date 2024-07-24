import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

PORT = 8050
IP_ADD = "127.0.0.1"
SERVER = None
BUFFER_SIZE = None

window = None
selectLabel = None
listBox = None
playButton = None
stopButton = None
uploadButton = None
downloadButton = None
infoLabel = None

def musicWindow():
    global window
    global selectLabel
    global listBox
    global playButton
    global stopButton
    global uploadButton
    global downloadButton
    global infoLabel

    window = Tk()
    window.title("Music Window")
    window.geometry("300x300")
    window.configure(bg="LightSKyBlue")
    
    selectLabel= Label (window, text="Select Song",bg='LightSkyBlue', font = ("Calibri",0)) 
    selectLabel.place (x= 2, y= 1)

    listBox= Listbox (window, height=10, width=39, activestyle = 'dotbox',bg='LightSkyBlue',borderwidth=2, font=("Calibri",10)) 
    listBox.place (x=10,y=18)

    scrollbar = Scrollbar(listBox)
    scrollbar.place (relheight= 1,relx=1)
    scrollbar.config(command = listBox.yview)

    PlayButton=Button(window, text="Play", width=10,bd=1,bg="SkyBlue", font=("Calibri",10))
    PlayButton.place(x=30,y=200)

    stopButton = Button(window, text="stop",bd=1,width=10,bg="SkyBlue", font = ("Calibri",10)) 
    stopButton.place (x=200,y=200)

    uploadButton=Button (window, text="Upload",width=10,bd=1,bg='SkyBlue', font=("Calibri",10))
    uploadButton.place (x=30,y=250)

    downloadButton =Button (window, text="Download", width=10,bd=1,bg="SkyBlue", font = ("Calibri",10)) 
    downloadButton.place (x=200,y=250)
    
    infoLabel= Label(window, text="",fg= "blue", font=("Calibri",8))
    infoLabel.place (x=4, y=280)
    
    window.mainloop()

def setup():
    global SERVER
    global IP_ADD
    global PORT

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   
    SERVER.connect((IP_ADD,PORT))

    musicWindow()



setup()




