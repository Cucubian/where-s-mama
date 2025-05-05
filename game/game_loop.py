import pygame
import os
import sys
from settings import *
from maze.maze import generate_maze, draw_grid
from maze.a_star import a_star
from game.player import Player
from game.bfs import bfs
from game.ui import show_menu, show_game_over
import time
import random
from game.sound_manager import SoundManager

HIGHSCORE_FILE = os.path.join('assets', 'highscore.txt')
def load_highscore():
    try:
        with open(HIGHSCORE_FILE, 'r') as file:
            score = int(file.read().strip())
            return max(0, score)
    except (FileNotFoundError, ValueError):
        return 0
def save_highscore(highscore):
    with open(HIGHSCORE_FILE, 'w') as file:
        file.write(str(highscore))
def get_random_positions():
    while True:
        start = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        end = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if start != end:
            return start, end
def get_min_steps(grid, start, end):
    path = a_star(grid, start, end)
    print(f"Min steps calculated (before adjustment): {len(path) if path else 'No path'}")
    if path:
        print(f"Path: {path}")
        return len(path) - 1 if len(path) > 1 else 0, path
    return 9999, path
def run_game(screen):
    clock = pygame.time.Clock()
    global CURRENT_LEVEL
    CURRENT_LEVEL = 1
    highscore = load_highscore()
    running_menu = True
    
    sound_manager = SoundManager()
    sound_manager.play_music()

    while running_menu:
        if show_menu(screen, CURRENT_LEVEL, sound_manager):
            playing = True
            while playing:
                while True:
                    start_pos, end_pos = get_random_positions()
                    grid = generate_maze(start_pos, end_pos)
                    if bfs(grid, start_pos, end_pos):
                        break
                min_steps, path = get_min_steps(grid, start_pos, end_pos)
                if not path:
                    continue
                player = Player(*start_pos)
                visited_tiles = set()
                steps = 0
                game_running = True
                start_time = time.time()
                time_limit = TIME_LIMIT
                suggested_path = []
                while game_running:
                    clock.tick(FPS)
                    current_time = time.time()
                    elapsed_time = current_time - start_time
                    remaining_time = max(0, int(time_limit - elapsed_time))
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT and player.move(-1, 0, grid):
                                steps += 1
                                visited_tiles.add((player.x, player.y))
                                sound_manager.play_move()
                            elif event.key == pygame.K_RIGHT and player.move(1, 0, grid):
                                steps += 1
                                visited_tiles.add((player.x, player.y))
                                sound_manager.play_move()
                            elif event.key == pygame.K_UP and player.move(0, -1, grid):
                                steps += 1
                                visited_tiles.add((player.x, player.y))
                                sound_manager.play_move()
                            elif event.key == pygame.K_DOWN and player.move(0, 1, grid):
                                steps += 1
                                visited_tiles.add((player.x, player.y))
                                sound_manager.play_move()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            x, y = event.pos
                            if quit_rect.collidepoint(x, y):
                                sound_manager.stop_music()
                                game_running = False
                                playing = False
                                CURRENT_LEVEL = 1
                                sound_manager.play_music()  # Restart music when returning to menu
                                break
                            elif help_rect.collidepoint(x, y):
                                current_pos = (player.x, player.y)
                                path = a_star(grid, current_pos, end_pos)
                                if path:
                                    suggested_path = path
                                else:
                                    suggested_path = []

                    screen.fill(WHITE)
                    pygame.draw.rect(screen, (230, 230, 230), (0, 0, WIDTH, 50))
                    font = get_font(18)
                    screen.blit(font.render(f'Level: {CURRENT_LEVEL}', True, PURPLE), (10, 10))
                    screen.blit(font.render(f'Min steps: {min_steps}', True, ORANGE), (90, 10))
                    screen.blit(font.render(f'Steps: {steps}', True, BLUE), (210, 10))
                    screen.blit(font.render(f'Time left: {remaining_time}s', True, RED), (300, 10))

                    quit_text = font.render('Quit', True, RED)
                    quit_rect = quit_text.get_rect(topleft=(WIDTH - 70, 10))
                    screen.blit(quit_text, quit_rect)

                    help_text = font.render('Help', True, BLUE)
                    help_rect = help_text.get_rect(topleft=(WIDTH - 150, 10))
                    screen.blit(help_text, help_rect)

                    draw_grid(screen, grid, [], start_pos, end_pos, visited_tiles, suggested_path)
                    player.draw(screen)

                    if (player.x, player.y) == end_pos:
                        sound_manager.play_win()
                        if CURRENT_LEVEL > highscore:
                            highscore = CURRENT_LEVEL
                            save_highscore(highscore)
                        CURRENT_LEVEL += 1
                        if show_game_over(screen, True, steps, min_steps, CURRENT_LEVEL, highscore):
                            game_running = False
                        else:
                            pygame.quit()
                            sys.exit()

                    elif steps >= min_steps:
                        pygame.mixer.stop()
                        sound_manager.play_lose()
                        CURRENT_LEVEL = 1
                        if show_game_over(screen, False, steps, min_steps, CURRENT_LEVEL, highscore):
                            game_running = False
                        else:
                            pygame.quit()
                            sys.exit()

                    elif elapsed_time >= time_limit:
                        pygame.mixer.stop()
                        sound_manager.play_lose()
                        CURRENT_LEVEL = 1
                        if show_game_over(screen, False, steps, min_steps, CURRENT_LEVEL, highscore):
                            game_running = False
                        else:
                            pygame.quit()
                            sys.exit()

                    pygame.display.flip()
        else:
            sound_manager.stop_music()
            running_menu = False