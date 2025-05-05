import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("assets/sounds/game.ogg")
        self.move_sound = pygame.mixer.Sound("assets/sounds/move.ogg")
        self.win_sound = pygame.mixer.Sound("assets/sounds/win.ogg")
        self.lose_sound = pygame.mixer.Sound("assets/sounds/lose.ogg")
        self.muted = False  # Start with sound enabled
        self.play_music()  # Ensure music starts playing on initialization

    def play_music(self):
        pygame.mixer.music.load("assets/sounds/game.ogg")  # Reload music to ensure it can restart
        pygame.mixer.music.play(-1)  # Loop music
        if self.muted:
            pygame.mixer.music.pause()  # Pause if muted

    def toggle_mute(self):
        self.muted = not self.muted
        if self.muted:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def play_move(self):
        if not self.muted:
            self.move_sound.play()

    def play_win(self):
        if not self.muted:
            self.win_sound.play()

    def play_lose(self):
        if not self.muted:
            self.lose_sound.play()