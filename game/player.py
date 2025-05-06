import pygame
from settings import BLOCK_SIZE
from settings import BLOCK_SIZE, TOP_BAR_HEIGHT
from settings import CHARACTER_DATA

class Player:
    def __init__(self, x, y, char_name):
        self.x = x
        self.y = y
        self.char_name = char_name
        self.image = pygame.image.load(CHARACTER_DATA[char_name]["image"])
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
        screen.blit(self.image, (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE + TOP_BAR_HEIGHT))