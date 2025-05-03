import pygame
from settings import *
from maze.maze import generate_maze, draw_grid
from maze.a_star import a_star
from game.player import Player
from game.bfs import bfs
from game.ui import show_menu, show_game_over
import time
import random


def get_random_positions():
    while True:
        start = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        end = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if start != end:
            return start, end

def get_min_steps(grid, start, end):
    path = a_star(grid, start, end)
    return len(path) if path else 9999  # Tránh lỗi nếu không có đường đi

def run_game(screen):
    clock = pygame.time.Clock()
    global CURRENT_LEVEL
    CURRENT_LEVEL = 1  # Bắt đầu từ level 1

    while True:
        if show_menu(screen, CURRENT_LEVEL):
            # Sinh maze cho đến khi có đường đi
            while True:
                start_pos, end_pos = get_random_positions()
                grid = generate_maze(start_pos, end_pos)
                if bfs(grid, start_pos, end_pos):
                    break



            path = a_star(grid, start_pos, end_pos)
            if not path:
                continue  # Tạo lại maze nếu không tìm được đường đi bằng A*
            min_steps = len(path)

            player = Player(*start_pos)
            visited_tiles = set()
            steps = 0
            running = True

            start_time = time.time()
            time_limit = TIME_LIMIT

            while running:
                clock.tick(FPS)

                current_time = time.time()
                elapsed_time = current_time - start_time
                remaining_time = max(0, int(time_limit - elapsed_time))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT and player.move(-1, 0, grid):
                            steps += 1
                            visited_tiles.add((player.x, player.y))
                        elif event.key == pygame.K_RIGHT and player.move(1, 0, grid):
                            steps += 1
                            visited_tiles.add((player.x, player.y))
                        elif event.key == pygame.K_UP and player.move(0, -1, grid):
                            steps += 1
                            visited_tiles.add((player.x, player.y))
                        elif event.key == pygame.K_DOWN and player.move(0, 1, grid):
                            steps += 1
                            visited_tiles.add((player.x, player.y))


                screen.fill(WHITE)
                draw_grid(screen, grid, [], start_pos, end_pos, visited_tiles)
                player.draw(screen)

                font = pygame.font.Font(None, 36)
                screen.blit(font.render(f'Level: {CURRENT_LEVEL}', True, PURPLE), (10, 10))
                screen.blit(font.render(f'Min steps: {min_steps}', True, ORANGE), (10, 50))
                screen.blit(font.render(f'Steps: {steps}', True, BLUE), (10, 90))
                screen.blit(font.render(f'Time left: {remaining_time}s', True, RED), (10, 130))

                if (player.x, player.y) == end_pos:
                    CURRENT_LEVEL += 1  # Tăng level
                    if show_game_over(screen, True, steps, min_steps, CURRENT_LEVEL):
                        running = False  # Thoát vòng lặp để tạo mê cung mới
                    else:
                        pygame.quit(); sys.exit()  # Thoát nếu người chơi chọn Quit
                elif steps >= min_steps:
                    CURRENT_LEVEL = 1  # Reset về level 1 khi thua
                    if show_game_over(screen, False, steps, min_steps, CURRENT_LEVEL):
                        running = False  # Thoát vòng lặp để tạo mê cung mới
                    else:
                        pygame.quit(); sys.exit()  # Thoát nếu người chơi chọn Quit
                elif elapsed_time >= time_limit:
                    CURRENT_LEVEL = 1  # Reset về level 1 khi hết thời gian
                    if show_game_over(screen, False, steps, min_steps, CURRENT_LEVEL):
                        running = False  # Thoát vòng lặp để tạo mê cung mới
                    else:
                        pygame.quit(); sys.exit()  # Thoát nếu người chơi chọn Quit

                pygame.display.flip()