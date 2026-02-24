import pgzrun
from random import randint
from time import time

starttime=0
totaltime=0
endtime=0

pikachus=[]
lines=[]
TITLE="CONNECT PIKACHU"
WIDTH=800
HEIGHT=500
number_of_pikachu=8
next_pik=0


def create_pikachu():
    global number_of_pikachu,starttime
    for i in range (0,number_of_pikachu):
        pik=Actor('pikachu')
        pik.pos=randint(40,WIDTH-40),randint(40,HEIGHT-40)
        pikachus.append(pik)
    starttime=time()

def draw():
    global totaltime
    screen.blit("bg",(0,0))
    number=1
    for pik in pikachus:
        screen.draw.text(str(number),(pik.pos[0],pik.pos[1]+40))
        pik.draw()
        number=number+1

    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))

    if next_pik<number_of_pikachu:
        totaltime=time()-starttime
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize=30)

def on_mouse_down(pos):
    global next_pik,lines
    if next_pik<number_of_pikachu:
        if pikachus[next_pik].collidepoint(pos):
            if next_pik:
                print("adding line")
                lines.append((pikachus[next_pik-1].pos,pikachus[next_pik].pos))
                print("new data {lines}")
            next_pik=next_pik+1
        else:
            lines=[]
            next_pik=0
create_pikachu()
pgzrun.go()