import random
import pygame
from settings import *

# Load ảnh rock (cục đá) và grass (cỏ) 1 lần
ROCK_IMG = pygame.image.load('assets/images/rock.png')
ROCK_IMG = pygame.transform.scale(ROCK_IMG, (CELL_SIZE, CELL_SIZE))

GRASS_IMG = pygame.image.load('assets/images/grass.png')
GRASS_IMG = pygame.transform.scale(GRASS_IMG, (CELL_SIZE, CELL_SIZE))

FOOTPRINT_IMG = pygame.image.load('assets/images/footprint.png')
FOOTPRINT_IMG = pygame.transform.scale(FOOTPRINT_IMG, (CELL_SIZE, CELL_SIZE))

END_IMG = pygame.image.load('assets/images/mother1.jpg')  # Thay đổi đường dẫn nếu cần
END_IMG = pygame.transform.scale(END_IMG, (CELL_SIZE, CELL_SIZE))

def generate_maze(start_pos, end_pos):
    """
    Trả về grid kích thước GRID_WIDTH x GRID_HEIGHT:
    0 = đường đi, 1 = chướng ngại vật (rock)
    """
    grid = [[0 for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]
    
    # Sinh chướng ngại vật 20%, trừ START và END
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            # Sinh chướng ngại vật với xác suất OBSTACLE_RATIO
            if random.random() < OBSTACLE_RATIO and (x, y) != start_pos and (x, y) != end_pos:
                grid[x][y] = 1

    return grid

def draw_grid(screen, grid, path, start, end, visited_tiles):
    """
    Vẽ grid lên screen:
    - grid[x][y] == 1 → blit rock image
    - (x,y) trong path → highlight đường đi xanh (sử dụng cỏ)
    - ngược lại fill cỏ (grass image)
    Cuối cùng vẽ viền ô (GRAY) và 2 ô start/end.
    """
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE + TOP_BAR_HEIGHT, CELL_SIZE, CELL_SIZE)

            if (x, y) in visited_tiles:
                screen.blit(FOOTPRINT_IMG, rect)

            elif grid[x][y] == 1:
                screen.blit(ROCK_IMG, rect)
            elif (x, y) in path:
                screen.blit(GRASS_IMG, rect)
            else:
                screen.blit(GRASS_IMG, rect)

            pygame.draw.rect(screen, GRAY, rect, 1)

    # Vẽ start
    sx, sy = start
    pygame.draw.rect(screen, GREEN, pygame.Rect(sx * CELL_SIZE, sy * CELL_SIZE + TOP_BAR_HEIGHT, CELL_SIZE, CELL_SIZE))

    # Vẽ end với ảnh
    ex, ey = end
    screen.blit(END_IMG, pygame.Rect(ex * CELL_SIZE, ey * CELL_SIZE + TOP_BAR_HEIGHT, CELL_SIZE, CELL_SIZE))
