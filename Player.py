import pygame


class Player:
    def __init__(self):
        self.player_img = pygame.image.load("images/space-ship.png")
        self.player_x = 368
        self.player_y = 536
        self.x_movement = 0
        self.y_movement = 0
        self.speed = 1

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x_movement = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.x_movement = self.speed
        else:
            self.x_movement = 0

        if keys[pygame.K_UP]:
            self.y_movement = -self.speed
        elif keys[pygame.K_DOWN]:
            self.y_movement = self.speed
        else:
            self.y_movement = 0

        self.player_x += self.x_movement
        self.player_y += self.y_movement

        # Keep player on the screen
        if self.player_x < 0:
            self.player_x = 0
        if self.player_x > 736:
            self.player_x = 736
        if self.player_y < 0:
            self.player_y = 0
        if self.player_y > 536:
            self.player_y = 536

    def draw(self, game_screen):
        game_screen.blit(self.player_img, (self.player_x, self.player_y))