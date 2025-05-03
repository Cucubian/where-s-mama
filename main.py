import pygame
from settings import WIDTH, HEIGHT
from game.game_loop import run_game

def main():
    pygame.init()
    icon = pygame.image.load('assets/images/monkey.png')  # Đường dẫn đến icon của bạn
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Where's Mama - Little Monkey")
    run_game(screen)

if __name__ == "__main__":
    main()
