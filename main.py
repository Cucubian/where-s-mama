import pygame
from settings import WIDTH, HEIGHT
from game.game_loop import run_game

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Runner - A* Algorithm")
    run_game(screen)

if __name__ == "__main__":
    main()
