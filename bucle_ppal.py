import pygame as pg
from pygame.locals import *

class Target():
    def __init__(self, x=0, y=0):
        #self.position = [x, y]
        self.custome = pg.draw.rect(screen, (255, 0, 0), (x, y, 100, 20)) #fix blocks

#Initialize and set up screen
pg.init()
screen = pg.display.set_mode((600, 800))
pg.display.set_caption("Arkanoid")

# Game speed
fps = 100
fpsClock = pg.time.Clock()

#Initialize game condition
game_over = False

#Initial ball position
ball_x = 300
ball_y = 799

#Initial block position
pos_x = 0

# Initial ball direction (up & right)
dx = 1
dy = -1

colTarget = (25, 175, 325, 475)
rowTarget = 40

targets = []

#Game 
while not game_over:
    events = pg.event.get()

    #Boundary conditions
    if ball_x >= (600 - 10) or ball_x <= (0 + 10):
        dx = dx * -1
    if ball_y == 800: #game_over!!!
        game_over = True #dy = -1
    elif ball_y == 0 + 10: #WIN
        dy = dy * -1

    if ball_y == 760 and ball_x in range (pos_x-25, pos_x+125):
        dy = -1

    #Moving block to push ball
    for event in events:
        if event.type == pg.QUIT:
            game_over = True
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT and pos_x < 500:
                pos_x += 50
            elif event.key == K_LEFT and pos_x > 0:
                pos_x += -50

    #Ball dynamics
    ball_x += dx
    ball_y += dy

    screen.fill((160, 160, 160))
    pg.draw.rect(screen, (0, 0, 255), (pos_x, 770, 100, 20)) #moving block
    pg.draw.circle(screen, (255, 255, 0), (ball_x, ball_y), 10)        #ball

    for i in range (4):
        Target(colTarget[i], rowTarget)
        #if Target.[1] == ball_y:
            #Target.position[0] = -200



    pg.display.flip()
    fpsClock.tick(fps)

pg.quit()




