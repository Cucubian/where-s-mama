import pygame
import sys
from collections import deque
from settings import *
from maze import generate_maze, draw_grid
from a_star import a_star

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('assets/images/monkey.png')
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))  # Thay đổi kích thước theo BLOCK_SIZE


    def move(self, dx, dy, grid):
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != 1:
            self.x = new_x
            self.y = new_y
            return True
        return False

    def draw(self, screen):
        # Vẽ nhân vật với hình ảnh đã tải
        screen.blit(self.image, (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE))


# Hàm BFS để tính số bước tối thiểu và kiểm tra tính khả thi của đường đi
def bfs(grid, start, end):
    queue = deque([start])
    visited = set()
    visited.add(start)
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return True  # Có đường đi
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return False  # Không có đường đi

# Hàm để tính toán số bước tối thiểu bằng thuật toán A*
def get_min_steps(grid, start, end):
    # Sử dụng A* hoặc BFS để tính số bước tối thiểu
    path = a_star(grid, start, end)
    return len(path)  # Trả về độ dài của đường đi ngắn nhất

def show_menu():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 74)
    title = font.render('Maze Runner', True, BLUE)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//4))
    
    font = pygame.font.Font(None, 36)
    start_button = font.render('Start Game', True, GREEN)
    quit_button = font.render('Quit', True, RED)
    
    screen.blit(start_button, (WIDTH//2 - start_button.get_width()//2, HEIGHT//2))
    screen.blit(quit_button, (WIDTH//2 - quit_button.get_width()//2, HEIGHT//2 + 50))

    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (WIDTH//2 - start_button.get_width()//2 <= x <= WIDTH//2 + start_button.get_width()//2 and
                    HEIGHT//2 <= y <= HEIGHT//2 + 40):
                    return True  # Start Game
                if (WIDTH//2 - quit_button.get_width()//2 <= x <= WIDTH//2 + quit_button.get_width()//2 and
                    HEIGHT//2 + 50 <= y <= HEIGHT//2 + 90):
                    pygame.quit()
                    sys.exit()

def show_game_over(won, steps, min_steps):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 74)
    if won:
        text = font.render('You Win!', True, (0, 255, 0))
    else:
        text = font.render('Game Over!', True, (255, 0, 0))
    
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4))
    
    font = pygame.font.Font(None, 36)
    steps_text = font.render(f'Steps: {steps}', True, BLUE)
    screen.blit(steps_text, (WIDTH // 2 - steps_text.get_width() // 2, HEIGHT // 2))
    
    # Hiển thị số bước tối thiểu
    min_steps_text = font.render(f'Min steps: {min_steps}', True, (255, 165, 0))
    screen.blit(min_steps_text, (WIDTH // 2 - min_steps_text.get_width() // 2, HEIGHT // 2 + 40))
    
    replay_button = font.render('Replay', True, GREEN)
    quit_button = font.render('Quit', True, RED)
    
    screen.blit(replay_button, (WIDTH//2 - replay_button.get_width()//2, HEIGHT//2 + 90))
    screen.blit(quit_button, (WIDTH//2 - quit_button.get_width()//2, HEIGHT//2 + 140))

    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (WIDTH//2 - replay_button.get_width()//2 <= x <= WIDTH//2 + replay_button.get_width()//2 and
                    HEIGHT//2 + 90 <= y <= HEIGHT//2 + 130):
                    return True  # Replay Game
                if (WIDTH//2 - quit_button.get_width()//2 <= x <= WIDTH//2 + quit_button.get_width()//2 and
                    HEIGHT//2 + 140 <= y <= HEIGHT//2 + 180):
                    pygame.quit()
                    sys.exit()  # Exit game


def main():
    pygame.init()
    global screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Runner - A* Algorithm")
    clock = pygame.time.Clock()

    # Hiển thị menu trước
    while True:
        if show_menu():
            grid = generate_maze()

            # Kiểm tra xem có đường đi từ điểm bắt đầu đến điểm kết thúc
            if not bfs(grid, START_POS, END_POS):
                font = pygame.font.Font(None, 74)
                text = font.render('Maze không khả dụng!', True, (255, 0, 0))
                screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
                pygame.display.flip()
                pygame.time.wait(2000)  # Dừng 2 giây để người chơi thấy thông báo
                continue  # Quay lại màn hình menu

            # Tính số bước tối thiểu từ điểm bắt đầu đến kết thúc
            min_steps = get_min_steps(grid, START_POS, END_POS)

            # Tạo đối tượng Player
            player = Player(START_POS[0], START_POS[1])
            steps = 0
            running = True
            while running:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            if player.move(-1, 0, grid):  # Chỉ di chuyển nếu có thể
                                steps += 1
                        elif event.key == pygame.K_RIGHT:
                            if player.move(1, 0, grid):  # Chỉ di chuyển nếu có thể
                                steps += 1
                        elif event.key == pygame.K_UP:
                            if player.move(0, -1, grid):  # Chỉ di chuyển nếu có thể
                                steps += 1
                        elif event.key == pygame.K_DOWN:
                            if player.move(0, 1, grid):  # Chỉ di chuyển nếu có thể
                                steps += 1



                # Hiển thị số bước tối thiểu và số bước hiện tại
                screen.fill(WHITE)
                draw_grid(screen, grid, [], START_POS, END_POS)
                player.draw(screen)  # Vẽ nhân vật

                # Hiển thị số bước ngắn nhất và số bước hiện tại
                font = pygame.font.Font(None, 36)
                min_steps_text = font.render(f'Min steps: {min_steps}', True, (255, 165, 0))
                steps_text = font.render(f'Steps: {steps}', True, BLUE)
                screen.blit(min_steps_text, (10, 10))
                screen.blit(steps_text, (10, 50))

                # Kiểm tra nếu nhân vật đến đích hoặc hết số bước tối thiểu
                if (player.x, player.y) == END_POS:
                    show_game_over(True, steps, min_steps)
                    running = False  # Kết thúc game
                elif steps >= min_steps:
                    show_game_over(False, steps, min_steps)
                    running = False  # Kết thúc game

                pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
