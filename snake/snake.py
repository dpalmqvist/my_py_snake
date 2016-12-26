import pygame

class Snake:
    def __init__(self):
        self.length = 1
        self.direction = 'right'
        self.coords = [(200, 200)]

    def step(self, snack):
        (x, y) = self.coords[0]
        if self.direction == 'right':
            x += 10
        elif self.direction == 'down':
            y += 10
        elif self.direction == 'left':
            x -= 10
        elif self.direction == 'up':
            y -= 10
        if (x, y) == snack.coord:
            self.length += 1
            snack.life = 0
        self.coords.insert(0, (x, y))
        if len(self.coords) > self.length:
            self.coords.pop(self.length)

    def extend(self):
        self.length += 1

    def turn(self, key):
        if key == pygame.K_LEFT:
            if self.direction == 'right':
                self.direction = 'up'
            elif self.direction == 'down':
                self.direction = 'right'
            elif self.direction == 'left':
                self.direction = 'down'
            elif self.direction == 'up':
                self.direction = 'left'
        elif key == pygame.K_RIGHT:
            if self.direction == 'right':
                self.direction = 'down'
            elif self.direction == 'down':
                self.direction = 'left'
            elif self.direction == 'left':
                self.direction = 'up'
            elif self.direction == 'up':
                self.direction = 'right'

    def draw(self, surf):
        for (x, y) in self.coords:
            pygame.draw.rect(surf, (0, 0, 0),
                            (x, y, 10, 10))

    def alive(self, maxx, maxy):
        (x, y) = self.coords[0]
        if len(self.coords) > 0 and (x,y) in self.coords[1:]:
            return False
        elif x < 0 or x >= maxx:
            return False
        elif y < 0 or y >= maxy:
            return False
        return True