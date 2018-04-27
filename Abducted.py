import pygame

import time

pygame.init()

screen = pygame.display.set_mode((1280,680)) 

pygame.display.set_caption("Abducted")

colr = (0,0,0) #Background colour

recc = (255,255,255) #box colour

timer = pygame.time.Clock()

def button(x, y, w, h, action = None): #creates a button and their effects 
    for event in pygame.event.get():
        use = True
        while use:
                if x + w > mouse[0] > x  and y + h > mouse[1] > y:
                    if action != None:
                        if action == "Start":
                            gamestrt()
                        if action == "ChrC":
                            charcter()
        
def intro(): #this is for the title screen
    start = True
    while start:
        screen.fill(colr)
        pygame.draw.rect(screen,recc,[465,350,350,100],5)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.evnt.MOUSEBUTTONDOWN:
                button(465,350,350,100, "Start")
                
        
     
def gamestrt(): #changes the screen to the game beginnin 
        print ("Hello")
        screen.fill(colr)
        pygame.draw.rect(screen, recc,[100,50,335,400],5)
        pygame.draw.rect(screen, recc,[470,50,335,400],5)
        pygame.draw.rect(screen, recc,[840,50,335,400],5)
        pygame.display.flip()
        use = False

def character():
        print ("works")
        use = False 

                        
                      
intro()
pygame.quit()   
