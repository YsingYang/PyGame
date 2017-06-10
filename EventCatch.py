import pygame
from collections import deque
pygame.init()
screen = pygame.display.set_mode((640, 480))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
background = background.convert()

font = pygame.font.SysFont('arial', 16)#16刚好可以被480整除
fontHeight = font.get_linesize()#这个有什么用?
print(fontHeight)
maxSize = screen.get_height() // fontHeight
eventList = deque()

while True:
    event = pygame.event.wait()#等待一个事件触发
    eventList.append(str(event))
    if len(eventList) > maxSize:
        eventList.popleft()
    if event.type ==  pygame.QUIT:
        exit()

    #开始渲染
    screen.blit(background, (0, 0))
    height = 0
    for text in reversed(eventList):
        screen.blit(font.render(text, True, (128, 0, 0)), (0, height))
        height += fontHeight
    pygame.display.update()




