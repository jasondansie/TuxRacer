import sys, pygame, pygame.mixer, race_library
import sys, pygame, pygame.mixer, race_library
from pygame.locals import *
""" this initiates all the stuff for pygame to work"""
pygame.init()

""" this initiates the sound in pygame. if there is no sound drivers installed
    in the OS this will generate an error and you will have to comment out all
    areas where sound is called.
"""
pygame.mixer.init()

account = 1000
rem = None


""" this loads intro sreen and the game loop from the library file"""   
race_library.intro()

race_library.game(rem, account)
