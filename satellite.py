import pygame
import pgzrun
import random
import time
HEIGHT=500
WIDTH=500
satellites=[]
lines=[]
next=0
nos=8
starttime=0
endtime=0
totaltime=0
def draw():
    global totaltime
    screen.blit("blackbackground", (0,0))
    number=1
    for i in satellites:
        i.draw()
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20)) #Draws the number of sateelite on the screen
        number+=1
    if next<nos:
        totaltime=time.time()-starttime
        screen.draw.text(str(totaltime), (50, 50), fontsize=50)
    for i in lines:
        screen.draw.line(i[0],i[1], (0, 0, 255)) #Connecting line from point 1 to point 2

def update():
    pass

def createsatellite():
    global starttime
    for i in range(nos):
        satellite=Actor("satellite")
        satellite.pos=random.randint(50, WIDTH-50),random.randint(50, WIDTH-50) #Assigns satellites to random position
        satellites.append(satellite) #Adds satellite actor to the list of satellites
    starttime=time.time()

def on_mouse_down(pos):
    global next, lines
    if next<nos:
        if satellites[next].collidepoint(pos):
            if next: #When next is zero, it becomes false, as if 0 is automatically False
                lines.append((satellites[next-1].pos,satellites[next].pos))
            next+=1 #Checks if the satellite collides with the position of the mouse
        else:
            lines=[]
            next=0


createsatellite()

pgzrun.go()