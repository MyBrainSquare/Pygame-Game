import pygame, sys
import os

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Epic Game")

x = 50
y = 440
width = 40
height = 60
vel = 10

isJump = False
jumpCount = 10

run = True

while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x != 0 or keys[pygame.K_a] and x != 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x != 460 or keys[pygame.K_d] and x != 460:
        x += vel
    if not(isJump):
        if keys[pygame.K_UP] and y != 0 or keys[pygame.K_w] and y != 0:
            y -= vel
        if keys[pygame.K_DOWN] and y != 440 or keys[pygame.K_s] and y != 440:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else: 
            isJump = False
            jumpCount = 10

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

    pygame.display.flip()