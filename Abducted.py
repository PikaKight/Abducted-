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
    click = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            for i in range(1):
                if event.type == pygame.MOUSEBUTTONDOWN:#interagative button
                    mouse = pygame.mouse.get_pos()
                    if (mouse[0] > 470 and mouse[0] < 810) and (mouse[1] > 355 and mouse[1] < 445):#The range of which the mouse clicks work
                        screen.fill(colr)
                        pygame.draw.rect(screen, recc,[100,50,335,400],5)
                        pygame.draw.rect(screen, recc,[470,50,335,400],5)
                        pygame.draw.rect(screen, recc,[840,50,335,400],5)
                        pygame.display.flip()

def Choose():# To let player choose a character
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.MOUSEBUTTONDOWN:#interagative button to choose a character
                mouse = pygame.mouse.get_pos()
                if (mouse[0] > 105 and mouse[0] < 430) and (mouse[1] > 55 and mouse[1] < 445):
                    screen.fill(colr)
                    pygame.draw.rect(screen, recc, [50, 50, 500, 500, 7])
                    pygame.display.flip()
                elif (mouse[0] > 475 and mouse[0] < 800) and (mouse[1] > 55 and mouse[1] < 445):
                    screen.fill(colr)
                    pygame.draw.rect(screen, recc, [50, 50, 500, 500, 7])
                    pygame.display.flip()
                elif (mouse[0] > 845 and mouse[0] < 1170) and (mouse[1] > 55 and mouse[1] < 445):
                    screen.fill(colr)
                    pygame.draw.rect(screen, recc, [50, 50, 500, 500, 7])
                    pygame.display.flip()
                else:
                    break
intro()
gamestrt()
Choose()
pygame.quit()   
