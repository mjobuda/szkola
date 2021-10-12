from tkinter import *

#pobieranie danych automatycznie
import socket
nazwaPC = socket.gethostname()
IP = socket.gethostbyname(nazwaPC)

#Formularz graficzny - inicjacja
root = Tk()
imie = Entry(root, width=50)
imie.pack()
nazwisko = Entry(root, width=50)
nazwisko.pack()
problem = Entry(root, width=50)
problem.pack()

#Wciśnięcie przycisku zapisuje dane z formularza i dane o komputerze
def wyslij():
    with open('readme.txt', 'a') as f:
        f.write('\n' + imie.get())
        f.write('\n' + nazwisko.get())
        f.write('\n' + problem.get())
        f.write('\n' + nazwaPC)
        f.write('\n' + IP)

#przycisk formularza ma inicjować się po deklaracji funkcji "Wyslij"
myButton = Button(root, text="Wyślij", command=wyslij)
myButton.pack()

root.mainloop()