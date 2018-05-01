import pygame

import time

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1280,680)) 

pygame.display.set_caption("Abducted")

colr = (0,0,0) #Background colour

recc = (255,255,255) #box colour
Hrecc = (50, 255, 0)

timer = pygame.time.Clock()

def textObj(msg, text):
    textcolour =  textfont.render(msg, 1,  recc)
    return textcolour, textcolour.get_rect()

def text(msg, x, y, size):
    global textfont
    textfont = pygame.font.SysFont('forte_o', size)
    textscreen, textrecc = textObj(msg, textfont)
    textrecc.center = (x , y)
    screen.blit(textscreen, textrecc)
    
def intro(): #this is for the title screen
    screen.fill(colr)
    pygame.draw.rect(screen,(50,255,0),[465,350,350,100])
    text("Start", 630, 400, 50)
    pygame.display.flip()
    start = True
    while start:
        mouse = pygame.mouse.get_pos()
        if (mouse[0] > 470 and mouse[0] < 810) and (mouse[1] > 355 and mouse[1] < 445):
            pygame.draw.rect(screen, Hrecc, [465,350,350,100], 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.MOUSEBUTTONDOWN:#interagative button
                click =  pygame.mouse.get_pressed()
                if (mouse[0] > 470 and mouse[0] < 810) and (mouse[1] > 355 and mouse[1] < 445):#The range of which the mouse clicks work
                        print ("Hello")
                        screen.fill(colr)
                        pygame.draw.rect(screen, recc,[100,50,335,400],5)
                        pygame.draw.rect(screen, recc,[470,50,335,400],5)
                        pygame.draw.rect(screen, recc,[840,50,335,400],5)
                        pygame.display.flip()
        

intro()
pygame.quit()   
