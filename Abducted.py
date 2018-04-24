import pygame

import time

pygame.init()

screen = pygame.display.set_mode((1280,680)) 

pygame.display.set_caption("Abducted")

colr = (0,0,0) #Background colour

recc = (255,255,255) #box colour

timer = pygame.time.Clock()

def intro(): #this is for the title screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
    screen.fill(colr)
    pygame.draw.rect(screen,recc,[465,350,350,100],5)
    pygame.display.flip()

def button(msg, x,y,w,h,):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:

def gamestrt():#changes the screen to the game beginnin              
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.MOUSEBUTTONDOWN:#interagative button
                mouse = pygame.mouse.get_pos()
                if  470+345 >mouse[0] >470  and 359+95 > mouse[1] > 359:#The range of which the mouse clicks work
                    screen.fill(colr)
                    pygame.draw.rect(screen, recc,[100,50,335,400],5)
                    pygame.draw.rect(screen, recc,[470,50,335,400],5)
                    pygame.draw.rect(screen, recc,[840,50,335,400],5)
                    pygame.display.flip()

def character():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if event.button == 1:
                        if 105 + 330 > mouse[0] and 55+395>mouse[1] :
                            print ("works")
                        
                      
intro()
gamestrt()
character()
pygame.quit()   
