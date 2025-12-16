import pgzrun
from random import randint

WIDTH=300
HEIGHT=300

def draw():

    w=WIDTH 
    h=HEIGHT-200
    for i in range (1000):
        r=255
        g=0
        b=randint(120,255)
        
        rect=Rect((0,0),(w,h))
        rect.center=150,150
        screen.draw.rect(rect,(r,g,b))

        w=w-1
        h=h+1

pgzrun.go()
