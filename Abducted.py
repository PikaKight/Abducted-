import pygame

import time

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1280,680)) 

pygame.display.set_caption("Abducted")

colr = (0,0,0) #Background colour

recc = (255,255,255) #box colour

sc = (100, 250 , 0)

hc = (100, 255, 150)

time = pygame.time.Clock()

def textObj(msg, text):
    textcolour =  textfont.render(msg, 1,  recc)
    return textcolour, textcolour.get_rect()

def Startaction():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               start = False
            if event.type == pygame.MOUSEBUTTONDOWN:#interagative button
                if (mouse[0] > 470 and mouse[0] < 810) and (mouse[1] > 355 and mouse[1] < 445):#The range of which the mouse clicks 
                    print ("Hello")
                    screen.fill(colr)
                    pygame.draw.rect(screen, recc,[100,50,335,400],5)
                    pygame.draw.rect(screen, recc,[470,50,335,400],5)
                    pygame.draw.rect(screen, recc,[840,50,335,400],5)
                    pygame.display.flip()
                    

def button(msg, x, y, w, h, sc, hc, a):
    global mouse
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, hc,(x,y,w,h))
        if click[0] == 1 and a == 1:
                Startaction()
    else:
        pygame.draw.rect(screen, sc, (x,y,w,h))

        
    global textfont
    textfont = pygame.font.SysFont('forte_o', 50)
    textscreen, textrecc = textObj(msg, textfont)
    textrecc.center = ((x+(w/2)) , (y+(h/2)))
    screen.blit(textscreen, textrecc)

    
def intro(): #this is for the title
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False

        screen.fill(colr)
        button("Start", 465,350,350,100, sc, hc, 1)
        pygame.display.flip()
        pygame.display.update()
        time.tick(15)    
                        
        

intro()
pygame.quit()   
