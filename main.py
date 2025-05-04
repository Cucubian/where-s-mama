import pygame
from settings import WIDTH, HEIGHT
from game.game_loop import run_game

def main():
    pygame.init()
    icon = pygame.image.load('assets/images/monkey.png')
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("April 30: Road to Reunification")
    run_game(screen)

if __name__ == "__main__":
    main()
