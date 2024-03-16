import pygame
import time
pygame.init()
print(pygame.display.Info())

w = pygame.display.Info().current_w
h = pygame.display.Info().current_h
size = [w, h]

screen = pygame.display.set_mode(size)
fon = pygame.image.load('фон.jpg').convert()
fon = pygame.transform.scale(fon, (1920, 1200))
clock = pygame.time.Clock()
running = True

dino = pygame.image.load('Динозавр.png').convert_alpha()
dino = pygame.transform.scale(dino, (200, 180))
dino_x = 450
dino_y = 400
dino_jump = False
dino_jump_height = 12.5
speed = 10

pablo_x = 1920
pablo_y = 400
pablo_model = pygame.image.load('Кактус.png').convert()
pablo_model  = pygame.transform.scale(pablo_model, (200, 180))
print(pablo_model)
while running:
    screen.fill((255, 255, 255))
    screen.blit(fon, (0, 0))
    screen.blit(dino, (dino_x, dino_y))
    screen.blit(pablo_model, (pablo_x, pablo_y))

    dino_rect = pygame.Rect(dino_x, dino_y, 160, 180)
    pablo_rect = pygame.Rect(pablo_x, pablo_y, 160, 180)
    
    if dino_rect.colliderect(pablo_rect):
        running = False

    pablo_x -= speed
    if pablo_x < -200:
        pablo_x = 1920
        speed += 0.1

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
            dino_jump_height -= 1
        else:
            dino_jump = False
            dino_jump_height = 12.5
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(30)
dino = pygame.image.load('Динозавр.png').convert_alpha()
pygame.quit()