'''
major comment cutting needed
major fixups required
'''


import ctypes
import pathlib
import pygame
import random
import time

pygame.init()

# dimentions of the mindows, measured in pixles (constants)
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# colours
# RGB values (R, G, B)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BALL_COLOUR = (255, 255, 255)
PADDLE_COLOUR = (255, 255, 255)
BACKROUND_MAINMENU_COLOUR = (0, 100, 100)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# score (how many times you hit the paddle)
score = 0

# Dimentions of the paddle
PADDLE_HEIGHT = 150
PADDLE_WIDTH = 3
# dimentinos of the ball
BALL_HEIGHT = 10
BALL_WIDTH = 10

# creats the actual game window
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
# The name of the game window
pygame.display.set_caption('Pong For One Person')

clock = pygame.time.Clock()

# function for counting score


def Balls_Hit(score):
    # font and font size
    font = pygame.font.SysFont('freesansbold.ttf', 60)
    # displays the text on screen and makes sure the score counts up
    text = font.render('Score: ' + str(score) + '/15', True, GREEN)
    # displays the text at x(300) and y(0)
    gameDisplay.blit(text, (290, 0))

# change text colours using RGB values


def textObjects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

# text for the main menu
# displays font, size and colour


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText

# main


def main():

    menu = True
    # sets the defualt option as 'start'
    selected = "start"

    # controls user input
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # detects when keys are pressed down
            if event.type == pygame.KEYDOWN:
                # if the left arrow key is pressed
                if event.key == pygame.K_LEFT:
                    # selecs start when the left arrow is pressed
                    selected = "start"
                # if the right arrow key is pressed
                elif event.key == pygame.K_RIGHT:
                    # selects the quit option if right arrow key is pressed
                    selected = "quit"

                # detects when enter key is pressed
                if event.key == pygame.K_RETURN:
                    # when start is selected and key enter is pressed
                    if selected == "start":
                        print("Start")
                        # runs the main function and starts the game when selected
                        gameloop_paddle()
                    # when quit is selected and key enter is pressed
                    if selected == "quit":
                        pygame.quit()
                        # quits the game when selected
                        quit()

        # main menu user interface
        # fills the backround with the specified colour
        gameDisplay.fill(BACKROUND_MAINMENU_COLOUR)
        # sets the 'title' text font size and colour
        title = text_format("Pong - Main Menu", 'freesansbold.ttf', 80, WHITE)
        # sets the 'how to win' text font size and colour
        howtowin = text_format(
            "Get 15 points to win. Each time the ball hits the paddle, it gets harder", 'freesansbold.ttf', 20, YELLOW)
        # sets the 'rules' text font size and colour
        rules = text_format(
            "Press right and left to choose. When 'QUIT' or 'START' is green, press enter.", 'freesansbold.ttf', 20, YELLOW)

        # the following lines of code tells the user which one (either play or quit) is chosen
        if selected == "start":
            # when you are about to select start, the text turns green
            text_start = text_format("START", 'freesansbold.ttf', 75, GREEN)
        else:
            # when start is deselected, the texy turns back to white
            text_start = text_format("START", 'freesansbold.ttf', 75, WHITE)
        if selected == "quit":
            # when you are about to select quit, the text turns green
            text_quit = text_format("QUIT", 'freesansbold.ttf', 75, GREEN)
        else:
            # when quit is deselected, the text turns back to white
            text_quit = text_format("QUIT", 'freesansbold.ttf', 75, WHITE)

        # folowing line of code creates the text that the user reads in the main menu
        title_rect = title.get_rect()
        howtowin_rect = howtowin.get_rect()
        rules_rect = rules.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        # following lines of code displats the co-ordinates of the text
        gameDisplay.blit(title, (DISPLAY_WIDTH/2 - (title_rect[2]/2), 80))
        gameDisplay.blit(howtowin, (415 - (title_rect[2]/2), 200))
        gameDisplay.blit(rules, (380 - (title_rect[2]/2), 230))
        gameDisplay.blit(text_start, (280 - (start_rect[2]/2), 300))
        gameDisplay.blit(text_quit, (530 - (quit_rect[2]/2), 300))
        # updates the screen display
        pygame.display.update()
        # frames per second
        clock.tick(60)

# function for displayin text


def messageDisplay(text, y_position):
    # font
    largeText = pygame.font.Font(('freesansbold.ttf'), 75)
    # text size (115)
    textSurf, textRect = textObjects(text, largeText)
    textRect.center = ((DISPLAY_WIDTH/2), (y_position))
    # Tells us where to put the message (middle of screen)
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    # immediately updates the screen
    time.sleep(5)
    # restart game
    main()

# dunction defining paddle's x position, y position, paddle width, paddle height, and the colour


def paddle(x_location_paddle, y_location_paddle, PADDLE_COLOUR):
    pygame.draw.rect(gameDisplay, PADDLE_COLOUR, (x_location_paddle,
                                                  y_location_paddle, PADDLE_WIDTH, PADDLE_HEIGHT))

# dunction defining ball's x position, y position, ball width, ball height, and the colour


def ball(x_location_ball, y_location_ball, BALL_COLOUR):
    pygame.draw.rect(gameDisplay, BALL_COLOUR, (x_location_ball,
                                                y_location_ball, BALL_WIDTH, BALL_HEIGHT))

# most important function
# main function


def gameloop_paddle():
    # global variables allows the variabels to be visible througout the entire program
    # It recognizes the variables os the same declares at the top of the screen
    global PADDLE_HEIGHT, PADDLE_COLOUR, BALL_COLOUR

    # Variable Declatations
    # colour (RGB values)
    BALL_COLOUR = (255, 255, 255)
    PADDLE_COLOUR = (255, 255, 255)
    GREEN = (0, 255, 0)

    # variable for score
    score = 0
    # variable to make the colour of an object to transform into another colour
    colour_incriment = 0

    # Paddle and ball dimentions
    PADDLE_HEIGHT = 150
    PADDLE_WIDTH = 2
    BALL_HEIGHT = 10
    BALL_WIDTH = 10
    # current x and y position of paddle
    x_location_paddle = 760
    y_location_paddle = 100
    # current x and y position of ball
    x_location_ball = 400
    y_location_ball = 300

    # velocity of the paddle
    yVelocityPaddle = 0
    # x and y velocity of the ball
    ballSpeedX = 5
    ballSpeedY = -5

    gameExit = False

    # checks if the paddle is on screen and allows for keyboard input
    while gameExit == False:
        # turns the screen black
        gameDisplay.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                # following code allows the user to move up and down
                if event.key == pygame.K_UP:
                    yVelocityPaddle = -10  # lets the paddle move when the user presses up and down
                elif event.key == pygame.K_DOWN:
                    yVelocityPaddle = 10

            if event.type == pygame.KEYUP:
                # when key goes up, it sets the velocity to zero, so the car does not go on forever
                if event.key == pygame.K_UP:
                    yVelocityPaddle = 0  # stops the paddle when the key is not pressed
                elif event.key == pygame.K_DOWN:
                    yVelocityPaddle = 0

        # makes sures that the paddle moves
        y_location_paddle = y_location_paddle + yVelocityPaddle
        # draws the paddle and the ball on screen
        paddle(x_location_paddle, y_location_paddle, PADDLE_COLOUR)
        ball(x_location_ball, y_location_ball, BALL_COLOUR)

        # call the funtion that keeps track of the score
        Balls_Hit(score)

        # makes the ball move up and down
        y_location_ball = y_location_ball + ballSpeedY
        x_location_ball = x_location_ball + ballSpeedX

        # display updating and frames per second
        pygame.display.update()
        clock.tick(60)

        # collision detection: prevents the ball from leaving the screen by setting the velocity to zero once the paddle its the screen
        if y_location_paddle > DISPLAY_HEIGHT - PADDLE_HEIGHT or y_location_paddle < 0:
            y_location_paddle = y_location_paddle - yVelocityPaddle

        # collision detection: if ball hits top or bottom edge
        if y_location_ball > (DISPLAY_HEIGHT - BALL_HEIGHT) or y_location_ball < 0:
            # makes the ball bounce by flipping its y velocity
            ballSpeedY *= -1

        # collision detection: if ball hits leftmost edge
        if x_location_ball < 0:
            # makes the ball bounce by flipping its x velocity
            ballSpeedX *= -1

        # collision detection: if the ball passes beyond the paddle and hits the rightmost edge
        if x_location_ball > DISPLAY_WIDTH:
            # the main menu function is called within the messageDisplay function
            messageDisplay('GAME OVER', 300)

        # if the ball is in the range of the paddle. I.e. collision detection to hit the paddle (front and edges)
        if x_location_ball + BALL_WIDTH >= x_location_paddle and x_location_ball <= x_location_paddle and y_location_ball < y_location_paddle + PADDLE_HEIGHT and y_location_ball + BALL_HEIGHT > y_location_paddle and ballSpeedX > 0:
            # Ball x speed gets facter each time, inreiment by a random value (1, or 2) after bouning off the paddle in an opposite direction
            ballSpeedX = (ballSpeedX + random.randint(1, 2)) * -1
            # Ball speed gets facter each time
            # makes sure that the ball boucnes in the right direction
            if ballSpeedY > 0:
                ballSpeedY = random.randint(1, 5)
            else:
                ballSpeedY = random.randint(1, 5) * -1

            colour_incriment = colour_incriment + 16
            # makes sure the colour value does not turn negaive
            if colour_incriment > 255:
                colour_incriment = 255

            # paddle height gets smaller each time ball hits the paddle
            PADDLE_HEIGHT = PADDLE_HEIGHT - 10
            # turn the paddle colour a bit red each time it hits
            PADDLE_COLOUR = (255, 255 - colour_incriment,
                             255 - colour_incriment)
            # Makes the ball darker each time (harder to see)
            BALL_COLOUR = (255 - colour_incriment, 255 -
                           colour_incriment, 255 - colour_incriment)
            # score add 1 each time ball hits the paddle
            score = score + 1

        if score == 15 and x_location_ball < 700:  # makes sure the score is actually display 15 once you win
            # if statement for winning
            # the main menu function is called within the messageDisplay function
            messageDisplay('YOU WON', 300)
