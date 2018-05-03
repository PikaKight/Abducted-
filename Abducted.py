import pygame

import time

pygame.init()

screen = pygame.display.set_mode((1280,680)) 

pygame.display.set_caption("Abducted")

colr = (0,0,0) #Background colour

recc = (255,255,255) #box colour

sc = (100, 250 , 0) #start button colour 

hc = (100, 255, 150) #highlight colour

timer = pygame.time.Clock()

def textObj(msg, text):
    textcolour =  textfont.render(msg, 1,  recc)
    return textcolour, textcolour.get_rect()

def Cchoice():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP1:
                    pygame.draw.rect(screen, hc,[100,50,335,400],5)
                    pygame.display.update()
                    timer.tick(10)
                    pygame.time.delay(1000)
                    screen.fill(colr)
                    pygame.display.update()
                    timer.tick(10)
                    start = False

                if event.key == pygame.K_KP2:
                    pygame.draw.rect(screen, hc, [470,50,335,400], 5)
                    pygame.display.update()
                    timer.tick(10)
                    pygame.time.delay(1000)
                    screen.fill(colr)
                    pygame.display.update()
                    timer.tick(10)
                    start = False
                    
                if event.key == pygame.K_KP3:
                    pygame.draw.rect(screen, hc,[840,50,335,400],5)
                    pygame.display.update()
                    timer.tick(10)
                    pygame.time.delay(1000)
                    screen.fill(colr)
                    pygame.display.update()
                    timer.tick(10)
                    start = False
                    
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
                    text("Don't click the Screen! Choose a character using num pad 1, 2 or 3", 50,500,1080,150, 50)
                    pygame.display.flip()
                    Cchoice()
                    

                    
def text(msg, x, y, w, h, size):
    global textfont
    textfont = pygame.font.SysFont('forte_o', size)
    textscreen, textrecc = textObj(msg, textfont)
    textrecc.center = ((x+(w/2)) , (y+(h/2)))
    screen.blit(textscreen, textrecc)
    
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

    
def game(): #this is for the title
    global start
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False

        screen.fill(colr)
        button("Start", 465,350,350,100, sc, hc, 1)
        pygame.display.flip()
        pygame.display.update()
        timer.tick(15)
  
                      
        

game()
pygame.quit()   
