#pre_init(frequency=22050, size=-16, channels=2, buffersize=4096)

import pygame
import os

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

try:
    pygame.mixer.music.load(os.path.join('resource', 'an-turr.ogg'))
    fail = pygame.mixer.Sound(os.path.join('resource','fail.wav'))
    jump = pygame.mixer.Sound(os.path.join('resource', 'jump.wav'))

except:
    raise(UserWarning, '没有找到相应的文件')

pygame.mixer.music.play(-1)
screen = pygame.display.set_mode((640, 480))

background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
background = background.convert()
screen.blit(background, (0, 0))
clock = pygame.time.Clock()
mainLoop = True
FPS = 30
while mainLoop:
    milliseconds = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainLoop = False
            if event.key == pygame.K_a:
                print('Fail Key  pressed')
                fail.play()
            if event.key ==pygame.K_b:
                print('Jump key pressed')
                jump.play()
    pygame.display.set_caption("FPS: {:.2f} Press [a] or [b] to play sound effects".format(clock.get_fps()))
    pygame.display.flip()


pygame.quit()

