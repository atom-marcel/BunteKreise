# @Author: Marcel Maluta
# @Date:   2022-05-26T11:26:45+02:00
# @Email:  marcelmaluta@gmail.com
# @Last modified by:   Marcel Maluta
# @Last modified time: 2022-05-26T13:14:54+02:00



import pygame
import math
from point import Point
import random

window_x = 1920
window_y = 1080

sim_window = pygame.display.set_mode((window_x, window_y))
clock = pygame.time.Clock()

p = Point((window_x / 2) + 5, (window_y / 2) + 0, window_x / 2, window_y / 2)

j = 1
r = 5
r_inc = 2
j_inc = 1

resolution = 32
phi = math.pi / resolution

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    clock.tick(20)
    phi = (j * math.pi) / resolution
    p.polar_move(r, phi)
    p.draw(sim_window)
    j += j_inc
    r += r_inc
    pygame.display.flip()
    if(r > 500):
        r = 5
        j = -1
        j_inc *= -1
        sim_window.fill((0, 0, 0))
