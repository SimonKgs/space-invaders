import pygame
from pygame import mixer


class Bullet:
    def __init__(self):
        self.bullet_img = pygame.image.load("images/bala_g.png")
        self.bullet_x = 0
        self.bullet_y = 536
        self.y_movement = 1
        self.visible = False

    def fire(self, player_x, player_y):
        if not self.visible:
            bullet_sound = mixer.Sound('sounds/disparo.mp3')
            bullet_sound.set_volume(0.2)
            bullet_sound.play()
            self.bullet_x = player_x + 20
            self.bullet_y = player_y
            self.visible = True

    def update(self):
        if self.visible:
            self.bullet_y -= self.y_movement
            if self.bullet_y <= 0:
                self.visible = False

    def draw(self, game_screen):
        if self.visible:
            game_screen.blit(self.bullet_img, (self.bullet_x, self.bullet_y))

    def reset(self):
        self.bullet_x = 0
        self.bullet_y = -100
        self.visible = False
