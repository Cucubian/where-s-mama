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
# Đường dẫn đến file lưu high score
HIGHSCORE_FILE = os.path.join('assets', 'highscore.txt')
def load_highscore():
    """Đọc high score từ file, nếu không có file thì trả về 0 (giá trị mặc định)"""
    try:
        with open(HIGHSCORE_FILE, 'r') as file:
            score = int(file.read().strip())
            return max(0, score)  # Đảm bảo không âm
    except (FileNotFoundError, ValueError):
        return 0  # Giá trị mặc định nếu không có file hoặc file lỗi
def save_highscore(highscore):
    """Ghi high score vào file"""
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
    print(f"Min steps calculated (before adjustment): {len(path) if path else 'No path'}")  # Debug
    if path:
        print(f"Path: {path}")  # In đường đi để debug
        # Trả về số bước (số ô - 1), không tính ô bắt đầu
        return len(path) - 1 if len(path) > 1 else 0, path
    return 9999, path  # Trả về cả min_steps và path
def run_game(screen):
    clock = pygame.time.Clock()
    global CURRENT_LEVEL
    CURRENT_LEVEL = 1  # Bắt đầu từ level 1
    highscore = load_highscore()  # Đọc high score khi bắt đầu trò chơi (số màn cao nhất)
    running_menu = True
    while running_menu:
        if show_menu(screen, CURRENT_LEVEL):
            playing = True
            while playing:
                # Sinh maze mới mỗi khi bắt đầu một màn chơi
                while True:
                    start_pos, end_pos = get_random_positions()
                    grid = generate_maze(start_pos, end_pos)
                    if bfs(grid, start_pos, end_pos):
                        break
                min_steps, path = get_min_steps(grid, start_pos, end_pos)
                if not path:
                    continue  # Tạo lại maze nếu không tìm được đường đi bằng A*
                player = Player(*start_pos)
                visited_tiles = set()
                steps = 0
                game_running = True
                start_time = time.time()
                time_limit = TIME_LIMIT
                while game_running:
                    clock.tick(FPS)
                    # Cập nhật thời gian còn lại
                    current_time = time.time()
                    elapsed_time = current_time - start_time
                    remaining_time = max(0, int(time_limit - elapsed_time))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()  # Thoát hoàn toàn chương trình khi bấm nút đóng
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
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if quit_rect.collidepoint(event.pos):
                                game_running = False  # Dừng màn chơi hiện tại
                                playing = False # Dừng vòng lặp chơi, quay về menu
                                CURRENT_LEVEL = 1 # Reset về level 1
                                break # Thoát khỏi vòng lặp sự kiện

                    # Xóa màn hình trước khi vẽ lại
                    screen.fill(WHITE)
                    # Vẽ thanh thông tin trên cùng (50px)
                    pygame.draw.rect(screen, (230, 230, 230), (0, 0, WIDTH, 50))  # Màu xám rất nhạt
                    font = pygame.font.Font(None, 24)  # Font nhỏ hơn để vừa với thanh
                    screen.blit(font.render(f'Level: {CURRENT_LEVEL}', True, PURPLE), (10, 10))
                    screen.blit(font.render(f'Min steps: {min_steps}', True, ORANGE), (90, 10))
                    screen.blit(font.render(f'Steps: {steps}', True, BLUE), (210, 10))
                    screen.blit(font.render(f'Time left: {remaining_time}s', True, RED), (300, 10))

                    # Vẽ nút Quit
                    quit_text = font.render('Quit', True, RED)
                    quit_rect = quit_text.get_rect(topleft=(WIDTH - 70, 10))  # Điều chỉnh vị trí nếu cần
                    screen.blit(quit_text, quit_rect)

                    # Vẽ maze (phần còn lại của màn hình) dưới thanh thông tin
                    draw_grid(screen, grid, [], start_pos, end_pos, visited_tiles)
                    player.draw(screen)

                    # Kiểm tra khi người chơi thắng
                    if (player.x, player.y) == end_pos:
                        if CURRENT_LEVEL > highscore:  # Cập nhật high score nếu đạt level cao hơn
                            highscore = CURRENT_LEVEL
                            save_highscore(highscore)
                        CURRENT_LEVEL += 1  # Tăng level sau khi cập nhật highscore
                        if show_game_over(screen, True, steps, min_steps, CURRENT_LEVEL, highscore):
                            game_running = False
                        else:
                            pygame.quit()
                            sys.exit()  # Thoát nếu người chơi chọn Quit từ game over
                    # Kiểm tra khi người chơi thua (vượt quá số bước tối thiểu)
                    elif steps >= min_steps:
                        CURRENT_LEVEL = 1  # Reset về level 1 khi thua
                        if show_game_over(screen, False, steps, min_steps, CURRENT_LEVEL, highscore):
                            game_running = False
                        else:
                            pygame.quit()
                            sys.exit()  # Thoát nếu người chơi chọn Quit từ game over
                    # Kiểm tra khi hết thời gian
                    elif elapsed_time >= time_limit:
                        CURRENT_LEVEL = 1  # Reset về level 1 khi hết thời gian
                        if show_game_over(screen, False, steps, min_steps, CURRENT_LEVEL, highscore):
                            game_running = False
                        else:
                            pygame.quit()
                            sys.exit()  # Thoát nếu người chơi chọn Quit từ game over

                    pygame.display.flip()  # Cập nhật màn hình
                # Khi playing là False (do bấm Quit), vòng lặp while playing kết thúc
                # Vòng lặp while running_menu sẽ gọi lại show_menu
        else:
            running_menu = False # Thoát khỏi vòng lặp menu nếu người chơi chọn Quit ở menu chính