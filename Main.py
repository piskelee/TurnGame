import math

import pygame
from pygame.locals import *

from Point import *

pygame.init()
scwidth, scheight = 600, 600
screen = pygame.display.set_mode((scwidth, scheight))


# angle
def wrap_angle(angle):
    return angle % 360


##################### Start Code ##############################

# Loading Img
space = pygame.image.load('space.jpg').convert_alpha()
planet = pygame.image.load('planet.png').convert_alpha()

# Ship set
ufo = pygame.image.load('ufo.png').convert_alpha()
width, height = ufo.get_size()
ship = pygame.transform.smoothscale(ufo, (width // 2, height // 2))
radius = 250
angle = 0.0
pos = Point(0, 0)
old_pos = Point(0, 0)

# Game LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Draw Screen
    screen.blit(space, (0, 0))

    # draw Planet
    width, height = planet.get_size()
    screen.blit(planet, ((scwidth - width) / 2, (scheight - height) / 2))

    # move Ship
    angle = wrap_angle(angle - 0.05)
    pos.x = math.sin(math.radians(angle)) * radius
    pos.y = math.cos(math.radians(angle)) * radius

    delta_x = (pos.x - old_pos.x)
    delta_y = (pos.y - old_pos.y)
    rangle = math.atan2(delta_y, delta_x)
    rangled = wrap_angle(-math.degrees(rangle))
    scratch_ship = pygame.transform.rotate(ship, rangled)

    # Draw Ship
    width, height = scratch_ship.get_size()
    x = (scwidth / 2) + pos.x - width // 2
    y = (scheight / 2) + pos.y - height // 2
    screen.blit(scratch_ship, (x, y))

    pygame.display.update()

    # update move
    old_pos.x = pos.x
    old_pos.y = pos.y

pygame.quit()
