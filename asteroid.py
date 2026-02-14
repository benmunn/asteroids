from circleshape import CircleShape
import pygame
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_angle = random.uniform(20,50) 
        new_ast_vector1 = self.velocity.rotate(split_angle)
        new_ast_vector2 = self.velocity.rotate(split_angle*(-1))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast1 = Asteroid(self.position[0], self.position[1], new_radius)
        new_ast2 = Asteroid(self.position[0], self.position[1], new_radius)
        new_ast1.velocity = new_ast_vector1
        new_ast2.velocity = new_ast_vector2
        