import pygame

import time

pygame.init()

screen = pygame.display.set_mode((1280,680)) 

pygame.display.set_caption("Abducted")

colr = (0,0,0) #Background colour

recc = (255,255,255) #box colour

def intro(): #this is for the title screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
    screen.fill(colr)
    pygame.draw.rect(screen,recc,[465,350,350,100],5)
    pygame.display.flip()

def gamestrt():#changes the screen to the game beginnin              
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if (mouse[0] > 470 and mouse[0] < 810) and (mouse[1] > 355 and mouse[1] < 445):
                    screen.fill(colr)
                    pygame.draw.rect(screen, recc,[100,50,335,400],5)
                    pygame.draw.rect(screen, recc,[470,50,335,400],5)
                    pygame.draw.rect(screen, recc,[840,50,335,400],5)
                    pygame.display.flip()

intro()
gamestrt()
pygame.quit()   
