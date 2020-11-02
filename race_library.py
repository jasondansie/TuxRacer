import sys, pygame, random
from pygame.locals import *
pygame.init()
pygame.mixer.init()


""" this set up variables for a black color, sets the screen size and then
    puts it all in a screen variable to use in other areas of the code.
    it also set a variable for the clock to control game timing. rem holds
    the list of racers not choosen so we dont choose the same racer.
"""
color = 0,0,0
size = width, height = 800,600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
rem = None
bet = None
sel_racer = None


""" loads a background image to the window and transforms it to the proper size """
bg = pygame.image.load('Track.png')
bg = pygame.transform.scale(bg,(800,600))


""" this loads the intro screen at the begining of the game. """
def intro():
    introsound = pygame.mixer.Sound('flute.wav')
    introsound.play()

    bg = pygame.image.load('Front2.png')
    bg = pygame.transform.scale(bg,(800,600))
    stop = 1
    while stop != 0:
        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            elif event.type == KEYDOWN and event.key == K_q:
                exit()
            elif event.type == KEYDOWN and event.key == K_RETURN:
               stop = 0


        screen.fill((color))
        screen.blit(bg,(0,0))
        pygame.display.flip()


def bet_screen(racer1, racer2, racer3, racer4, racer5, account):


    bg = pygame.image.load('Track.png')
    bg = pygame.transform.scale(bg,(800,600))
    stop = 1
    while 1:
        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            elif event.type == KEYDOWN and event.key == K_q:
                exit()
            elif event.type == KEYDOWN and event.key == K_1:
                if account < 10:
                    pass
                else:
                    return 10
            elif event.type == KEYDOWN and event.key == K_2:
                if account < 20:
                    pass
                else:
                    return 20
            elif event.type == KEYDOWN and event.key == K_3:
                if account < 50:
                    pass
                else:
                    return 50
            elif event.type == KEYDOWN and event.key == K_4:
                if account < 100:
                    pass
                else:
                    return 100
            elif event.type == KEYDOWN and event.key == K_5:
                if account < 500:
                    pass
                else:
                    return 500
                

            
        text = "Use number keys 1-5 to make your bet"
        myFont = pygame.font.SysFont("Comic Sans MS", 25)
        instruc = myFont.render(text, 1, (0,0,200))

        
        text = "Your money:" + str(account)
        myFont = pygame.font.SysFont("Comic Sans MS", 20)
        acc_label = myFont.render(text, 1, (200,0,200))

        
        

        text = "1: $10"
        myFont = pygame.font.SysFont("Comic Sans MS", 20)
        label1 = myFont.render(text, 1, (0,0,200))
        text = "2: $20"
        myFont = pygame.font.SysFont("Comic Sans MS", 20)
        label2 = myFont.render(text, 1, (0,0,200))
        text = "3: $50"
        myFont = pygame.font.SysFont("Comic Sans MS", 20)
        label3 = myFont.render(text, 1, (0,0,200))
        text = "4: $100"
        myFont = pygame.font.SysFont("Comic Sans MS", 20)
        label4 = myFont.render(text, 1, (0,0,200))
        text = "5: $500"
        myFont = pygame.font.SysFont("Comic Sans MS", 20)
        label5 = myFont.render(text, 1, (0,0,200))

        screen.fill((color))
        screen.blit(bg,(0,0))
        screen.blit(instruc, (200, 450))
        

        """ displays the racer labels on the screen """
        screen.blit(label1, (220, 490))
        screen.blit(label2, (220, 530))
        screen.blit(label3, (500, 490))
        screen.blit(label4, (500, 530))
        screen.blit(label5, (350, 560))
        screen.blit(acc_label, (20, 490))
         

        """ displays the racer on the screen """
        screen.blit(racer1.scale,(0,0))
        screen.blit(racer2.scale,(0,90))
        screen.blit(racer3.scale,(0,188))
        screen.blit(racer4.scale,(0,277))
        screen.blit(racer5.scale,(0,366))
        pygame.display.flip()


def select_screen(racer1, racer2, racer3, racer4, racer5):


    bg = pygame.image.load('Track.png')
    bg = pygame.transform.scale(bg,(800,600))
    stop = 1
    while 1:
        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            elif event.type == KEYDOWN and event.key == K_q:
                exit()
            elif event.type == KEYDOWN and event.key == K_1:
                return racer1.name
            elif event.type == KEYDOWN and event.key == K_2:
                return racer2.name
            elif event.type == KEYDOWN and event.key == K_3:
                return racer3.name
            elif event.type == KEYDOWN and event.key == K_4:
               return racer4.name
            elif event.type == KEYDOWN and event.key == K_5:
                return racer5.name

            
        text = "Use number keys 1-5 to choose a racer"
        myFont = pygame.font.SysFont("Comic Sans MS", 25)
        instruc = myFont.render(text, 1, (0,0,200))
        
        

        text = "Position 1: " + racer1.name+" Odd:"+ str(racer1.odd)
        myFont = pygame.font.SysFont("Comic Sans MS", 20)
        label1 = myFont.render(text, 1, (0,0,200))
        text = "Position 2: " + racer2.name+" Odd:"+ str(racer2.odd)
        myFont = pygame.font.SysFont("Comic Sans MS", 20)
        label2 = myFont.render(text, 1, (0,0,200))
        text = "Position 3: " + racer3.name+" Odd:"+ str(racer3.odd)
        myFont = pygame.font.SysFont("Comic Sans MS", 20)
        label3 = myFont.render(text, 1, (0,0,200))
        text = "Position 4: " + racer4.name+" Odd:"+ str(racer4.odd)
        myFont = pygame.font.SysFont("Comic Sans MS", 20)
        label4 = myFont.render(text, 1, (0,0,200))
        text = "Position 5: " + racer5.name+" Odd:"+ str(racer5.odd)
        myFont = pygame.font.SysFont("Comic Sans MS", 20)
        label5 = myFont.render(text, 1, (0,0,200))

        screen.fill((color))
        screen.blit(bg,(0,0))
        screen.blit(instruc, (200, 450))
        

        """ displays the racer labels on the lower right of the screen """
        screen.blit(label1, (90, 490))
        screen.blit(label2, (90, 530))
        screen.blit(label3, (500, 490))
        screen.blit(label4, (500, 530))
        screen.blit(label5, (250, 560))

        """ displays the racer on the screen """
        screen.blit(racer1.scale,(0,0))
        screen.blit(racer2.scale,(0,90))
        screen.blit(racer3.scale,(0,188))
        screen.blit(racer4.scale,(0,277))
        screen.blit(racer5.scale,(0,366))
        pygame.display.flip()


""" this displays the winning screen with the correct winners picture and a
    flashing background
"""
def win_screen(racer, bet, sel_racer, account):

    winsound = pygame.mixer.Sound('crowd_cheer.wav')
    winsound.play()
    winnings = 0
    lose = 0
    r = 0
    winner = pygame.image.load(racer.image)
    winner = pygame.transform.scale(winner,(325,380))
    
    while 1:
        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
            elif event.type == KEYDOWN and event.key == K_q:
                pygame.quit()
            elif event.type == KEYDOWN and event.key == K_c:
                if winnings > 0:
                    account = winnings
                else:
                    account = lose
                if account <= 0 :
                    game_over()
                else:
                    introsound = pygame.mixer.Sound('flute.wav')
                    introsound.play()

                    rem = None
                    game(rem, account)
                    
          
        
        text = "Press c to continue"
        myFont = pygame.font.SysFont("Comic Sans MS", 30)
        cont = myFont.render(text, 1, (0,0,200))

        text = "Press q to quit"
        myFont = pygame.font.SysFont("Comic Sans MS", 30)
        quit_label = myFont.render(text, 1, (0,0,200))

        text = racer.name + " Wins"
        myFont = pygame.font.SysFont("Comic Sans MS", 60)
        label = myFont.render(text, 1, (0,0,200))

        
        text =  "You choose: " + sel_racer
        myFont = pygame.font.SysFont("Comic Sans MS", 30)
        bet2 = myFont.render(text, 1, (100,0,200))

        text = "Your bet was: $" + str(bet)
        myFont = pygame.font.SysFont("Comic Sans MS", 30)
        sel_racer1 = myFont.render(text, 1, (100,0,200))

      
        if sel_racer == racer.name:
            winnings = account + bet
            text =  "Your money: $" + str(winnings)
            myFont = pygame.font.SysFont("Comic Sans MS", 30)
            acc_label = myFont.render(text, 1, (100,0,200))
        else:
            lose = account - bet
            text =  "You lose, you now have: $" + str(lose)
            myFont = pygame.font.SysFont("Comic Sans MS", 30)
            acc_label = myFont.render(text, 1, (100,0,200))
        
        
        screen.fill((r,0,0))
        screen.blit(winner, (250, 200))
        screen.blit(label, (250, 100))
        screen.blit(bet2, (10, 20))
        screen.blit(sel_racer1, (10, 50))
        screen.blit(acc_label, (10, 80))
        screen.blit(quit_label, (10, 550))
        screen.blit(cont, (10, 500))
        
        
        pygame.display.flip()

        """ created by Jason Dansie """
        """ this part of the code is what make the background change colors."""
        if r == 255:
            r1 = -1
        elif r == 0:
            r1 = 1
        r = r + r1
    
    

def game_over():

    r = 0
    introsound = pygame.mixer.Sound('flute.wav')
    introsound.play()

    
    stop = 1
    while stop != 0:
        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            elif event.type == KEYDOWN and event.key == K_q:
                exit()
            elif event.type == KEYDOWN and event.key == K_RETURN:
               stop = 0

        text = "Game Over"
        myFont = pygame.font.SysFont("Comic Sans MS", 70)
        label = myFont.render(text, 1, (0,0,200))
        text = "Pres ESC to quit"
        myFont = pygame.font.SysFont("Comic Sans MS", 50)
        label1 = myFont.render(text, 1, (0,0,200))

        screen.fill((r,0,0))
        screen.blit(label, (240, 200))
        screen.blit(label1, (20, 500))
        pygame.display.flip()
        if r == 255:
            r1 = -1
        elif r == 0:
            r1 = 1
        r = r + r1
        


def New_racer(rem):
    racer1 = racer()
    returnval = get_racer(rem)
    racer1.image = returnval[1]
    tux = pygame.image.load(racer1.image)
    tux = pygame.transform.scale(tux,(80,80))
    racer1.scale = tux
    Cname = convert_name(racer1)
    racer1.name = Cname
    rem = returnval[0]

    return (racer1, rem)

""" this gets a random image for the racer. """                    
def get_racer(rem):

    """ this is the list of images for the racers """
    racers = ['original-tux.png', 'batman-tux.png', 'marg-tux.png', 'robin-tux.png', 'mario-tux.png', 'specialops-tux.png', 'leo-tux.png', 'rambo-tux.png', 'shrek-tux.png', 'wolverine-tux.png']

    if rem == None:
        rem = racers
    n = len(rem)
    racer = rem[(random.randrange(0,n))]

    rem.remove(racer)
    return (rem, racer)


""" this strips the name from the image name and assigns it to the
        racer.name member
"""
def convert_name(racer):
    
    name = racer.image.split ( '-' )
    Nname = name[0].title()
    
    return Nname



""" this defines the speed of the racer. if you use 0 as the starting value
    one racer wil not run.
"""
def speed(racer):
    if racer.odd < 4:
        vel = random.randint(1,3)
        return vel
    elif racer.odd >= 4 & racer.odd < 7:
        vel = random.randint(0,3)
        return vel
    elif racer.odd >= 7 & racer.odd < 11:
        vel = random.randint(0,2)
        return vel

""" this creates the label at the bottom right of the screen. it does not
    set it at the bottom it just creates it. use the scree.blit area to set
    its location on the screen
"""
def get_label(racer):
    text = racer.name + ": " + str(racer.tux_x) 
    myFont = pygame.font.SysFont("Comic Sans MS", 15)
    label = myFont.render(text, 1, (0,0,255))
    return label


def start_race(racer):
    racer.tux_x = racer.tux_x + racer1.speed
    return racer
    

""" this is the racer class. using this all the racers get the same info and
    make much of the game code easier to manipulate.
"""

def get_odd():
    odd = random.randint(2,10)
    return odd

class racer:
    def __init__(self):
        self.name = None
        self.image = None
        self.tux_x = 0
        self.scale = None
        self.odd = get_odd()
        



def game(rem, account):
    
    """ creates a class object racer and updates the rem list so there are less
        chances of getting 2 of the same racers
    """

    racer1 = New_racer(rem)
    rem = racer1[1]

    racer2 = New_racer(rem)
    rem = racer2[1]

    racer3 = New_racer(rem)
    rem = racer3[1]

    racer4 = New_racer(rem)
    rem = racer4[1]


    racer5 = New_racer(rem)
    rem = racer5[1]

    sel_racer = select_screen(racer1[0], racer2[0], racer3[0], racer4[0], racer5[0])

    bet = bet_screen(racer1[0], racer2[0], racer3[0], racer4[0], racer5[0], account)



    """ loads a sound and plays it at the begining of the game """
    sound = pygame.mixer.Sound('galloping.wav')
    sound.play()

    """ racers initial y starting coordinants """

    tux1_y = 0
    tux2_y = 90
    tux3_y = 188
    tux4_y = 277
    tux5_y = 366

    """ the main game loop """
    while 1:
        
        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            elif event.type == KEYDOWN and event.key == K_q:
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                camera.play()
                mx,my = pygame.mouse.get_pos()

                """ this allows you to take a screen shoot by pressing spacebar """
            elif event.type == KEYDOWN and event.key == K_SPACE:
                pygame.image.save(screen, "screenshot.jpg")

        """ adds a text label with the racer name and speed """
        
        label1 = get_label(racer1[0])
        label2 = get_label(racer2[0])
        label3 = get_label(racer3[0])
        label4 = get_label(racer4[0])
        label5 = get_label(racer5[0])

        clock.tick(60)
        screen.fill((0,0,0))
        screen.blit(bg,(0,0))
        
         
        """ displays the label on the lower right of the screen """
        screen.blit(label1, (680, 460))
        screen.blit(label2, (680, 480))
        screen.blit(label3, (680, 500))
        screen.blit(label4, (680, 520))
        screen.blit(label5, (680, 540))


        """ displays the racer on the screen """
        screen.blit(racer1[0].scale,(racer1[0].tux_x,tux1_y))
        screen.blit(racer2[0].scale,(racer2[0].tux_x,tux2_y))
        screen.blit(racer3[0].scale,(racer3[0].tux_x,tux3_y))
        screen.blit(racer4[0].scale,(racer4[0].tux_x,tux4_y))
        screen.blit(racer5[0].scale,(racer5[0].tux_x,tux5_y))
        
        pygame.display.flip()
        
        """ give the racer its speed """
        racer1[0].tux_x = racer1[0].tux_x + speed(racer1[0])
        racer2[0].tux_x = racer2[0].tux_x + speed(racer2[0])
        racer3[0].tux_x = racer3[0].tux_x + speed(racer3[0])
        racer4[0].tux_x = racer4[0].tux_x + speed(racer4[0])
        racer5[0].tux_x = racer5[0].tux_x + speed(racer5[0])

        """ this finds who wins the race and passes it to the winning screen
            screen funciont in the library
        """
        if racer1[0].tux_x >= 700:
            winner = racer1[0]
            win_screen(racer1[0], bet, sel_racer, account)
        elif racer2[0].tux_x >= 700:
            winner = racer2[0]
            win_screen(racer2[0], bet, sel_racer, account)
        elif racer3[0].tux_x >= 700:
            winner = racer3[0]
            win_screen(racer3[0], bet, sel_racer, account)
        elif racer4[0].tux_x >= 700:
            winner = racer4[0]
            win_screen(racer4[0], bet, sel_racer, account)
        elif racer5[0].tux_x >= 700:
            winner = racer5[0]
            win_screen(racer5[0], bet, sel_racer, account)
    return 0
