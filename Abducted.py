import pygame

import time

pygame.init()

screen = pygame.display.set_mode((1280,680))

pygame.display.set_caption("Abducted")

colr = (0,0,0)

recc = (255,255,255)

def intro():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               start = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print (mouse)
        screen.fill(colr)
        pygame.draw.rect(screen,recc,[360,350,500,200],5)
        pygame.display.flip()

intro()
pygame.quit()   
