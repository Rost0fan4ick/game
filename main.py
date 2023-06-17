from pygame import *
from random import randint
back = (randint(0, 255), randint(0, 255), randint(0, 255))
win = display.set_mode((randint(750, 1366), randint(500, 768)))
win.fill(back)
clock = time.Clock()
FPS = randint(30, 120)
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)