import pygame
import random


class Enemy:
    def __init__(self):
        self.enemy_img = pygame.image.load("images/enemy1.png")
        self.enemy_x = random.randint(0, 736)
        self.enemy_y = 0
        self.x_movement = 0.5
        self.y_movement = 0.03

    def update(self):
        self.enemy_x += self.x_movement
        self.enemy_y += self.y_movement
        self.keep_on_screen()

    def keep_on_screen(self):
        if self.enemy_x <= 0:
            self.x_movement = 0.5
            self.enemy_y += self.y_movement
        if self.enemy_x >= 736:
            self.x_movement = -0.5
            self.enemy_y += self.y_movement
        if self.enemy_y > 536:
            self.reset()

    def reset(self):
        self.enemy_x = random.randint(0, 736)
        self.enemy_y = 0

    def draw(self, game_screen):
        game_screen.blit(self.enemy_img, (self.enemy_x, self.enemy_y))