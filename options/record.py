#IMPORTS
import pygame as pg
from params.param1 import *

def record(file_name):
    running, mod = 1, 1
    keypresses = []
    pg.display.set_caption("EiffelStudio - Record | Change range: 0 - =")

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                running = False
            if event.type == pg.KEYDOWN:
                key = str(event.unicode)
                if key in keymod:
                    mod = keymod.index(str(event.unicode))
                elif key in keylist:
                    key = key+str(mod)
                    notes[key][0].play()
                    keypresses.append([1, notes[key][1], pg.time.get_ticks()])
                    screen.blit(font.render(notes[key][1], 0, (255,255,255)), notes[key][3])
            if event.type == pg.KEYUP and str(event.unicode) != '' and str(event.unicode) in keylist:
                key = str(event.unicode)+str(mod)
                notes[key][0].fadeout(100)
                keypresses.append([0, notes[key][1], pg.time.get_ticks()])
                screen.blit(font.render(notes[key][1], 0, notes[key][4]), notes[key][3])

        pg.display.update()
    pg.display.set_caption("Exporting sound sequence")
    if len(keypresses) > 1:
        for i in range(len(keypresses)-1):
            keypresses[-i-1][2] = keypresses[-i-1][2] - keypresses[-i-2][2]
        keypresses[0][2] = 0 # first at zero

        with open(file_name, "w") as file:
            for i in range(len(keypresses)):
                file.write(str(keypresses[i])+'\n') # separate lines for readability
        file.close()
    pg.mixer.quit()
    pg.quit()