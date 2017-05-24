import pygame
import random

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
x = random.randint(50, 400)
y = random.randint(50, 600)
x_speed = 3
y_speed = 3
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(10)
    pygame.draw.rect(screen, [255, 255, 255], [x - 35, y - 35, x + 35, y + 35], 0)
    x += x_speed
    y += y_speed
    if x > screen.get_width() - 30 or x < 30:
        x_speed = -x_speed
    if y > screen.get_height() - 30 or y < 30:
        y_speed = -y_speed
    pygame.draw.circle(screen, [255, 200, 0], [x, y], 30, 0)
    pygame.display.flip()

pygame.quit()
