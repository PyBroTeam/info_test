import sys
import pygame
from pygame.draw import *

pygame.init()

FPS = 30

#set size of the screen
screen = pygame.display.set_mode((630, 900))

#set screen color
screen_color = (0, 0, 0) #black
screen.fill(screen_color)
pygame.display.flip()

#draw the sky
def sky():
    color = (105, 105, 105) #grey
    x = 0 #left
    y = 0 #top
    width = 900
    heigh = 375
    size = (x, y, width, heigh)
    pygame.draw.rect(screen, color, size)

#draw the moon
def moon():
    color = (220, 220, 220) #light grey
    x = 560 #position left
    y = 80 #position top
    radius = 55
    pygame.draw.circle (screen, color, (x, y), radius)

#draw all clouds
def cloud_1():
    color = (40, 40, 40) #dark grey middle cloud
    x = 30 #left
    y = 85 #top
    width = 480
    heigh = 60
    size = (x, y, width, heigh)
    pygame.draw.ellipse (screen, color, size)

def cloud_2():
    color = (87, 87, 90) #grey for upper cloud on the right
    x = 290 #left
    y = 55 #top
    width = 350
    heigh = 60
    size = (x, y, width, heigh)
    pygame.draw.ellipse (screen, color, size) 

def cloud_3():
    color = (87, 87, 90) #dark grey lower left cloud
    x = 380 #left
    y = 132 #top
    width = 350
    heigh = 50
    size = (x, y, width, heigh)
    pygame.draw.ellipse (screen, color, size)
  
def cloud_4():
    color = (0, 0, 0) #black cloud bottom side
    x = 300 #left
    y = 200 #top
    width = 350
    heigh = 60
    size = (x, y, width, heigh)
    pygame.draw.ellipse (screen, color, size)

sky()
moon()
cloud_1()
cloud_2()
cloud_3()
cloud_4()

#draw windows
def window_1():
    color = (81, 60, 60) #dark red
    x = 30 #left
    y = 0 #top
    width = 35
    heigh = 180
    size = (x, y, width, heigh)
    pygame.draw.rect(house_surface, color, size)

def window_2():
    color = (81, 60, 60) #dark red
    x = 95 #left
    y = 0 #top
    width = 35
    heigh = 180
    size = (x, y, width, heigh)
    pygame.draw.rect(house_surface, color, size)

def window_3():
    color = (81, 60, 60) #dark red
    x = 185 #left
    y = 0 #top
    width = 35
    heigh = 180
    size = (x, y, width, heigh)
    pygame.draw.rect(house_surface, color, size)

def window_4():
    color = (81, 60, 60) #dark red
    x = 245 #left
    y = 0 #top
    width = 35
    heigh = 180
    size = (x, y, width, heigh)
    pygame.draw.rect(house_surface, color, size)


#set house surface
house_color = (33, 33, 00) #dark green
house_x = 30 #left
house_y = 190 #top
house_width = 320
house_heigh = 460
house_size = (house_width, house_heigh)
house_surface = pygame.Surface(house_size)
house_surface.fill(house_color)
window_1()
window_2()
window_3()
window_4()
screen.blit(house_surface, (house_x, house_y))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
sys.exit()
