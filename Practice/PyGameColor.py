import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

allColor = pygame.Surface((4096, 4096), depth = 24)#24的深度?

for r in range(256):
    x = (r & 15) * 256
    y = (r >> 4) * 256
    for g in range(256):
        for b in range(256):
            allColor.set_at((x+g, y + b), (r, g, b))

pygame.image.save(allColor, 'allcolrs.png')
