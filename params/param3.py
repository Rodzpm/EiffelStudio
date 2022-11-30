#IMPORTS
import pygame as pg

pg.init()
pg.mixer.init()

a_file = open("params/noteslist.txt")
file_contents = a_file.read(); a_file.close()
noteslist = file_contents.splitlines()
freq = 16.3516 #starting frequency
freqs = {}
song = "organ"
for i in range(len(noteslist)):
    freqs[noteslist[i]]= freq
    freq = freq * 2 ** (1/12)