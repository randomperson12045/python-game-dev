from random import randint
import pgzrun


TITLE="6767"
WIDTH=500
HEIGHT=500

message=""

#creating a sprite like scratch
six7=Actor('67')

def draw():
    screen.clear()
    screen.fill(color="orange")
    six7.draw()
    six7.scale=2
    screen.draw.text(message,center=(250,20),fontsize=30)


def place_six7():
    six7.x=randint(50,WIDTH-50)
    six7.y=randint(50,HEIGHT-50)

def on_mouse_down(pos):
    global message
    if six7.collidepoint(pos):
        message="BullsEye67"
        place_six7()
    else:
        message="You missed"




place_six7()
pgzrun.go()
    
