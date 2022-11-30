#IMPORTS
import pygame as pg
from params.param1 import *

def playground():
    running, mod = 1, 1
    pg.display.set_caption("EiffelStudio - Playground | Change range: 0 - =")

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
                    screen.blit(font.render(notes[key][1], 0, (255,255,255)), notes[key][3])
            if event.type == pg.KEYUP and str(event.unicode) != '' and str(event.unicode) in keylist:
                key = str(event.unicode)+str(mod)
                notes[key][0].fadeout(100)
                screen.blit(font.render(notes[key][1], 0, notes[key][4]), notes[key][3])

        pg.display.update()
    pg.mixer.quit()
    pg.quit()