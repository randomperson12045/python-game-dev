import pgzrun
from random import randint


TITLE="CLICK THE BAG GAME"
WIDTH=800
HEIGHT=500
centre_x=WIDTH/2
centre_y=HEIGHT/2
centre=(centre_x,centre_y)
start_speed=10
items=["paperbag","crate","plasticbag","bin"]
gameover=False
game_complete=False
current_level=1




def draw():
    global items,current_level,gameover,game_complete
    screen.clear()
    screen.blit("bg",(0,0))
    if gameover:
        display_message("GAME OVER","please try again")
    elif game_complete:
        display_message("YOU WIN","good job")
    else:
        for item in items:
            item.draw()

    
    
    


pgzrun.go()
