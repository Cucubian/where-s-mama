# === maze.py ===
import random
import pygame
from settings import *

def generate_maze():
    grid = [[0 for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if random.random() < 0.2 and (x, y) != START_POS and (x, y) != END_POS:
                grid[x][y] = 1  # 1 = obstacle
    return grid

def draw_grid(screen, grid, path, start, end):
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if grid[x][y] == 1:
                color = BLACK
            elif (x, y) in path:
                color = BLUE
            else:
                color = WHITE
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)

    pygame.draw.rect(screen, GREEN, pygame.Rect(start[0]*CELL_SIZE, start[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, pygame.Rect(end[0]*CELL_SIZE, end[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))