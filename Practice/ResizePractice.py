#想做一个窗口的缩放, 同时保持对image的缩放
import os
import pygame

pygame.init()
img = pygame.image.load(os.path.join('../resource', 'war3.jpg'))
screen = pygame.display.set_mode((img.get_size()), pygame.RESIZABLE, 32)
img = img.convert()
#background = pygame.Surface(screen.get_size()).convert()
#pygame.transform.scale(img, screen.get_size(), background)
SCREEN_SIZE = img.get_size()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.VIDEORESIZE:
            SCREEN_SIZE = event.size #取出变化的event的size
            screen = pygame.display.set_mode((SCREEN_SIZE), pygame.RESIZABLE, 32)

    pygame.transform.scale(img, SCREEN_SIZE, screen) #这样直接写应该只是简单的将img改变成screen的大小, 而不是对原图img进行改变, 如果是对原图进行改变, 那么对不断得伸缩, 会有损
    #background = pygame.transform.scale(background, SCREEN_SIZE)
    #screen.blit(background, (0, 0))
    pygame.display.flip()
