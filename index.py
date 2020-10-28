from tkinter import ttk
from tkinter import *
from gtts import gTTS
from playsound import playsound
import os
from os import remove
import speech_recognition as sr

class inicio:
    def __init__(self,ventana):
        self.ven = ventana
        self.ven.iconbitmap('icon.ico')
        self.ven.geometry("1280x720+350+150")
        self.ven.resizable(False, False)
        self.ven.title("Texto a Audio")

        #Entry de texto a audio
        self.txt = Entry(self.ven, width=40, font=("Console", 30), background="#FF4D00")
        self.txt.place(x=200, y=50)
        self.lbl = Label(self.ven, text="No hay ningun archivo que borrar", font=("Console", 30))

        #Button de texto a audio
        self.btnreproducir = Button(self.ven, text="Reproducir", font=("Console", 30), background="#FF4D00", command=self.textoavoz)
        self.btnreproducir.place(x=855, y=250)
        self.btnborrar = Button(self.ven, text="Borrar", font=("Console", 30), background="#FF4D00", command=self.borrar)
        self.btnborrar.place(x=210, y=250)
        self.btnpegar = Button(self.ven, text="Pegar", font=("Console", 30), background="#FF4D00", command=self.segunda)
        self.btnpegar.place(x=210, y=400)
        self.btnsegunda = Button(self.ven, text="Voz a Texto", font=("Console", 30), background="#FF4D00", command=self.segunda)
        self.btnsegunda.place(x=855,y=400)
    
    def textoavoz(self):
        
        self.lbl.place_forget()
        gta = gTTS(self.txt.get(), lang="es-us")
        if os.path.isfile("prueba.mp3"):
        
            remove("prueba.mp3")
        if os.path.isfile("prueba.mp3")==False:
            gta.save("prueba.mp3")
            playsound("prueba.mp3")
        else:
            gta.save("prueba.mp3")
            playsound("prueba.mp3")
    
    def borrar(self):
        
        if os.path.isfile("prueba.mp3"):
            
            remove("prueba.mp3")
        else:
            self.lbl.place(x=350, y=600)
    
    #Segunda Ventana

    def segunda(self):
        self.ven2 = Frame(self.ven, width=1280, height=720)
        self.ven2.place(x=0, y=0)

        #Entry de texto a audio
        self.txt2 = Entry(self.ven2, width=40, font=("Console", 30), background="#FF4D00")
        self.txt2.place(x=200, y=50)

        #Button de voz a texto
        self.btngrabar = Button(self.ven2, text="Grabar Voz", font=("Console", 30), background="#FF4D00", command=self.grabar)
        self.btngrabar.place(x=850, y=250)
        self.btnrepro = Button(self.ven2, text="Reproducir", font=("Console", 30), background="#FF4D00")
        self.btnrepro.place(x=210, y=250)
        self.btncopiar = Button(self.ven2, text="Copiar", font=("Console", 30), background="#FF4D00")
        self.btncopiar.place(x=250, y=400)
        self.btnatras = Button(self.ven2,text="Atras", font=("Console", 30), background="#FF4D00", command=self.atras)
        self.btnatras.place(x=910, y=400)
    
    def grabar(self):
        
        self.r = sr.Recognizer()
        with sr.Microphone() as self.source:
            print("ya puedes hablar")
            self.audio = self.r.listen(self.source)
            try:
                self.text = self.r.recognize_google(self.audio)
                self.txt2.insert(0, self.text)
            except:
                print("no se pudo escuchar")

    def atras(self):
        self.ven2.place_forget()



if __name__=='__main__':
    ventana = Tk()
    application = inicio(ventana)
    ventana.mainloop()
