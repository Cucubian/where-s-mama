# === maze/maze.py ===
import random
import pygame
from settings import *

# Load ảnh rock (cục đá) và grass (cỏ) 1 lần
ROCK_IMG = pygame.image.load('assets/images/rock.png')
ROCK_IMG = pygame.transform.scale(ROCK_IMG, (CELL_SIZE, CELL_SIZE))

GRASS_IMG = pygame.image.load('assets/images/grass.png')
GRASS_IMG = pygame.transform.scale(GRASS_IMG, (CELL_SIZE, CELL_SIZE))

def generate_maze():
    """
    Trả về grid kích thước GRID_WIDTH x GRID_HEIGHT:
    0 = đường đi, 1 = chướng ngại vật (rock)
    """
    grid = [[0 for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            # sinh chướng ngại vật 20%, trừ START và END
            if random.random() < 0.2 and (x, y) != START_POS and (x, y) != END_POS:
                grid[x][y] = 1
    return grid

def draw_grid(screen, grid, path, start, end):
    """
    Vẽ grid lên screen:
    - grid[x][y] == 1 → blit rock image
    - (x,y) trong path → highlight đường đi xanh (sử dụng cỏ)
    - ngược lại fill cỏ (grass image)
    Cuối cùng vẽ viền ô (GRAY) và 2 ô start/end.
    """
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

            if grid[x][y] == 1:
                # Vẽ rock thay vì ô đen
                screen.blit(ROCK_IMG, rect)
            elif (x, y) in path:
                # Vẽ đường đi bằng grass
                screen.blit(GRASS_IMG, rect)
            else:
                # Vẽ background là cỏ
                screen.blit(GRASS_IMG, rect)

            # Vẽ lưới
            pygame.draw.rect(screen, GRAY, rect, 1)

    # Vẽ start và end
    sx, sy = start
    ex, ey = end
    pygame.draw.rect(screen, GREEN, pygame.Rect(sx * CELL_SIZE, sy * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED,   pygame.Rect(ex * CELL_SIZE, ey * CELL_SIZE, CELL_SIZE, CELL_SIZE))
