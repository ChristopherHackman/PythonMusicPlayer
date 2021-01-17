import pygame
import tkinter as tkr


player = tkr.Tk()

player.title("Music Player")
player.geometry("500x500")


file = "LZ.mp3"

'''Action Event'''


def Play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


def Stop():
    pygame.mixer.music.fadeout(2500)


def Pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


def getmusic():
    pygame.mixer.music.get_pos()


button1 = tkr.Button(player, width=5, height=3, text="Play", command=Play)
button1.pack(fill="x")

button2 = tkr.Button(player, width=5, height=3, text="Stop", command=Stop)
button2.pack(fill="x")

button3 = tkr.Button(player, width=5, height=3, text="Pause", command=Pause)
button3.pack(fill="x")

button4 = tkr.Button(player, width=5, height=3, text="Unpause", command=unpause)
button4.pack(fill="x")


player.mainloop()
