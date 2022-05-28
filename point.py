# @Author: Marcel Maluta
# @Date:   2022-05-26T11:30:17+02:00
# @Email:  marcelmaluta@gmail.com
# @Last modified by:   Marcel Maluta
# @Last modified time: 2022-05-28T11:24:53+02:00

import pygame
import math
from vector import Vector
import random

class Point(object):
    def __init__(self, x, y, origin_x, origin_y):
        self.position = Vector(x, y)
        self.origin = Vector(origin_x, origin_y)

    def polar_move(self, r, phi):
        x = int(r * math.cos(phi))
        y = int(r * math.sin(phi))
        self.set_position(x, y)

    def set_position(self, x, y):
        self.position.x = x
        self.position.y = y
        self.position.add_vector(self.origin)

    def draw(self, surface):
        pygame.draw.circle(surface, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), (self.position.x, self.position.y), 5)
