# === settings.py ===
CELL_SIZE = 40
GRID_WIDTH = 15
GRID_HEIGHT = 15
WIDTH = CELL_SIZE * GRID_WIDTH
HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 60
TOP_BAR_HEIGHT = 50
HEIGHT = TOP_BAR_HEIGHT + GRID_HEIGHT * CELL_SIZE

# START_POS = (0, 0)
# END_POS = (GRID_WIDTH - 1, GRID_HEIGHT - 1)
CURRENT_LEVEL = 1  # Bắt đầu từ level 1
OBSTACLE_RATIO = 0.2  # Tỷ lệ chướng ngại vật cố định
TIME_LIMIT = 120  # Thời gian giới hạn cố định (2 phút)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 120, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

BLOCK_SIZE = 40
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Font settings
FONT_PATH = "assets/fonts/Myfont.ttf"

CHARACTER_DATA = {
    "monkey1": {"name": "Monkey 1", "image": "assets/images/monkey.png"},
    "monkey2": {"name": "Monkey 2", "image": "assets/images/monkey2.png"}# Thay đổi đường dẫn nếu cần
}
DEFAULT_CHARACTER = "monkey1"  # Nhân vật mặc định

def get_font(size):
    import pygame  # Đảm bảo import khi dùng
    return pygame.font.Font(FONT_PATH, size)