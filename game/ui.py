import pygame
import sys
from settings import WIDTH, HEIGHT, WHITE, BLUE, GREEN, RED, ORANGE, PURPLE
from settings import get_font, CHARACTER_DATA  # Import CHARACTER_DATA

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
    speaker_on = pygame.image.load('assets/images/mic_on.png')
    speaker_on = pygame.transform.scale(speaker_on, (60, 90))
    speaker_off = pygame.image.load('assets/images/mic_off.png')
    speaker_off = pygame.transform.scale(speaker_off, (60, 90))

    # Determine initial speaker icon
    if sound_manager.muted:
        speaker_icon = speaker_off
    else:
        speaker_icon = speaker_on
    speaker_rect = speaker_icon.get_rect(topright=(WIDTH - 10, 10))

    # Character selection
    font = pygame.font.Font(None, 24)
    char_text = font.render("Choose Character:", True, GREEN)
    char_rect = char_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

    # Load character images and scale them
    char1_img = pygame.image.load(CHARACTER_DATA["monkey1"]["image"])
    char1_img = pygame.transform.scale(char1_img, (50, 50))  # Adjust size as needed
    char1_rect = char1_img.get_rect(center=(WIDTH // 2 - 70, HEIGHT // 2 + 160))

    char2_img = pygame.image.load(CHARACTER_DATA["monkey2"]["image"])
    char2_img = pygame.transform.scale(char2_img, (50, 50))  # Adjust size
    char2_rect = char2_img.get_rect(center=(WIDTH // 2 + 70, HEIGHT // 2 + 160))

    char1_button = font.render(CHARACTER_DATA["monkey1"]["name"], True, GREEN)
    char1_button_rect = char1_button.get_rect(center=(WIDTH // 2 - 70, HEIGHT // 2 + 130))

    char2_button = font.render(CHARACTER_DATA["monkey2"]["name"], True, GREEN)
    char2_button_rect = char2_button.get_rect(center=(WIDTH // 2 + 70, HEIGHT // 2 + 130))

    selected_char = "monkey1"  # Lưu nhân vật đã chọn

    # Initial draw
    screen.blit(background, (0, 0))
    screen.blit(title1, title1.get_rect(center=(WIDTH//2, HEIGHT//4 - 30)))
    screen.blit(title2, title2.get_rect(center=(WIDTH//2, HEIGHT//4 + 30)))
    screen.blit(start_button, start_rect)
    screen.blit(quit_button, quit_rect)
    screen.blit(speaker_icon, speaker_rect)

    # Vẽ các thành phần chọn nhân vật
    screen.blit(char_text, char_rect)
    screen.blit(char1_button, char1_button_rect)
    screen.blit(char1_img, char1_rect)
    screen.blit(char2_button, char2_button_rect)
    screen.blit(char2_img, char2_rect)
    pygame.draw.rect(screen, ORANGE, char1_rect, 2)  # Highlight nhân vật mặc định
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if start_rect.collidepoint(x, y):
                    return True, selected_char  # Trả về cả lựa chọn nhân vật
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

                    # Vẽ lại phần chọn nhân vật
                    screen.blit(char_text, char_rect)
                    if selected_char == "monkey1":
                        pygame.draw.rect(screen, ORANGE, char1_rect, 2)  # Highlight nhân vật được chọn
                    screen.blit(char1_button, char1_button_rect)
                    screen.blit(char1_img, char1_rect)
                    if selected_char == "monkey2":
                        pygame.draw.rect(screen, ORANGE, char2_rect, 2)
                    screen.blit(char2_button, char2_button_rect)
                    screen.blit(char2_img, char2_rect)
                    pygame.display.flip()
                elif char1_rect.collidepoint(x, y) or char1_button_rect.collidepoint(x,y):
                    selected_char = "monkey1"
                    # Redraw menu
                    screen.blit(background, (0, 0))
                    screen.blit(title1, title1.get_rect(center=(WIDTH//2, HEIGHT//4 - 30)))
                    screen.blit(title2, title2.get_rect(center=(WIDTH//2, HEIGHT//4 + 30)))
                    screen.blit(start_button, start_rect)
                    screen.blit(quit_button, quit_rect)
                    screen.blit(speaker_icon, speaker_rect)

                    # Vẽ lại phần chọn nhân vật
                    screen.blit(char_text, char_rect)
                    if selected_char == "monkey1":
                        pygame.draw.rect(screen, ORANGE, char1_rect, 2)  # Highlight nhân vật được chọn
                    screen.blit(char1_button, char1_button_rect)
                    screen.blit(char1_img, char1_rect)
                    if selected_char == "monkey2":
                        pygame.draw.rect(screen, ORANGE, char2_rect, 2)
                    screen.blit(char2_button, char2_button_rect)
                    screen.blit(char2_img, char2_rect)
                    pygame.display.flip()
                elif char2_rect.collidepoint(x, y) or char2_button_rect.collidepoint(x,y):
                    selected_char = "monkey2"
                    # Redraw menu
                    screen.blit(background, (0, 0))
                    screen.blit(title1, title1.get_rect(center=(WIDTH//2, HEIGHT//4 - 30)))
                    screen.blit(title2, title2.get_rect(center=(WIDTH//2, HEIGHT//4 + 30)))
                    screen.blit(start_button, start_rect)
                    screen.blit(quit_button, quit_rect)
                    screen.blit(speaker_icon, speaker_rect)

                    # Vẽ lại phần chọn nhân vật
                    screen.blit(char_text, char_rect)
                    if selected_char == "monkey1":
                        pygame.draw.rect(screen, ORANGE, char1_rect, 2)  # Highlight nhân vật được chọn
                    screen.blit(char1_button, char1_button_rect)
                    screen.blit(char1_img, char1_rect)
                    if selected_char == "monkey2":
                        pygame.draw.rect(screen, ORANGE, char2_rect, 2)  # Highlight nhân vật được chọn
                    screen.blit(char2_button, char2_button_rect)
                    screen.blit(char2_img, char2_rect)
                    pygame.display.flip()

        # Cursor handling
        mouse_pos = pygame.mouse.get_pos()
        if start_rect.collidepoint(mouse_pos) or quit_rect.collidepoint(mouse_pos) or speaker_rect.collidepoint(mouse_pos) or char1_rect.collidepoint(mouse_pos) or char2_rect.collidepoint(mouse_pos) or char1_button_rect.collidepoint(mouse_pos) or char2_button_rect.collidepoint(mouse_pos):
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()


def show_game_over(screen, won, steps, min_steps, level, highscore):
    if won:
        background = pygame.image.load('assets/images/monkeyLaugh.png')  # ảnh khi thắng
    else:
        background = pygame.image.load('assets/images/monkeyCry.png')  # ảnh khi thua
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))

    font = pygame.font.Font(None, 50)
    if won:
        text = font.render('You Win!', True, GREEN)
    else:
        text = font.render('Game Over!', True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(text, text_rect)

    text_font = pygame.font.Font(None, 36)
    mid_x = WIDTH // 2
    mid_y = HEIGHT // 2
    line_gap = 40

    steps_text = text_font.render(f'Your steps: {steps}', True, BLUE)
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
                elif quit_rect.collidepoint(x, y):
                    return False

        mouse_pos = pygame.mouse.get_pos()
        if replay_rect.collidepoint(mouse_pos) or quit_rect.collidepoint(mouse_pos):
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)