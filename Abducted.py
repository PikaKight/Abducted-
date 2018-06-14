import pygame, time, random
from pygame.locals import*

pygame.mixer.pre_init() 
pygame.mixer.init()
pygame.init()

screen = pygame.display.set_mode((1280,680)) #the screen size

backmusic = pygame.mixer.music.load("Cloud_Wheels_Castle_Builder.mp3") # loads the background music
dooropen = pygame.mixer.Sound("Wood_Door_Creak_Open.wav") # loads the opening door sound
startroom = pygame.image.load('Starting Room.png') # load the starting room pic
key = pygame.image.load('Lock_Large.png') # Load the key pic
corridor = pygame.image.load('Corridor.png') # load the 1st corridor pic
closed = pygame.image.load('Closed door.png') # load the closed door pic
opened = pygame.image.load('Open Door.png') #load the open door pic
corridor2_cl = pygame.image.load('Corridor 2 Closed.png')# loads the close door corridor 2 pic
corridor2_op = pygame.image.load('Corridor 2 Open.png')# loads the open door corridor 2 pic
corridor34 = pygame.image.load('Corridor 3,4.png') # loads the corridor 3/4
Leveloneexit = pygame.image.load('Boss Door One Keyhole.png') # loads the 1st level exit
Longcorridor = pygame.image.load('Long corridor.png') #loads long corridor
corridor5 = pygame.image.load('Corridor 5.png') #loads 5th corridor
corridor6 = pygame.image.load('Corridor 6.png')# loads 6th corridor
corridor7 = pygame.image.load('Corridor 7.png')# loads 7th corridor
corridor8 = pygame.image.load('Corridor 8.png')# loads 8th corridor
corridor10 = pygame.image.load('Corridor 10.png')# loads 10th corridor
room2 = pygame.image.load('Room 2.png') # loads 2nd room
room3 = pygame.image.load('Room 3.png') # loads 3rd room
rooml2 = pygame.image.load('Boss Room.png')# loads the level 2 room
finalexit = pygame.image.load('Boss Door Two Keyhole.png')# loads the final exit!!
key_place = random.randint(1,3) # this generates a random number inclusively between 1 to 3 BTW this decides the key location
print(key_place) #this prints the number

pygame.mixer.music.play(-1) # play the music and loops it
pygame.mixer.music.set_volume(0.25) # sets the volume to half

pygame.display.set_caption("Abducted") # this adds a title to the game on the top left outside the screen in the border 

colr = (0,0,0) #Background colour

recc = (255,255,255) #box colour

sc = (100, 250 , 0) #start button colour 

hc = (100, 255, 150) #highlight colour

timer = pygame.time.Clock() #lets us use the clock more

timer.tick(60)
 
font = pygame.font.Font(None, 25)

frame_count = 0
frame_rate = 20
start_time = 0

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
        pygame.display.flip() #puts everything on to the display, which lets the user see it
 
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
                    ChrM = pygame.image.load('Character - Dude.png')
                    screen.blit(ChrF, (250, 50))
                    pygame.draw.rect(screen, recc,[620,50,335,400],5)
                    screen.blit(ChrM, (620, 50))
                    text("Choose a character using 1 or 2, Don't use Numb Pad", 50,500,1080,150, 50) #another text that tells the user what to do
                    pygame.display.flip()
                    Cchoice() #calls for the Cchoice functions               
                    
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
                    pygame.draw.rect(screen, hc, [620,50,335,400], 5)
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
    text("Greeting, I am the goddess of Victory, Nike.", 100, 75, 1100, 100, 36) #general story 
    pygame.display.update()
    timer.tick(30)
    pygame.time.delay(500)
    text("You were kidnapped by the Lord of the Flies.", 100, 175, 1100, 100, 36)
    pygame.display.update()
    timer.tick(30)
    pygame.time.delay(500)
    text("I am here to help you escape. Listen to me carefully", 100, 275, 1100, 100, 36)
    pygame.display.update()
    timer.tick(30)
    pygame.time.delay(1000)
    text("The time has come, wait for the your chance and escape.", 100, 375, 1100, 100, 36)
    pygame.display.update()
    timer.tick(30)
    pygame.time.delay(500)
    text("Be cautious and Good Luck.", 100, 475, 1100, 100, 36)
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
                        text("You awaken from a odd dream and hear people talking...", 100, 75, 1100, 100, 36)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        text("It's time to wake him up or the Boss will be mad", 100, 175, 1100, 100, 36)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        text("Prisonner 1, it's time to wake up!", 100, 275, 1100, 100, 36)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        text("What the, where is he? Find him!! ... Wait Who are you?!", 100, 375, 1100, 100, 36)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        text(" *Screams* ", 100, 375, 1100, 100, 36)
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
                        text("You awaken from a odd dream and hear people talking...", 100, 75, 1100, 100, 36)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        text("It's time to wake her up or the Boss will be mad", 100, 175, 1100, 100, 36)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        text("Prisonner 1, it's time to wake up!", 100, 275, 1100, 100, 36)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        text("What the, where is she? Find her!! ... Wait Who are you?!", 100, 375, 1100, 100, 36)
                        pygame.display.update()
                        timer.tick(30)
                        pygame.time.delay(1000)
                        text(" *Screams* ", 100, 375, 1100, 100, 36)
                        tutorial()

def Chr( x, y): #this is to load the character pic
    if char == 1: #female character
     Chrct = pygame.image.load('Girl drawing Larger.png') #loads the female character
     screen.blit(Chrct, (x, y))
     pygame.display.update()
     timer.tick(60)
    if char == 2: #male
     Chrct = pygame.image.load('Guy drawing Larger.png') #loads the male character
     screen.blit(Chrct, (x, y))
     pygame.display.update()
     timer.tick(60)

def tutorial():#starts the game and places the setting
     screen.fill(colr)
     screen.blit( startroom, (315, 35))
     screen.blit( corridor, (945, 220))
     screen.blit( closed, (945, 220)) 
     Chr( 615, 259)
     text("Use WASD to move", 100 , 0 , 100, 50, 36)
     pygame.display.flip()
     pygame.time.delay(1500)
     movement()    

def movement(): #this the movement
    global output_string, bound, unlock, xc, yc
    frame_count = 0
    bound = 0 #this is for the boundaries and to change them base on the different bound value
    unlock = 0 #this is too unlock the exits when the value  
    if bound == 0: # when bound is 0 then place the user at the given location at the start
        x = 615 #location of the x axis of the character
        y = 259 #and the y axis of the character   
    xc = 0 #this is for the movement of the character (left to right)
    yc = 0 #this is for the movement of the character (up to down)
    sup =1 # this is to do speed boost
    
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print (mouse)
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
                    
        x += (xc * sup)#makes the character move by changing the location on the x and y axis
        y+= (yc * sup)

        if x  > 810 and x  < 910 and y > 480 and y  < 600 and bound == 0: # if you are in this area and bound is o, then it will
            pygame.mixer.Sound.play(dooropen)# plays door open sound effects
            bound +=1
            print ("You are unbound!")

        if x >= 1280 and bound == 1: # if it is bound 1 and this area, then it will do this:
            x = 35
            bound = 2

        if x >= 1000 and bound == 2: # if it is bound 2 and this area, then it will do this:
            bound = 3
            text("It seems that the Boss door is locked. Go find the Key to unlock it.", 200, 50, 900, 100, 36)
            pygame.display.flip()
    
        if  x >= 840 and x <= 1090 and y <= 211 and bound == 3: # if it is bound 3 and this area, then it will do this: (this is for the top part)
            bound = 4
            y = 600
            
        if y >= 680 and x >= 250 and x <= 500 and bound == 3:# if it is bound 3 and this area, then it will do this: (this is for bottom)
            bound = 5
            y = 35

        if  x >= 1278 and bound == 5: # if it is bound 5 and this area, then it will do this: (right area)
            bound = 6
            x = 35

        if y >= 660 and bound == 5: # if it is bound 1 and this area, then it will do this: (bottom area)
            bound = 7
            y = 35
            
        if bound == 4 and y >= 680:
            bound = 3
            y = 215
            
        if bound == 5 and y <= 0:
            bound = 3
            y = 600

        if bound == 6 and x <= 0:
            bound = 5
            x = 1278

        if bound == 7 and y <= 0:
            bound = 5
            y = 555

        if x >= 370 and x <= 392 and y >= 165 and y <= 175 and key_place == 1 and unlock == 0 and bound == 4:
            unlock = 1
            print("You did it, You got your freedom!")
            pygame.mixer.Sound.play(dooropen)

        if x >= 700 and x <= 715 and y >= 69 and y <= 79 and key_place == 2 and unlock == 0 and bound == 6:
            unlock = 1
            print("You did it, You got your freedom!")
            pygame.mixer.Sound.play(dooropen)
            
        if x >= 657 and x < 670 and y >= 336 and key_place == 3 and unlock == 0 and bound == 7:
            unlock = 1
            print("You did it, You got your freedom!")
            pygame.mixer.Sound.play(dooropen)

        if x >= 1263 and bound == 3 and unlock == 1:
           bound = 8
           x = 35
           sup = 2
           print("Just Kidding, There's still more!")
           pygame.mixer.music.stop() #ends the first song and goes to the next
           backmusic = pygame.mixer.music.load("The_New_Order.mp3")
           pygame.mixer.music.play(-1)
           pygame.mixer.music.set_volume(0.5)

        if x >= 1270 and bound == 8:
            bound = 9
            x = 10

        if x >= 1270 and bound == 9:
            bound = 10
            x = 10

        if x >= 1270 and bound == 10:
            bound = 11
            x = 10

        if x <= 0 and bound == 11:
            bound = 10
            x = 1260
            
        if x <= 0 and bound == 10:
            bound = 9
            x = 1260
            
        if x <= 0 and bound == 9:
            bound = 8
            x = 1260
            
        if y <= 200 and bound == 11:
            y = 670
            bound = 12

        if bound == 12 and y >= 680:
            y = 210
            bound = 11

        if bound == 12 and x <= 0:
            x = 1265
            bound = 13

        if bound == 13 and x >= 1280:
            x = 10
            y = 306
            bound = 12

        if bound == 13 and x <= 0:
            x = 1260
            bound = 14
            
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
            if y <= 231:
                y += 7
            if y >= 345:
                y -= 7

        if bound == 3:
            if x <= 35:
                x += 7
            if x >= 1100:
              x -= 7                
            if y >= 345:
                y -= 7        
            if x <= 840 and y <= 210:
                x += 7
            if x >= 965 and y <= 210:
                x -= 7
            if x >= 252 and x <= 377:
                if y >= 340:
                    y += 7
            if x <= 252 and y >= 349:
                x += 7
            if x >= 377 and y >= 349:
                x -=7
            if x <= 853 and y <= 231:
                y += 7
            if x >= 1089 and y <= 231:
                y += 7
            if unlock == 1:
                if x >= 1095:
                    x += 7
        
        if bound == 4:
            if x <= 840 and y >= 460:
                x += 7
            if x >= 965:
                x -= 7
            if y <= 103:
                y += 7
            if y >= 334 and x <= 721:
                y -= 7
            if x <= 349:
                x += 7           
                
        if bound == 5:
            if x <= 259:
                x += 7
            if  x >= 370:
                x -= 7
            if y >= 181 and x >= 259:
                x += 7
            if y <= 203 and x >= 483:
                y += 7
            if x >= 876:
                x  -= 7
            if (y >= 504 and x <= 607) or (x >= 734 and y >= 504) :
                y -= 7
            if y >= 329 and y <= 434 and x >= 875:
                x += 7
            if y <= 329 and x >= 990:
                y += 7
            if y >= 434 and x >= 990:
                y -= 7
            if y >= 490 and x <= 620:
                    x += 7
            if y >= 490 and x >= 735:
                    x -= 7

        if bound == 6:
            if y <= 320 and x <= 250:
                y += 7
            if y >= 440 and x <= 250:
               y -= 7
            if y >= 513:
                y -= 7
            if  x >= 756:
                x -= 7
            if x <= 250 and y == 505:
                x += 7
            if x <= 250 and y <= 198:
                x += 7
            if y <= 76:
                y += 7
            
        if bound == 7:
            if x <= 620:
                x += 7
            if x >= 735:
                x -= 7
            if y >= 371:
                y -= 7

       
        if bound == 8:
            if x <= 35:
                x += 14 
            if y <= 246 and x <= 223:
                y += 14
            if y >= 336 and x <= 223:
                y -= 14
            if x <= 313 and y <= 156:
                x += 14
            if x <= 313 and y >= 425:
                x += 14
            if y <= 96:
                y += 14
            if  y >= 509:
                y -= 14
            if x >= 818 and y >= 404:
                x -= 14
            if x >= 818 and y <= 81:
                x -= 14
            if x >= 903 and y >= 333:
                y -= 14
            if x >= 945 and y <= 207:
                y += 14
            if x >= 819 and y <= 120:
                x -= 14
                
        if bound == 9:
            if y <= 236:
                y += 14
            if y >= 334:
                y -= 14

        if bound == 10:
            if y <= 236:
                y += 14
            if y >= 334:
                y -= 14

        if bound == 11:
            if x >= 1080:
              x -= 14              
            if y >= 341:
                y -= 14
            if y <= 236 and x < 841:
                y += 14
            if y <= 236 and x >= 1080:
                y += 14

        if bound == 12:
            if y <= 110:
                y += 14
            if x  >= 961:
                x -= 14
            if y >= 318 and x <= 841:
                y -= 14
            if y <= 255 and x <= 338:
                x += 14
            if y <= 236 and x < 338:
                y += 14
            
        if bound == 13:
            if y <= 110:
                y += 14
            if y >= 335:
                y -= 14
            if x <= 663 and y <= 110:
                x += 14
            if y <= 235 and x <= 633:
                y += 14

        if bound == 14:
            if y <= 220:
                y += 14
            if y >= 320 and x <= 1022 and x >= 220:
                y -= 14
            if y >= 320 and x <= 84 and x <= 0:
                y -= 14
            if x <= 1036 and y >= 460:
                x += 14
            if x >= 1148 and y >= 460:
                x -= 14
            if x <= 83 and y >= 460:
                x += 14
            if x >= 196 and y >= 460:
                x -= 14
            
        if bound == 0: 
            screen.fill(colr)
            total_seconds = frame_count // frame_rate
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "{0:02}:{1:02}".format(minutes, seconds)
            time = font.render(output_string, True, recc)
            screen.blit(time, [1100, 35])
            total_seconds = (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
            frame_count += 1
            screen.blit( corridor, (945, 220))
            screen.blit( closed, (945, 220)) 
            screen.blit( startroom, (315, 35))
            text("Go to the key to unlock the door", 200, 10, 100, 50, 36)
            Chr( x, y)
            screen.blit(key, (820, 510))
            pygame.display.flip()

        if bound == 1:
            screen.fill(colr)
            total_seconds = frame_count // frame_rate
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "{0:02}:{1:02}".format(minutes, seconds)
            time = font.render(output_string, True, recc)
            screen.blit(time, [1100, 35])
            total_seconds = (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
            frame_count += 1
            screen.blit( corridor, (945, 220))
            screen.blit( opened, (945, 220)) 
            screen.blit( startroom, (315, 35))
            text("Go to the key to unlock the door", 200, 10, 100, 50, 36)
            Chr( x, y)
            screen.blit(key, (820, 510))
            pygame.display.update()
            timer.tick(60)
                
        if bound == 2:
            screen.fill(colr)
            total_seconds = frame_count // frame_rate
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "{0:02}:{1:02}".format(minutes, seconds)
            time = font.render(output_string, True, recc)
            screen.blit(time, [1100, 35])
            total_seconds = (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
            frame_count += 1
            text("It seems the door is locked. Go find the Key to unlock it.", 200, 50, 900, 100, 36)
            screen.blit( corridor2_cl, (35, 220)) 
            screen.blit( Leveloneexit, (1235, 205,)) 
            Chr( x, y)
            pygame.display.update()
            timer.tick(60)

        if bound == 3:
            screen.fill(colr)
            total_seconds = frame_count // frame_rate
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "{0:02}:{1:02}".format(minutes, seconds)
            time = font.render(output_string, True, recc)
            screen.blit(time, [1100, 35])
            total_seconds = (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
            frame_count += 1
            screen.blit( corridor2_op, (35, 220))
            screen.blit( corridor34, (250, 470,))
            screen.blit( Leveloneexit, (1235, 205,))
            if unlock == 1:
                pygame.draw.rect(screen, recc, [1235, 205, 45, 280])
            Chr( x, y)
            pygame.display.update()
            timer.tick(60)

        if bound == 4:
            screen.fill(colr)
            total_seconds = frame_count // frame_rate
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "{0:02}:{1:02}".format(minutes, seconds)
            time = font.render(output_string, True, recc)
            screen.blit(time, [1100, 35])
            total_seconds = (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
            frame_count += 1
            screen.blit(room2 ,(340, 30))
            screen.blit(corridor5, (840, 460))
            Chr(x,y)
            if key_place == 1:
                screen.blit(key, (410, 199))
            pygame.display.update()
            timer.tick(60)

        if bound == 5:
            screen.fill(colr)
            total_seconds = frame_count // frame_rate
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "{0:02}:{1:02}".format(minutes, seconds)
            time = font.render(output_string, True, recc)
            screen.blit(time, [1100, 35])
            total_seconds = (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
            frame_count += 1
            screen.blit(corridor6,(250, 0))
            screen.blit(corridor7,(610, 630))
            screen.blit(corridor8,(1000, 320))
            screen.blit(room3,(250, 200))
            Chr(x, y)
            pygame.display.update()
            timer.tick(60)
             
        if bound == 6:
            screen.fill(colr)
            total_seconds = frame_count // frame_rate
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "{0:02}:{1:02}".format(minutes, seconds)
            time = font.render(output_string, True, recc)
            screen.blit(time, [1100, 35])
            total_seconds = (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
            frame_count += 1
            screen.blit(corridor10, (0, 320,))
            screen.blit(rooml2, (250, 35,))
            Chr(x, y)
            if key_place == 2:
                screen.blit(key, (736, 79))
            pygame.display.update()
            timer.tick(60)

        if bound == 7:
            screen.fill(colr)
            total_seconds = frame_count // frame_rate
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "{0:02}:{1:02}".format(minutes, seconds)
            time = font.render(output_string, True, recc)
            screen.blit(time, [1100, 35])
            total_seconds = (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
            frame_count += 1
            screen.blit(corridor6, (610, 0))
            Chr(x, y)
            if  key_place == 3:
                screen.blit(key, (687, 366))
            pygame.display.update()
            timer.tick(60)

        if bound == 8:
            screen.fill(colr)
            total_seconds = frame_count // frame_rate
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "{0:02}:{1:02}".format(minutes, seconds)
            time = font.render(output_string, True, recc)
            screen.blit(time, [1100, 35])
            total_seconds = (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
            frame_count += 1
            screen.blit(Longcorridor, (0, 220))
            screen.blit(rooml2, (315, 35))
            Chr(x,y)
            pygame.display.update()
            timer.tick(60)

        if bound == 9:
            screen.fill(colr)
            total_seconds = frame_count // frame_rate
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "{0:02}:{1:02}".format(minutes, seconds)
            time = font.render(output_string, True, recc)
            screen.blit(time, [1100, 35])
            total_seconds = (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
            frame_count += 1
            screen.blit(Longcorridor, (0, 220))
            Chr(x, y)
            pygame.display.update()
            timer.tick(60)

        if bound == 10:
            screen.fill(colr)
            total_seconds = frame_count // frame_rate
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "{0:02}:{1:02}".format(minutes, seconds)
            time = font.render(output_string, True, recc)
            screen.blit(time, [1100, 35])
            total_seconds = (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
            frame_count += 1
            screen.blit(Longcorridor, (0, 220))
            Chr(x, y)
            pygame.display.update()
            timer.tick(60)

        if bound == 11:
            screen.fill(colr)
            total_seconds = frame_count // frame_rate
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "{0:02}:{1:02}".format(minutes, seconds)
            time = font.render(output_string, True, recc)
            screen.blit(time, [1100, 35])
            total_seconds = (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
            frame_count += 1
            text("This is it, The Boss Door. Find the Two Keys to open it and excape!", 127, 517, 1000, 100, 36)
            screen.blit( corridor2_op, (0, 220))
            screen.blit( finalexit, (1200, 205,))
            Chr(x, y)
            pygame.display.update()
            timer.tick(60)

        if bound == 12:
            screen.fill(colr)
            total_seconds = frame_count // frame_rate
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "{0:02}:{1:02}".format(minutes, seconds)
            time = font.render(output_string, True, recc)
            screen.blit(time, [1100, 35])
            total_seconds = (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
            frame_count += 1
            screen.blit(Longcorridor, (0, 220))
            screen.blit(corridor5, (840, 460))
            screen.blit(room2 ,(340, 30))
            pygame.draw.rect(screen, colr, [1090, 0, 190, 680 ])
            Chr(x, y)
            pygame.display.update()
            timer.tick(60)
        
        if bound == 13:
            screen.fill(colr)
            total_seconds = frame_count // frame_rate
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "{0:02}:{1:02}".format(minutes, seconds)
            time = font.render(output_string, True, recc)
            screen.blit(time, [1100, 35])
            total_seconds = (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
            frame_count += 1
            screen.blit(Longcorridor, (0, 220))
            screen.blit( room2, (650, 35))
            Chr(x, y)
            pygame.display.update()
            timer.tick(60)

        if bound == 14:
            screen.fill(colr)
            total_seconds = frame_count // frame_rate
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "{0:02}:{1:02}".format(minutes, seconds)
            time = font.render(output_string, True, recc)
            screen.blit(time, [1100, 35])
            total_seconds = (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
            frame_count += 1
            screen.blit(Longcorridor, (0, 220))
            screen.blit( corridor34, (78, 470,))
            screen.blit( corridor34, (1020, 470,))
            Chr(x, y)
            pygame.display. update()
            timer.tick(60)
            
game()
pygame.quit()  
