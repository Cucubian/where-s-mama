import pygame
from settings import BLOCK_SIZE

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('assets/images/monkey.png')
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))

    def move(self, dx, dy, grid):
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != 1:
            self.x = new_x
            self.y = new_y
            return True
        return False

    def draw(self, screen):
        screen.blit(self.image, (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE))
