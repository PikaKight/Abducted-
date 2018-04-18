import pygame

import time

pygame.init()

screen = pygame.display.set_mode((1280,680),pygame.RESIZABLE)

pygame.display.set_caption("Abducted")

colr = (0,0,0)

recc = (255,255,255)

def intro():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               start = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print(mouse)
                #if mouse[0] > 

        screen.fill(colr)
        pygame.draw.rect(screen,recc,[360,350,500,200],5)
        pygame.display.flip()

intro()
pygame.quit()   
