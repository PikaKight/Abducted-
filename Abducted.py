import pygame

import time

pygame.init()

screen = pygame.display.set_mode((1280,680)) 

pygame.display.set_caption("Abducted")

colr = (0,0,0)

recc = (255,255,255)

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
            if event.type == pygame.KEYDOWN:
               if event.key is pygame.K_s:
                   screen.fill(recc)
                   pygame.draw.rect(screen, colr,[465,350,350,100],7)
                   pygame.display.flip()             

intro()
gamestrt()
pygame.quit()   
