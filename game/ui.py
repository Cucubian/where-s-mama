# === game/ui.py ===
import pygame
import sys
from settings import WIDTH, HEIGHT, WHITE, BLUE, GREEN, RED, ORANGE, PURPLE  # Thêm PURPLE
from settings import get_font


def show_menu(screen, level=1):
    background = pygame.image.load('assets/images/mother.png')  # Đường dẫn đến ảnh nền
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Đảm bảo vừa với màn hình

    screen.blit(background, (0, 0))

    font = get_font(32)
    title1 = font.render("Where's Mama - Little Monkey", True, BLUE)
    title2 = font.render(f'Level {level}', True, BLUE)

    screen.blit(title1, (WIDTH//2 - title1.get_width()//2, HEIGHT//4 - 30))
    screen.blit(title2, (WIDTH//2 - title2.get_width()//2, HEIGHT//4 + 30))

    font = get_font(24)
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

def show_game_over(screen, won, steps, min_steps, level, highscore):
    # xử lý thêm highscore ở đây nếu cần

    # Chọn ảnh nền khác nhau tùy kết quả
    if won:
        background = pygame.image.load('assets/images/monkeyLaugh.png')  # ảnh khi thắng
    else:
        background = pygame.image.load('assets/images/monkeyCry.png')  # ảnh khi thua
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