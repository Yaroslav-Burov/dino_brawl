import pygame
import time
import random

pygame.init()

w = pygame.display.Info().current_w
h = pygame.display.Info().current_h
rand = random.randint(0, 2)
score = 0
hp = 3
size = [w, h]

screen = pygame.display.set_mode(size)
fon = pygame.image.load('background.jpg').convert()
fon = pygame.transform.scale(fon, (1920, 1200))
clock = pygame.time.Clock()
running = True

dino = pygame.image.load('Dinosaur.png').convert_alpha()
dino = pygame.transform.scale(dino, (200, 180))
dino_x = 450
dino_y = 800
speed = 10

dino_jump = False
dino_jump_height = 12.5

mini_pablo_x = w
mini_pablo_y = h - 210
mini_pablo_w = 100
mini_pablo_h = 90
mini_pablo_model = pygame.image.load('Cactus.png').convert()
mini_pablo_model = pygame.transform.scale(mini_pablo_model, (mini_pablo_w, mini_pablo_h))

pablo_x = w + 50
pablo_y = h - 300
pablo_w = 200
pablo_h = 180
pablo_model = pygame.image.load('Cactus.png').convert()
pablo_model = pygame.transform.scale(pablo_model, (pablo_w, pablo_h))


def collision():
    global dino_rect, dino_x, dino_y, pablo_rect, pablo_x, pablo_y, running, mini_pablo_rect, mini_pablo_x, mini_pablo_y, pablo_w, pablo_h, mini_pablo_w, hp
    dino_rect = pygame.Rect(dino_x, dino_y, 160, 180)
    pablo_rect = pygame.Rect(pablo_x, pablo_y, pablo_w - 100, pablo_h - 40)
    mini_pablo_rect = mini_pablo_rect = pygame.Rect(mini_pablo_x, mini_pablo_y, mini_pablo_w - 50, mini_pablo_h - 20)

    if dino_rect.colliderect(pablo_rect):
        hp -= 1
        pablo_x = 2 * h - 300
    if dino_rect.colliderect(mini_pablo_rect):
        hp -= 1
        mini_pablo_x = 2 * h


def pablo():
    global pablo_x, mini_pablo_x, speed, score, rand, w
    if rand == 0:
        pablo_x -= speed
    if pablo_x < -200:
        rand = random.randint(0, 2)
        pablo_x = w + 50
        score += 1
        speed += 0.1

    if rand == 1:
        mini_pablo_x -= speed
    if mini_pablo_x < -200:
        rand = random.randint(0, 2)
        mini_pablo_x = w
        score += 1
        speed += 0.1

    if rand == 2:
        mini_pablo_x -= speed
        pablo_x -= speed
    if mini_pablo_x < -200:
        mini_pablo_x = w
        pablo_x = w + 50
        score += 1
        speed += 0.1
        rand = random.randint(0, 2)

    if rand == 3:
        mini_pablo_x


def jump():
    global dino_jump, dino_jump_height, dino_y
    keys = pygame.key.get_pressed()
    if not dino_jump:
        if keys[pygame.K_SPACE]:
            dino_jump = True
    else:
        if dino_jump_height >= -12.5:
            if dino_jump_height > 0:
                dino_y -= (dino_jump_height ** 2) / 2
            else:
                dino_y += (dino_jump_height ** 2) / 2
            dino_jump_height -= 0.5
        else:
            dino_jump = False
            dino_jump_height = 12.5


def calc(a, b):
    return a + b


if __name__ == '__main__':
    while running:
        screen.blit(fon, (0, 0))
        screen.blit(dino, (dino_x, dino_y))
        screen.blit(pablo_model, (pablo_x, pablo_y))
        screen.blit(mini_pablo_model, (mini_pablo_x, mini_pablo_y))

        collision()
        pablo()
        jump()

        if hp == 0:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        clock.tick(30)
        print(score)
    dino = pygame.image.load('Dinosaur.png').convert_alpha()
    pygame.quit()
