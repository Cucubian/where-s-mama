import pygame
import sys
from settings import WIDTH, HEIGHT, WHITE, BLUE, GREEN, RED, ORANGE, PURPLE
from settings import get_font

def show_menu(screen, level=1, sound_manager=None):
    background = pygame.image.load('assets/images/mother.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    font = pygame.font.Font(None, 50)
    title1 = font.render("Where's Mama - Little Monkey", True, BLUE)
    title2 = font.render(f'Level {level}', True, BLUE)

    font = pygame.font.Font(None, 36)
    start_button = font.render('Start Game', True, GREEN)
    quit_button = font.render('Quit', True, RED)

    # Define rects for buttons
    start_rect = start_button.get_rect(center=(WIDTH//2, HEIGHT//2))
    quit_rect = quit_button.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))

    # Load speaker icons
    speaker_on = pygame.image.load('assets/images/speaker_on.png')
    speaker_on = pygame.transform.scale(speaker_on, (40, 40))
    speaker_off = pygame.image.load('assets/images/speaker_off.png')
    speaker_off = pygame.transform.scale(speaker_off, (40, 40))

    # Determine initial speaker icon
    if sound_manager.muted:
        speaker_icon = speaker_off
    else:
        speaker_icon = speaker_on
    speaker_rect = speaker_icon.get_rect(topright=(WIDTH - 10, 10))

    # Initial draw
    screen.blit(background, (0, 0))
    screen.blit(title1, title1.get_rect(center=(WIDTH//2, HEIGHT//4 - 30)))
    screen.blit(title2, title2.get_rect(center=(WIDTH//2, HEIGHT//4 + 30)))
    screen.blit(start_button, start_rect)
    screen.blit(quit_button, quit_rect)
    screen.blit(speaker_icon, speaker_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if start_rect.collidepoint(x, y):
                    return True
                elif quit_rect.collidepoint(x, y):
                    pygame.quit(); sys.exit()
                elif speaker_rect.collidepoint(x, y):
                    sound_manager.toggle_mute()
                    # Update speaker icon
                    if sound_manager.muted:
                        speaker_icon = speaker_off
                    else:
                        speaker_icon = speaker_on
                    # Redraw menu
                    screen.blit(background, (0, 0))
                    screen.blit(title1, title1.get_rect(center=(WIDTH//2, HEIGHT//4 - 30)))
                    screen.blit(title2, title2.get_rect(center=(WIDTH//2, HEIGHT//4 + 30)))
                    screen.blit(start_button, start_rect)
                    screen.blit(quit_button, quit_rect)
                    screen.blit(speaker_icon, speaker_rect)
                    pygame.display.flip()

        # Cursor handling
        mouse_pos = pygame.mouse.get_pos()
        if start_rect.collidepoint(mouse_pos) or quit_rect.collidepoint(mouse_pos) or speaker_rect.collidepoint(mouse_pos):
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

def show_game_over(screen, won, steps, min_steps, level, highscore):
    if won:
        background = pygame.image.load('assets/images/monkeyLaugh.png')
    else:
        background = pygame.image.load('assets/images/monkeyCry.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))

    title_font = get_font(50)
    text_font = get_font(24)
    mid_x = WIDTH // 2
    mid_y = HEIGHT // 2
    line_gap = 50

    if won:
        win_text = title_font.render('You Win!', True, GREEN)
        screen.blit(win_text, win_text.get_rect(center=(mid_x, mid_y - line_gap)))
    else:
        text1 = title_font.render('Game Over!', True, RED)
        text2 = title_font.render('You Lose!', True, RED)
        screen.blit(text1, text1.get_rect(center=(mid_x, mid_y - line_gap)))
        screen.blit(text2, text2.get_rect(center=(mid_x, mid_y)))

    steps_text = text_font.render(f'Steps: {steps}', True, BLUE)
    screen.blit(steps_text, steps_text.get_rect(center=(mid_x, mid_y + line_gap)))

    min_text = text_font.render(f'Min steps: {min_steps}', True, ORANGE)
    screen.blit(min_text, min_text.get_rect(center=(mid_x, mid_y + line_gap * 2)))

    highscore_text = text_font.render(f'High score: {highscore}', True, PURPLE)
    screen.blit(highscore_text, highscore_text.get_rect(center=(mid_x, mid_y + line_gap * 3)))

    replay_btn = text_font.render(f'Play Level {level}', True, GREEN)
    replay_rect = replay_btn.get_rect(center=(mid_x, mid_y + line_gap * 4))
    screen.blit(replay_btn, replay_rect)

    quit_btn = text_font.render('Quit', True, RED)
    quit_rect = quit_btn.get_rect(center=(mid_x, mid_y + line_gap * 5))
    screen.blit(quit_btn, quit_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if replay_rect.collidepoint(x, y):
                    return True
                if quit_rect.collidepoint(x, y):
                    pygame.quit(); sys.exit()

        mouse_pos = pygame.mouse.get_pos()
        if replay_rect.collidepoint(mouse_pos) or quit_rect.collidepoint(mouse_pos):
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)