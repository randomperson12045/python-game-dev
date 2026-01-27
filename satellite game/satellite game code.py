import pgzrun
from random import randint
from time import time

starttime=0
totaltime=0
endtime=0

satellites=[]
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
    if next_sat<number_of_satellites:
        totaltime=time()-starttime
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize=30)


create_satellite()
pgzrun.go()