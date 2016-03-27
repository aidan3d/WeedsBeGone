###################################################################
#                WEEDS BE GONE!
#
# Author:        Aidan Hegarty
#
# Last modified: March 27, 2016
#
# Description:   A board game in which the player matches
#                a number displayed on screen by removing
#                clumps of weeds!
#
#                Note:
#                    This could be a mathematics game in
#                    which only prime numbers are
#                    selected, or perhaps factors of
#                    a non-prime number. Letters? LCD
#                    mnemonic symbols? "Red Returns?"
#
###################################################################
import random
import time
import board
import pygame
from pygame.locals import *

# Create global constants to hold the 'garden's' width and
# height (in pixels). A pixel represents a foot of length.
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

# Create a global constant to hold the height of the
# 'countdown strip' at the bottom of the game window.
SCORE_PAD_HEIGHT = 160

# Create global constants to hold the cell (or 'square'). 
# Count horizontally and vertically.
NUM_CELLS_HOR = 8
NUM_CELLS_VER = 8

# Global constants to reference the 'starting coordinates'
# for the grid.
X_ORIGIN = 0
Y_ORIGIN = 0

FPS = 30

# Global constant to reference the number of frames in the
# weed animation's 'film strip.'
NUM_FRAMES = 10

# A global constant to reference the number of slides in
# the splash screen slideshow.
NUM_SPLASH_SCREEN_SLIDES = 9

# A global constant referring to the number of slides
# in the splash screen slideshow.
NUM_HELP_SCREEN_SLIDES = 68

# A global constant to hold the point height of the
# countdown display font
COUNTDOWN_TEXT_HEIGHT = 200


TIMER_TEXT_HEIGHT = 24

# A global constant to control the maximum and minimum
# weed counter at the screen's bottom
# (i.e. 1 - 15 )
MIN_COUNT = 2
MAX_COUNT = 44

def main():



    ###############################################################
    # 1.    Initialization phase.
    #
    ###############################################################

    # Create a 'signal flag'; it will be 'raised' when the
    # player wishes to stop playing the game.
    done_playing = False

    # Create a random number for the player to match with
    # 'mowed' (i.e. erased) weeds.
    countdown_number = random.randint(MIN_COUNT, MAX_COUNT)



    ###############################################################
    # 1A.   Create the file names.
    #
    ###############################################################

    # The 'green' weed image base file name. The frame number
    # and the file type will be added to the end of the file
    # name in load_reel.
    green_weed_file_name_base = 'images\weed'

    # The 'red' weed image base file name. The 'red' weeds'
    # purpose is to represent 'mis-hits' on screen. Should
    # you happen upon a red weed, you'll know you can't
    # subtract that value from the 'weed count.'
    # (countdown_number)
    red_weed_file_name_base = 'images\weed_red'

    # The base file name for the splash screen slideshow.
    splash_screen_file_name_base = 'images\splash_screen'

    # The base file name for the help screen
    # slideshow.
    help_screen_file_name_base = 'images\help_screen'



    ###############################################################
    # 1B.   Create the game board.
    #
    ###############################################################

    garden = board.Board(
        SCREEN_WIDTH,
        SCREEN_HEIGHT - SCORE_PAD_HEIGHT,
        NUM_CELLS_HOR,
        NUM_CELLS_VER,
        X_ORIGIN,
        Y_ORIGIN
    )



    ###############################################################
    # 1C.   Set up pyGame.
    #
    ###############################################################    

    # Set up pyGame.
    pygame.init()

    # Create a Surface object to hold the garden.
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT), RESIZABLE, 32
    )
    pygame.display.set_caption('Weeds Be Gone!')

    # Create the display font for the countown timer.
    full_screen_font = pygame.font.SysFont("arial bold", COUNTDOWN_TEXT_HEIGHT)

    # Create the smaller font for the timer.
    timer_font = pygame.font.SysFont("arial", TIMER_TEXT_HEIGHT)


    ###############################################################
    # 1D.   Load the slideshows and the weed clump bitmaps.
    #
    ###############################################################


    # Load the slideshow for the
    # splash screen.
    splash_screen_file_names = load_slideshow(
        splash_screen_file_name_base,
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        NUM_SPLASH_SCREEN_SLIDES
    )

    # Load the slideshow for the help
    # screens.
    help_screen_file_names = load_slideshow(
        help_screen_file_name_base,
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        NUM_HELP_SCREEN_SLIDES
    )

    # Load the animation reel (the weed images
    # for the cells on the board)
    filmstrip_green = load_reel(
        green_weed_file_name_base,
        garden.get_cell_width(),
        garden.get_cell_height()
    )

    # Load the 'missed cells' animation
    # reel (red weed images for the
    # cells on the board).
    filmstrip_red = load_reel(
        red_weed_file_name_base,
        garden.get_cell_width(),
        garden.get_cell_height()
    )



    ###############################################################
    # 2.    Execution phase.
    #
    ###############################################################

    # Show the garden.
    screen.fill([0, 0, 0])

    # Display the splash screen.
    display_screen(screen, splash_screen_file_names)

    # Flip the back buffer for
    # the first time.
    pygame.display.update()


    ###############################################################
    # 2A.   Start the timer.
    #
    ###############################################################

    start_time = time.time()
    
    # The main game loop.
    while not done_playing:

        ###########################################################
        # 2A(i).   Update the timer.
        #
        ###########################################################
        current_time = time.time()
        elapsed_time = current_time - start_time
        print(format(elapsed_time, '.2f'), 's', sep='')

        # Retrive all events
        # and empty the event queue.
        event = pygame.event.wait()

        # Check whether the user has
        # hit the game window's close
        # button.
        if event.type == QUIT:
            done_playing = True

        # Check whether the player
        # has hit the mouse button.
        if event.type == MOUSEBUTTONDOWN:

            # Paint in the grass.
            screen.fill([0, 0, 0])

            # Pull the mouse coordinates when the
            # mouse button was clicked by the
            # player.
            mousex, mousey = pygame.mouse.get_pos()



            #######################################################
            # 2A(i)a.   Check whether the player has hit the
            #           'stop' button.
            #
            #######################################################

            # If the player has clicked on the stop button...
            if (
                mousey > SCREEN_HEIGHT-SCORE_PAD_HEIGHT and 
                mousex > 0.75*SCREEN_WIDTH
            ):
                    done_playing = True
            # Or, if the player has clicked the
            # help button...
            elif (
                mousey > SCREEN_HEIGHT-SCORE_PAD_HEIGHT and
                mousex > (0.25 * SCREEN_WIDTH)
                ):
                    # Display the help screen.
                    display_screen(screen, help_screen_file_names)

            # ...otherwise, play on!
            else:

                ###############################################################
                # Calculate the value of the weed clump
                # most recently hit by the player.
                #
                ###############################################################

                # Identify the id_number of the last cell
                # clicked
                # (in the range: 0 - NUM_CELLS_WIDE * NUM_CELLS_HIGH)
                current_cell_id = garden.identify_cell(mousex, mousey)
    
                # Subtract the current weed clump's value
                # from the overall weed countdown number.
                countdown_number = countdown_tracker(
                    screen,
                    garden,
                    current_cell_id,
                    countdown_number
                )



                #######################################################
                # Checking for our win condition here!!
                # ('Top' of the loop)
                #
                #######################################################
                
                if countdown_number == 0:
                    countdown_text = full_screen_font.render(
                        'win!',
                        True,
                        (0, 200, 0)
                    )

                else:
                    # Create a surface containing
                    # the updated countdown number.
                    countdown_text = full_screen_font.render(
                        str(countdown_number),
                        True,
                        (200, 200, 200)
                    )

                # Create a text surface for
                # to display the total game
                # time elapsed.
                timer_text = timer_font.render(
                   format((elapsed_time), '.1f') + 's',
                   True,
                   (150, 162, 150)
                )

                # Center the countdown number vertically,
                # and place it in the 'score strip' at the
                # bottom of the game window
                text_rect = countdown_text.get_rect()
                text_rect.centerx = screen.get_rect().centerx
                text_rect.centery = (
                    screen.get_rect().bottom - COUNTDOWN_TEXT_HEIGHT / 3
                )

                # Display the timer.
                screen.blit(timer_text, (0, SCREEN_HEIGHT-SCORE_PAD_HEIGHT))
                
                # Display the score.
                screen.blit(countdown_text, text_rect)



                ###############################################################
                # Grow the weed clumps in their rack.
                #
                ###############################################################
    
                # Grow the clumps of weeds in the garden.
                for cell_planter in range(NUM_CELLS_HOR * NUM_CELLS_VER):

                    # Draw the cell border.
                    cell_boundary = pygame.Rect(
                        garden.get_cell_by_index(cell_planter).get_x_center() -
                            garden.get_cell_width() / 2,
                            garden.get_cell_by_index(cell_planter).get_y_center() -
                            garden.get_cell_height() / 2,
                            garden.get_cell_width(),
                            garden.get_cell_height()
                    )
                    pygame.draw.rect(screen, (255, 255, 255), cell_boundary, 2)



                    ####################################################$#######
                    # The next tricky piece of code checks whether
                    # a cell has been 'marked' as dead by the last
                    # sweep of the countdown_tracker function in
                    # the previous iteration of the while loop.
                    #
                    ############################################################

                    # If the cell is flagged as a prior mis-hit...
                    if garden.get_cell_by_index(cell_planter).is_flagged():
                        
                        # Draw a 'red' weed clump in the
                        # current cell
                        screen.blit(
                            filmstrip_red[garden.get_cell_by_index(cell_planter).get_value()], (
                                garden.get_cell_by_index(cell_planter).get_x_center() -
                                garden.get_cell_width() / 2,
                                garden.get_cell_by_index(cell_planter).get_y_center() -
                                garden.get_cell_height() / 2
                            )
                        )

                    # Or else, if the cell is alive (and, therefore,
                    # implicitly not-flagged)...
                    elif garden.get_cell_by_index(cell_planter).is_alive():
    
                        # For each parcel in the garden, display the 
                        # weed clump.
                        screen.blit(
                            filmstrip_green[garden.get_cell_by_index(cell_planter).get_value()], (
                                garden.get_cell_by_index(cell_planter).get_x_center() -
                                garden.get_cell_width() / 2,
                                garden.get_cell_by_index(cell_planter).get_y_center() -
                                garden.get_cell_height() / 2
                            )
                        )

                    else: # The cell is not alive

                        # so draw a blank at the current cell.
                        screen.blit(
                            filmstrip_green[9], (  # Subscript is "weed10.png"
                                garden.get_cell_by_index(cell_planter).get_x_center() -
                                    garden.get_cell_width() / 2,
                                    garden.get_cell_by_index(cell_planter).get_y_center() -
                                    garden.get_cell_height() / 2
                            )
                        )

            # Flip the back buffer.
            pygame.display.update()



    ###############################################################
    # Termination phase.
    #
    ###############################################################

    # Unload pygame.
    pygame.quit()

# Loads the animation frames
# (a bunch of images of weed clumps).
def load_reel(file_name_base, width, height):

    # Create a sequence variable to
    # hold the references to the file
    # objects for each frame.
    animation_frames = list()

    for playhead in range(NUM_FRAMES):

        # Create a full file name (with the
        # frame number and the file extension
        # added to the base file name (i.e. if
        # the base is "ball", then the first
        # file is "ball1.jpg"))
        full_file_name = file_name_base + str(playhead + 1) + '.png'

        # Create a pygame surface object to hold
        # the new bitmap. Concatenate the base
        # file name, the frame number and the
        # file extension.
        frame_surface = pygame.image.load(
            full_file_name).convert_alpha()

        # Scale the image according to the
        # grid size chosen by the player.
        frame_surface = pygame.transform.scale(
            frame_surface,
            (int(width), int(height))
        )

        # Add the frame to the filmstrip
        animation_frames.append(frame_surface)

    return animation_frames

# Loads the slideshow images.
# (a bunch of screens from
# an image editing program).
def load_slideshow(file_name_base, width, height, num_slides):

    # Create a sequence variable to
    # hold the references to the file
    # objects for each slide.
    slideshow = list()

    for playhead in range(num_slides):

        # Create a full file name (with the
        # frame number and the file extension
        # added to the base file name (i.e. if
        # the base is "ball", then the first
        # file is "ball1.jpg"))
        full_file_name = file_name_base + str(playhead + 1) + '.png'

        # Create a pygame surface object to hold
        # the new bitmap. Concatenate the base
        # file name, the frame number and the
        # file extension.
        frame_surface = pygame.image.load(
            full_file_name).convert_alpha()

        # Add the frame to the filmstrip
        slideshow.append(frame_surface)

    return slideshow

# The countdown_tracker function updates
# the weeds-left-to-kill countdown, and
# flags weed clumps as being mis-hit
# or 'killed.'
def countdown_tracker(screen, board, cell_id, weeds_in):

    # Reduce the countdown number by
    # the value of the weed clump
    # vanquished.
    current_countdown = (
        weeds_in -
        board.get_cell_by_index(cell_id).get_value() - 1 # allow for overstep
    )

    # Be careful not to overcut,
    # can only mow to zero weeds.
    if current_countdown < 0:

        # Flag the cell as containing
        # a 'mis-hit' weed clump.
        board.get_cell_by_index(cell_id).flag()

        # Have overstepped the mark,
        # so do nothing to the countdown...
        return weeds_in

    else:

        # Kill the cell most recently hit.
        board.get_cell_by_index(cell_id).kill()

        return current_countdown

def display_screen(display, file_names):

    for name in file_names:

        # Fill the screen with black
        # ink.
        display.fill([0, 0, 0])
        
        # Draw the splash screen in the
        # game window.
        display.blit(name, (0, 0))
        
        pygame.time.delay(60)

        pygame.display.update()

# Call the main function.
main()
