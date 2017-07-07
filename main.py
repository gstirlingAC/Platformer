import pygame, sys, random  # 1 - import modules and check for successful installation

''' Pygame template - this will be a skeleton for a new pygame project '''


''' We import the libraries that we will want to access for useful modules containing pre-built code.

    For now all we require is:

    pygame - for the pygame modules which will allow us to draw to the screen, add and use sounds and
    control our player with different types of input systems i.e. keyboard/mouse, game pad, joystick etc.

    sys - we only really need this to be able to access the 'exit' function which will properly allow us to shut our program down.

    random - we are going to want to use random values later on in these tutorials e.g. platform spawning.'''

# 2. Set up some constants settings to be used throughout the project
WIDTH = 360
HEIGHT = 480
FPS = 30

# 7. Store references to some useful colour values - RGB values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 3. Initialise pygame and the sound mixer
pygame.init()  # to "start-up" pygame to allow us to be able to use the contained modules
pygame.mixer.init()  # to allow us to be able to add and use sounds in this program

# 4. Create a window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Title")

# 5. Create a 'clock' to control and handle the running speed of the game
clock = pygame.time.Clock()

# 6. Define the 'game loop'
isRunning = True

while isRunning:
    ''' A typical game loop executes in roughly this order:
        Processes - update speed, key presses, mouse presses etc.
        Update - apply any changes made between frames
        Draw/Render - draw the updates between each frame '''

    ###### PROCESSES / LOGIC ######
    clock.tick(FPS)  # Limit the running of the game to the defined frames-per-second (fps)

    # check for player inputs
    for event in pygame.event.get():  # poll for ANY event
        if event.type == pygame.QUIT:  # check for the player closing the window (via the x button)
            isRunning = False  # break out of the loop

    ###### UPDATES ######


    ###### DRAW/RENDER ######
    window.fill(BLACK)  # this is the same as window.fill(0, 0, 0)

    ''' pygame renders using 'double-buffering', what this means is that if you image the window
        is a sheet of paper, after each frame the sheet of paper is 'flipped', what was drawn on
        the other side is now visible, then a new update is drawn on the invisible side waiting
        to be rendered next frame. '''
    pygame.display.flip()  # *AFTER* drawing everything, flip the display

# 8. Shut everything down and close the program
pygame.quit()  # shut down pygame
sys.exit()  # shut down the game
