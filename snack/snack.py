from random import randrange
import pygame


class Snack:
    def __init__(self, maxx, maxy, snake):
        while True:
            self.coord = (randrange(0, maxx, 10), randrange(0, maxy, 10))
            if self.coord not in snake.coords:
                break
        self.life = 50

    def step(self):
        self.life -= 1

    def alive(self):
        return self.life > 0

    def draw(self, surf):
        (x, y) = self.coord
        pygame.draw.rect(surf, (255, 0, 0), (x, y, 10, 10))
