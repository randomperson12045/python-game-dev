import pgzrun
from random import randint
from time import time

starttime=0
totaltime=0
endtime=0

satellites=[]
lines=[]
TITLE="CONNECT SATELLITES"
WIDTH=800
HEIGHT=500
number_of_satellites=8
next_sat=0


def create_satellite():
    global number_of_satellites,starttime
    for i in range (0,number_of_satellites):
        sat=Actor('satellite')
        sat.pos=randint(40,WIDTH-40),randint(40,HEIGHT-40)
        satellites.append(sat)
    starttime=time()

def draw():
    global totaltime
    screen.blit("space bg",(0,0))
    number=1
    for sat in satellites:
        screen.draw.text(str(number),(sat.pos[0],sat.pos[1]+20))
        sat.draw()
        number=number+1

    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))

    if next_sat<number_of_satellites:
        totaltime=time()-starttime
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize=30)

def on_mouse_down(pos):
    global next_sat,lines
    if next_sat<number_of_satellites:
        if satellites[next_sat].collidepoint(pos):
            if next_sat:
                print("adding line")
                lines.append((satellites[next_sat-1].pos,satellites[next_sat].pos))
                print(f"new data {lines}")
            next_sat=next_sat+1
        else:
            lines=[]
            next_sat=0

create_satellite()
pgzrun.go()