import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("assets/sounds/game.ogg")
        self.move_sound = pygame.mixer.Sound("assets/sounds/move.ogg")
        self.win_sound = pygame.mixer.Sound("assets/sounds/win.ogg")
        self.lose_sound = pygame.mixer.Sound("assets/sounds/lose.ogg")

    def play_music(self):
        pygame.mixer.music.play(-1)  # Lặp vô hạn

    def stop_music(self):
        pygame.mixer.music.stop()

    def play_move(self):
        self.move_sound.play()

    def play_win(self):
        self.win_sound.play()

    def play_lose(self):
        self.lose_sound.play()
