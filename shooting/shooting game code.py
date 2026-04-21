import pgzrun
import random


HEIGHT=600
WIDTH=1200
TITLE='Shooting game Bang!'
bug=Actor("bug")
ship=Actor("f16_fighter_jet")
White=(255,255,255)
Blue=(0,0,255)
speed=2
enemies=[]
score=0
direction=1


ship.pos=(WIDTH//2,HEIGHT-60)
bullets=[]

for i in range(8):
    enemies.append(Actor('bug'))
    enemies[-1].x=100+90*i
    enemies[-1].y=80


def draw():
    screen.clear()
    screen.fill(Blue)
    ship.draw()
    
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    display_score()


def update():
    global score,direction
    move_down=False
    if keyboard.left:
        ship.x-=speed
        if ship.x<=0:
            ship.x=0
    if keyboard.right:
        ship.x+=speed
        if ship.x>=WIDTH:
            ship.x=WIDTH
    for bullet in bullets:
        if bullet.y<=0:
            bullets.remove(bullet)
        else:
            bullet.y=bullet.y-10
    if len(enemies)>0 and (enemies[-1].x>WIDTH-80 or enemies[0].x<80):
        move_down=True
        direction=direction*-1
    for enemy in enemies:
        enemy.x+=5*direction
        if move_down==True:
            enemy.y+=50
        for bullet in bullets:
            if enemy.colliderect(bullet):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score+=10
    if len(enemies)==0:
       print(len(enemies))
       display_gameover()
    


def display_score():
    screen.draw.text(str(score),(50,30))

def display_gameover():
    screen.draw.text("Game Over",(250,300))  
 

def on_key_down(key):
    if key==keys.SPACE:
       bullets.append(Actor('bullet')) 
       bullets[-1].x=ship.x
       bullets[-1].y=ship.y-50


if enemies==0:
    screen.draw.text(str(score),(10,10),fontsize=30)

pgzrun.go()