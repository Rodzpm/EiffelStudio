import pygame as pg

from params.param2 import *

def listen_music(file_path):
    with open(file_path, "r") as file:
        keypresses = [eval(line.rstrip()) for line in file]
    file.close()

    running = 1
    for i in range(len(keypresses)):
        if not running:
            break
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                running = False
        
        key = keypresses[i][1]
        pg.time.wait(keypresses[i][2])
        if keypresses[i][0]:
            notes[key][1].play()
            screen.blit(font.render(notes[key][4], 0, (255,255,255)), notes[key][2])
        else:
            notes[key][1].fadeout(100)
            screen.blit(font.render(notes[key][4], 0, notes[key][3]), notes[key][2])

        pg.display.update()

    pg.time.wait(500)
    pg.quit() 