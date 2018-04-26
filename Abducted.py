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
     
def gamestrt():#changes the screen to the game beginnin              
    start = True
    use = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                while use:
                    mouse = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()
                    print (click)
                    if 470 + 345 > mouse[0] > 470 and 355 + 95 > mouse[1] > 355 :
                        if click[0] == 1:
                            print ("Hello")
                            screen.fill(colr)
                            pygame.draw.rect(screen, recc,[100,50,335,400],5)
                            pygame.draw.rect(screen, recc,[470,50,335,400],5)
                            pygame.draw.rect(screen, recc,[840,50,335,400],5)
                            pygame.display.flip()
                            use = False

def character():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()
                    if 105 + 330 > mouse[0] > 105 and 55+395>mouse[1] > 55 :
                        if click == 1:
                            print ("works")
        

                        
                      
intro()
gamestrt()
character()
pygame.quit()   
