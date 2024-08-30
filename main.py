import pygame
from pygame import mixer

from Bullet import Bullet
from Enemy import Enemy
from Player import Player

# Initialize PyGame
pygame.init()

# Create the screen
game_screen = pygame.display.set_mode((800, 600))

# Image and Title
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/ovni.png")
pygame.display.set_icon(icon)

# music
mixer.music.load('sounds/MusicaFondo.mp3')
mixer.music.set_volume(0.3)

# Background image
background = pygame.image.load('images/Fondo.jpg')
mixer.music.play(-1)

# Points
points = 0


def is_collision(bullet_coll, enemy):
    bullet_width, bullet_height = bullet_coll.bullet_img.get_size()
    enemy_width, enemy_height = enemy.enemy_img.get_size()

    if (bullet_coll.bullet_x < enemy.enemy_x + enemy_width and
            bullet_coll.bullet_x + bullet_width > enemy.enemy_x and
            bullet_coll.bullet_y < enemy.enemy_y + enemy_height and
            bullet_coll.bullet_y + bullet_height > enemy.enemy_y):
        return True
    return False


def is_dead(player_coll, enemy):
    player_width, player_height = player_coll.player_img.get_size()
    enemy_width, enemy_height = enemy.enemy_img.get_size()

    if (player_coll.player_x < enemy.enemy_x + enemy_width and
            player_coll.player_x + player_width > enemy.enemy_x and
            player_coll.player_y < enemy.enemy_y + enemy_height and
            player_coll.player_y + player_height > enemy.enemy_y):
        return True
    return False


def draw_text(text, font_size, color, position):
    font_draw = pygame.font.SysFont(None, font_size)
    text_surface = font_draw.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    game_screen.blit(text_surface, text_rect)


def restart_game():
    global player, bullet, enemies, points, running

    # Reset variables
    player = Player()
    bullet = Bullet()
    enemies = [Enemy()]
    points = 0
    # start the loop again
    running = True


def game_over_screen(list_enemies):
    global running
    game_screen.blit(background, (0, 0))
    draw_text("GAME OVER", 72, (255, 0, 0), (400, 250))
    draw_text(f"SCORE: {points}", 48, (255, 255, 255), (400, 330))
    draw_text("Press R to Restart or Q to Quit", 36, (255, 255, 255), (400, 400))
    pygame.display.update()

    # Stop the enemies to avoid new collisions
    for enemy in list_enemies:
        enemy.x_movement = 0
        enemy.y_movement = 0

    # To force user input
    while True:
        for final_event in pygame.event.get():
            if final_event.type == pygame.QUIT:
                running = False
                return

            if final_event.type == pygame.KEYDOWN:
                if final_event.key == pygame.K_q:
                    running = False
                    return
                elif final_event.key == pygame.K_r:
                    restart_game()
                    return
        pygame.time.delay(500)


# Initialize game objects
player = Player()
bullet = Bullet()
enemies = [Enemy()]

# Game Loop
running = True
while running:
    game_screen.blit(background, (0, 0))

    keys = pygame.key.get_pressed()
    player.move(keys)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.fire(player.player_x, player.player_y)

    # Update and draw game objects
    player.draw(game_screen=game_screen)
    player.move(keys)

    for enemy_instance in enemies:
        enemy_instance.update()
        enemy_instance.draw(game_screen=game_screen)

    bullet.update()
    bullet.draw(game_screen=game_screen)

    # Check for collision
    for enemy_instance in enemies[:]:
        if is_collision(bullet, enemy_instance):
            collision_sound = mixer.Sound('sounds/Golpe.mp3')
            collision_sound.set_volume(0.3)
            collision_sound.play()
            bullet.reset()
            enemy_instance.reset()
            points += 1
            # add new enemies
            if len(enemies) < 8:
                bullet.y_movement += 0.1
                player.y_movement += 0.5
                player.x_movement += 1

                new_enemy = Enemy()
                enemies.append(new_enemy)
                for enemy_x in enemies:
                    enemy_x.y_movement += 0.03
                    enemy_x.x_movement += 0.05
                break

        if is_dead(player, enemy_instance):
            # Display points
            game_over_screen(enemies)

    # Display points
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Points: {points}", True, (255, 255, 255))
    game_screen.blit(text, (10, 10))

    pygame.display.update()
