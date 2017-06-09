import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

font = pygame.font.SysFont('arial', 16)#16刚好可以被480整除
eventList = []
