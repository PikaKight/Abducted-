import pygame, time
from pygame.locals import*

pygame.init()

screen = pygame.display.set_mode((1280,680)) #the screen size

startroom = pygame.image.load('Starting Room.png')
key = pygame.image.load('Lock_Large.png')
corridor = pygame.image.load('Corridor.png')
#corridor2 = pygame.image.load('Corridor # 2.png')

pygame.display.set_caption("Abducted")

colr = (0,0,0) #Background colour

recc = (255,255,255) #box colour

sc = (100, 250 , 0) #start button colour 

hc = (100, 255, 150) #highlight colour

timer = pygame.time.Clock() #lets us use the clock more

timer.tick(60)

def textObj(msg, text): #this function mainly handles what colour the text has 
    textcolour =  textfont.render(msg, 1,  recc)
    return textcolour, textcolour.get_rect()

def text(msg, x, y, w, h, size): #this is the main function that creates the text and the position 
    global textfont
    textfont = pygame.font.SysFont('forte', size) #this is for the font of the text
    textscreen, textrecc = textObj(msg, textfont) #lets the text have colour and the font
    textrecc.center = ((x+(w/2)) , (y+(h/2))) #for the position of th text
    screen.blit(textscreen, textrecc) #puts the text on the screen
    
def button(msg, x, y, w, h, sc, hc, a): #creates a button the works and has words on it
    global mouse
    mouse = pygame.mouse.get_pos() #find where the mouse is
    click = pygame.mouse.get_pressed() #finds which mouse button is pressed
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y: # check is the mouse is with in the range of the button 
        pygame.draw.rect(screen, hc,(x,y,w,h)) #makes the button highlighted
        if click[0] == 1 and a == 1: #check if the left button is click
            Startaction() #calls for this action
        if click[0] == 1 and a == 2:
            Load()
    else:
        pygame.draw.rect(screen, sc, (x,y,w,h)) #or it would put back the button back to normal

    global textfont #the next few lines are just the text code just for the buttons
    textfont = pygame.font.SysFont('forte', 72)
    textscreen, textrecc = textObj(msg, textfont)
    textrecc.center = ((x+(w/2)) , (y+(h/2)))
    screen.blit(textscreen, textrecc)

def game(): #this is for the game to run
    global start
    start = True
    while start: # as long as start is true it will run continuously
        for event in pygame.event.get(): #gets the different events in pygame
            if event.type == pygame.QUIT: #if the user quit the game, this will in turn end the program    
                start = False

        screen.fill(colr) #makes the screen black
        button("Start", 465,350,350,100, sc, hc, 1) #creates a start button
        button("Load", 465,460,350,100, sc, hc, 2) #load button
        pygame.display.flip() #puts everything on to the display, which lets the user see it
        pygame.display.update()#updates the screen depending on the tick time
        timer.tick(15)#gives a tick time of 15 nino secons 
 
def Startaction(): #this lets the user click on the start button
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               start = False
            if event.type == pygame.MOUSEBUTTONDOWN:#interagative button
                if (mouse[0] > 470 and mouse[0] < 810) and (mouse[1] > 355 and mouse[1] < 445):#The range of which the mouse clicks 
                    print ("Hello, ") #just there to check if it works and still on the screen
                    screen.fill(colr)
                    pygame.draw.rect(screen, recc,[250,50,335,400],5) #Draws rectangles on the screen
                    global ChrF # turns the ChrF var into a global var that other functions can use
                    ChrF = pygame.image.load('Character - GirlV2.png') #Loads the image of female card 
                    screen.blit(ChrF, (250, 50))
                    pygame.display.update()
                    timer.tick(30)
                    pygame.draw.rect(screen, recc,[620,50,335,400],5)
                    text("Choose a character using 1 or 2, Don't use Numb Pad", 50,500,1080,150, 50) #another text that tells the user what to do
                    pygame.display.flip()
                    Cchoice() #calls for the Cchoice functions

def Load():
    start = True
    while start:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             start = False
         if event.type == pygame.MOUSEBUTTONDOWN:#interagative button
             if (mouse[0] > 470 and mouse[0] < 810) and (mouse[1] > 465 and mouse[1] < 565): #if within range, then fill the screen black and do the load screen
                    screen.fill(colr)
                    pygame.draw.rect(screen, recc, [100, 50, 600, 200], 5)
                    pygame.display.flip()
                    
                    
def Cchoice(): # lets the user choose the character
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.KEYDOWN:# check if the the keyboard key is pressed
                if event.key == pygame.K_1: #check if the user press 1
                    print ("I'm your MC, I won't die soon (HOPEFULLY).")
                    pygame.draw.rect(screen, hc,[250,50,335,400],5) #highlighs the box and let it stay there for a short amount of time
                    screen.blit(ChrF, (250, 50))
                    pygame.display.update()
                    timer.tick(10)
                    pygame.time.delay(250)
                    screen.fill(colr)
                    story("F") #calls for the female story and character 
                    pygame.display.update()
                    timer.tick(60)
                    start = False

                if event.key == pygame.K_2: #check if the user pressed 2 and calls for the male story
                    print ("I'm your MC, I won't die soon (HOPEFULLY).")
                    pygame.draw.rect(screen, hc, [670,50,335,400], 5)
                    pygame.display.update()
                    timer.tick(10)
                    pygame.time.delay(250)
                    screen.fill(colr)
                    story("M")
                    pygame.display.update()
                    timer.tick(10)
                    start = False

def story(a): #story function
    global char
    char = 0 #this is to help indicate which character is chosen 
    text("Greeting Player, I am  ", 100, 75, 1100, 100, 36) #general story 
    pygame.display.update()
    timer.tick(30)
    pygame.time.delay(1000)
    text("You are Trapped  ", 100, 175, 1100, 100, 36)
    pygame.display.update()
    timer.tick(30)
    pygame.time.delay(1000)
    text("To escape", 100, 275, 1100, 100, 36)
    pygame.display.update()
    timer.tick(30)
    pygame.time.delay(1000)
    text("Listen to my intrustion carefully.", 100, 375, 1100, 100, 36)
    pygame.display.update()
    timer.tick(30)
    pygame.time.delay(1000)
    text("Be cautious, you are about to wake up.", 100, 475, 1100, 100, 36)
    pygame.display.update()
    timer.tick(30)
    text("Click space to continue -->", 100, 575, 1100, 100, 36)
    pygame.display.update()
    timer.tick(30)
    
    if a == "M": #this is the male sorry
        char = 2
        keypress = True
        while keypress:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keypress = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        screen.fill(colr)
                        pygame.time.delay(1000)
                        text("You hear people talking . . . ", 100, 75, 1100, 100, 36)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        text("He's been asleep for a while now", 100, 175, 1100, 100, 36)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        tutorial() #starts the actual game

    if a == "F":#female story
        char = 1
        keypress = True
        while keypress:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keypress = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        screen.fill(colr)
                        pygame.time.delay(1000)
                        text("You hear people talking . . . ", 100, 75, 1100, 100, 36)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        text("She's been asleep for a while now", 100, 175, 1100, 100, 36)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        tutorial()

def Chr( x, y): #this is to load the character pic
    if char == 1: #female character
     Chrct = pygame.image.load('Girl drawing Larger.png') #loads the female character
     screen.blit(Chrct, (x, y))
     pygame.display.update()
     timer.tick(60)
    if char == 2: #male
     Chrct = pygame.image.load('Girl drawing Larger.png') #loads the male character
     screen.blit(Chrct, (x, y))
     pygame.display.update()
     timer.tick(60)

def tutorial(): #starts the game and places the setting
       screen.fill(colr)
       screen.blit( startroom, (315, 35))
       screen.blit( corridor, (945, 220)) 
       Chr( 615, 259)
       text("Use WASD to move", 100 , 0 , 100, 50, 36)
       pygame.display.flip()
       pygame.time.delay(2500)
       movement()    

def movement(): #this the movement
    bound = 0
    if bound == 0:
        x = 615 #location of the x and y axis of the character
        y = 259    
    xc = 0 #this is for the movement of the character
    yc = 0
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_w: #when the play presses w, a, s, or d the character will move up(w) 5, left(a) 5, down(s) 5, and right(d) 5
                    yc -= 7
                if event.key == K_a:
                    xc -= 7
                if event.key == K_s:
                    yc += 7
                if event.key == K_d:
                    xc += 7
            if event.type == pygame.KEYUP: #when the user relase the key the character stops moving
                if event.key == K_w:
                    yc = 0
                if event.key == K_a:
                    xc = 0
                if event.key == K_s:
                    yc = 0
                if event.key == K_d:
                    xc = 0
                    
        x += xc #makes the character move by changing the location on the x and y axis
        y+= yc

        if x  > 810 and x  < 910 and y > 480 and y  < 600 and bound == 0:
            bound +=1
            print ("You are unbound!")

        if x >= 1280 and bound == 1:
            x = 35
            bound = 2
            screen.fill(colr)
            pygame.draw.rect(screen, recc, [35,220, 1100, 250])
            Chr( 35, y)
            pygame.display.flip()

        if x >= 1000 and bound == 2:
            bound = 3
            text("It seems this is the Boss Door. Go find the TWO Keys to unlock it.", 200, 50, 900, 100, 36)
            pygame.display.flip()
             
        if bound == 0:
            if x <= 315: #these if statement are for the boundry of the charcter, BTW the top left corner is (0,0)
                x += 7
            if  x >= 830:
                x -= 7
            if  y <= 180:
                y += 7
            if  y >= 500:
                y -= 7

        if bound == 1:
            if x <= 315: #these if statement are for the boundry of the charcter, BTW the top left corner is (0,0)
                x += 7
            if x >= 830 and y >= 345:
                if y  >= 345:
                   y -= 7
            if x >= 830 and y <= 230:
                if y <=230:
                    y += 7
            if x >= 830 and y >350:
                x -=7
            if  y <= 180:
                y += 7
            if  y >= 500:
                y -= 7

        if bound == 2:
            if x <= 35:
                x += 7
            if x >= 1100:
                x -= 7
            if y <= 230:
                y += 7
            if y >= 345:
                y -= 7

        if bound == 3:
            if x <= 35:
                x += 7
            if x >= 1100:
                x -= 7
            if y <= 230:
                y += 7
            if y >= 345:
                y -= 7        
   
        if bound <= 1: 
            screen.fill(colr)
            screen.blit( corridor, (945, 220)) 
            screen.blit( startroom, (315, 35))
            text("Go to the key to unlock the door", 200, 10, 100, 50, 36)
            Chr( x, y)
            screen.blit(key, (820, 510))
            pygame.display.flip()
            timer.tick(60)

        if bound == 2:
            screen.fill(colr)
            text("It seems this is the Boss Door. Go find the TWO Keys to unlock it.", 200, 50, 900, 100, 36)
            pygame.draw.rect(screen, recc, [35,220, 1200, 250])
            screen.blit( corridor, (35, 220)) 
            pygame.draw.rect(screen, hc, [1235, 205, 45, 280])
            Chr( x, y)
            pygame.display.update()
            timer.tick(60)

        if bound == 3:
            screen.fill(colr)
            pygame.draw.rect(screen, recc, [35,220, 1200, 250])
            screen.blit( corridor, (35, 220)) 
            pygame.draw.rect(screen, hc, [1235, 205, 45, 280])
            Chr( x, y)
            pygame.display.update()
            timer.tick(60)
        
            
game()
pygame.quit()   
