#IMPORTS
import numpy as np
import pygame as pg
from synth.synth import synth

#pygame init
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((1280, 720))
font = pg.font.SysFont("Impact", 48)
song = "organ"

#keybind
keylist = '123456789azertyuiopqsdfghjklmwxcvbn,;'
notes_file = open("params/noteslist.txt")
file_contents = notes_file.read()
notes_file.close()
noteslist = file_contents.splitlines()

keymod = '0-='
notes = {} # dict to store samples
freq = 16.3516 # start frequency
posx, posy = 25, 25 #start position

#set all notes and display them
for i in range(len(noteslist)):
    mod = int(i/36)
    key = keylist[i-mod*36]+str(mod) 
    sample = synth(freq, song)
    color = np.array([np.sin(i/25+1.7)*130+125,np.sin(i/30-0.21)*215+40, np.sin(i/25+3.7)*130+125])
    color = np.clip(color, 0, 255)
    notes[key] = [sample, noteslist[i], freq, (posx, posy), 255*color/max(color)]
    freq = freq * 2 ** (1/12)
    posx = posx + 140
    if posx > 1220:
        posx, posy = 25, posy+56
        
    screen.blit(font.render(notes[key][1], 0, notes[key][4]), notes[key][3])
    pg.display.update()