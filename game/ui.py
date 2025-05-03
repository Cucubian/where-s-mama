# === game/ui.py ===
import pygame
import sys
from settings import WIDTH, HEIGHT, WHITE, BLUE, GREEN, RED, ORANGE  # Thêm ORANGE

def show_menu(screen, level=1):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 74)
    title = font.render(f'Maze Runner - Level {level}', True, BLUE)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//4))

    font = pygame.font.Font(None, 36)
    start_button = font.render('Start Game', True, GREEN)
    quit_button = font.render('Quit', True, RED)

    screen.blit(start_button, (WIDTH//2 - start_button.get_width()//2, HEIGHT//2))
    screen.blit(quit_button, (WIDTH//2 - quit_button.get_width()//2, HEIGHT//2 + 50))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if WIDTH//2 - start_button.get_width()//2 <= x <= WIDTH//2 + start_button.get_width()//2:
                    if HEIGHT//2 <= y <= HEIGHT//2 + 40:
                        return True
                if WIDTH//2 - quit_button.get_width()//2 <= x <= WIDTH//2 + quit_button.get_width()//2:
                    if HEIGHT//2 + 50 <= y <= HEIGHT//2 + 90:
                        pygame.quit(); sys.exit()

def show_game_over(screen, won, steps, min_steps, level=1):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 74)
    text = font.render('You Win!' if won else 'Game Over!', True, GREEN if won else RED)
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//4))

    font = pygame.font.Font(None, 36)
    steps_text = font.render(f'Steps: {steps}', True, BLUE)
    screen.blit(steps_text, (WIDTH//2 - steps_text.get_width()//2, HEIGHT//2))

    min_text = font.render(f'Min steps: {min_steps}', True, ORANGE)
    screen.blit(min_text, (WIDTH//2 - min_text.get_width()//2, HEIGHT//2 + 40))

    replay_btn = font.render(f'Play Level {level}', True, GREEN)
    quit_btn = font.render('Quit', True, RED)

    screen.blit(replay_btn, (WIDTH//2 - replay_btn.get_width()//2, HEIGHT//2 + 90))
    screen.blit(quit_btn, (WIDTH//2 - quit_btn.get_width()//2, HEIGHT//2 + 140))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if WIDTH//2 - replay_btn.get_width()//2 <= x <= WIDTH//2 + replay_btn.get_width()//2:
                    if HEIGHT//2 + 90 <= y <= HEIGHT//2 + 130:
                        return True
                if WIDTH//2 - quit_btn.get_width()//2 <= x <= WIDTH//2 + quit_btn.get_width()//2:
                    if HEIGHT//2 + 140 <= y <= HEIGHT//2 + 180:
                        pygame.quit(); sys.exit()