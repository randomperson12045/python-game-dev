import pgzrun
from random import randint 


TITLE="BEE"
WIDTH=600
HEIGHT=500
SCORE=0
gameover=False
bee=Actor('bee-removebg-preview')
bee.pos=100,100
flower=Actor('flower remove bg')
flower.pos=200,200

def draw():
    screen.blit("background",(0,0))
    bee.draw()
    bee.scale=2
    flower.draw()
    screen.draw.text("SCORE: "+str(SCORE),color="black",topleft=(10,10))

    if gameover:
        screen.fill("red")
        screen.draw.text("Time's up! Your final score is "+str(SCORE),midtop=(WIDTH/2,10),fontsize=40,color="white")
    
def place_flower():
    flower.x=randint(70,(WIDTH-70))
    flower.y=randint(70,(HEIGHT-70))

def time_up():
    global gameover
    gameover=True

def update():
    global SCORE
    if keyboard.left:
        bee.x-=2
    if keyboard.right:
        bee.x+=2
    if keyboard.up:
        bee.y-=2
    if keyboard.down:
        bee.y+=2
    
    flower_collected=bee.colliderect(flower)
    if flower_collected:
        SCORE+=10
        place_flower()

clock.schedule(time_up,60.0)

pgzrun.go()
