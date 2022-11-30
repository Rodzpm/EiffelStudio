#IMPORTS
import numpy as np
import pygame as pg
from params.param3 import *
from synth.synth_export import synth

def export(file_name):
    with open("partitions/"+file_name+".txt", "r") as file:
        notes = [eval(line.rstrip()) for line in file]
    file.close()

    track = []
    for i in range(int(len(notes)/2)):
        track = track + list(np.zeros(max(0, int(44.1*(notes[i*2][2]-100)))))
        track = track + synth(freqs[notes[i*2][1]], song, 1e-3*(notes[i*2+1][2]+100))
    
    arr = 32767*np.asarray(track)*0.5
    sound = np.asarray([arr,arr]).T.astype(np.int16)
    sound = pg.sndarray.make_sound(sound.copy())

    import wave

    sfile = wave.open(file_name+"wav", 'w')
    sfile.setframerate(44100)
    sfile.setnchannels(2)
    sfile.setsampwidth(2)
    sfile.writeframesraw(sound)
    sfile.close()

    pg.mixer.quit()
    pg.quit()  