import pgzrun
import random


TITLE="CLICK THE BAG GAME"
WIDTH=1100
HEIGHT=900
CENTRE_X=WIDTH/2
CENTRE_Y=HEIGHT/2
centre=(CENTRE_X,CENTRE_Y)
start_speed=10
ITEMS=["paperbag","crate","plasticbag","battery","bottle","chips"]
gameover=False
game_complete=False
current_level=1
final_level=6
items=[]
animations=[]


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


def update():
    global items 
    if len(items)==0:
        items=make_items(current_level)
        

def make_items(number_of_extra_items):
    items_to_create=get_option_to_create(number_of_extra_items)
    new_items=create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(number_of_extra_items):
    items_to_create=["paperbag"]
    for i in range(0,number_of_extra_items):
        random_option=random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items=[]
    for option in items_to_create:
        item=Actor(option)
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    number_of_gaps=len(items_to_layout)
    gap_size=WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    for index,item in enumerate(items_to_layout):
        newX_pos=(index+1)*gap_size
        item.x=newX_pos



def animate_items(items_to_animate):
    global animations
    animations=[]
    for item in items_to_animate:
        duration=start_speed-current_level
        item.anchor=("center","bottom")
        animation=animate(item,duration=duration,on_finished=handle_game_over,y=HEIGHT)
        animations.append(animation)

def handle_game_over():
    global gameover
    gameover=True



def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize=60, center=centre, color="white")
    screen.draw.text(sub_heading_text, fontsize=30, center=(CENTRE_X, CENTRE_Y + 30), color="white")



def on_mouse_down(pos):
    global items, current_level
    for item in items:
        if item.collidepoint(pos):
            if "paperbag" in item.image:
                handle_game_complete()
            else:
                handle_game_over()
    
            
def handle_game_complete():
    global current_level,items,animations,game_complete
    stop_animations(animations)
    if current_level==final_level:
        game_complete=True
    else:
    
        current_level=current_level+1
        items=[]
        animations=[]
    
def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()



pgzrun.go()
