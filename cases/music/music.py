#! /usr/bin/env python3 

import pygame
import tkinter as tkr 
from tkinter.filedialog import askdirectory
import os 

music_player = tkr.Tk()
music_player.title('My Music')
music_player.geometry('700x800')

directory = askdirectory()
os.chdir(directory)

song_list = os.listdir()
play_list = tkr.Listbox(music_player, font='Helvetica 16 bold', bg='gold', selectmode=tkr.SINGLE)

for item in song_list:
    pos = 0 
    play_list.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    
def stop():
    pygame.mixer.music.stop()
    
def pause():
    pygame.mixer.music.pause()
    
def unpause():
    pygame.mixer.music.unpause()
    
Button1 = tkr.Button(music_player,
                     width=8, 
                     height=5, 
                     font='Helvetica 14 bold', 
                     text='Воспроизведение', 
                     command=play,
                     bg='black', 
                     fg='white')

Button2 = tkr.Button(music_player,
                     width=8, 
                     height=5, 
                     font='Helvetica 14 bold', 
                     text='Остановить', 
                     command=stop,
                     bg='red', 
                     fg='white')

Button3 = tkr.Button(music_player,
                     width=8, 
                     height=5, 
                     font='Helvetica 14 bold', 
                     text='Пауза', 
                     command=pause,
                     bg='gray', 
                     fg='white')

Button4 = tkr.Button(music_player,
                     width=8, 
                     height=5, 
                     font='Helvetica 14 bold', 
                     text='Снять с паузы', 
                     command=unpause,
                     bg='orange', 
                     fg='white')

var = tkr.StringVar()

song_title = tkr.Label(music_player, font='Helvetica 14 bold', textvariable=var)
song_title.pack()

Button1.pack(fill='x')
Button2.pack(fill='x')
Button3.pack(fill='x')
Button4.pack(fill='x')

play_list.pack(fill='both', expand='yes')
music_player.mainloop()
