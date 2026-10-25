import pgzrun
import random

WIDTH = 800
HEIGHT = 600

TITLE = "click the planets in order"

lines = []
address = []
next_planet = 0

planets=["mercury","venus","earth","mars","jupiter","saturn","uranus","neptune"]
total_planet = 8

for i in range(len(planets)):
    p = planets[i]+".png"
    print(p)
    mercury = Actor(p)
    mercury.x = random.randint(0,WIDTH)
    mercury.y = random.randint(0,HEIGHT)
    address.append(mercury)

def draw():
    number = 1
    screen.blit("space",(0,0))
    for i in address:
        i.draw()
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+18),color="green")
        number += 1
    for i in lines:
        screen.draw.line(i[0],i[1],color = "white")

def on_mouse_down(pos):
    global next_planet, lines
    if next_planet<total_planet:
        if address[next_planet].collidepoint(pos):
            if next_planet>0:
                lines.append((address[next_planet-1].pos,address[next_planet].pos))
            next_planet = next_planet+1
        else:
            next_planet = 0
            lines = []




pgzrun.go()
