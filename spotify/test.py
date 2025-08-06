from tkinter import Tk, Button
from reproductor import Reproductor

lista = ["musica/BABYMETAL x Slaughter To Prevail - Song 3 (OFFICIAL MUSIC VIDEO) - BABYMETAL.mp3"]
musica = Reproductor(lista[0])

def reproducirMusica():
    musica.reproducir()

winamp = Tk()
winamp.title("Winamp")
winamp.geometry("200x100")

bPlay = Button(text="▶", command = reproducirMusica)
bPlay.place(x=50,y=50)

winamp.mainloop()