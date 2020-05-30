'''
fix function order
polish comments?
major fixups required
'''

import pygame
import random
import time

pygame.init()

# Window dimentions
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BALL_COLOUR = (255, 255, 255)
PADDLE_COLOUR = (255, 255, 255)
BACKROUND_MAINMENU_COLOUR = (0, 100, 100)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Score (how many times you hit the paddle)
score = 0

# Paddle dimensions
PADDLE_HEIGHT = 150
PADDLE_WIDTH = 3

# Ball dimensions (square)
BALL_HEIGHT = 10
BALL_WIDTH = 10

# Initializes game window and gives it a name
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Pong For One Person')

clock = pygame.time.Clock()


# Displays current score in gameplay
def Balls_Hit(score):
    font = pygame.font.SysFont('freesansbold.ttf', 60)
    text = font.render('Score: ' + str(score) + '/15', True, GREEN)
    gameDisplay.blit(text, (290, 0))


def textObjects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()


# Text for the main menu
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText


# Main game function
def main():
    # Sets the default option as "start"
    # This is a choice in the main menu
    selected = "start"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # Detects when a key is pressed down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected = "start"
                elif event.key == pygame.K_RIGHT:
                    selected = "quit"

                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        gameloop_paddle()
                    if selected == "quit":
                        pygame.quit()

        # Main menu user interface
        gameDisplay.fill(BACKROUND_MAINMENU_COLOUR)
        title = text_format("Pong - Main Menu", 'freesansbold.ttf', 80, WHITE)
        win_rules = text_format("Get 15 points to win. Each time the ball hits the paddle, it gets harder", 'freesansbold.ttf', 20, YELLOW)
        general_rules = text_format("Press right and left to choose. When 'QUIT' or 'START' is green, press enter.", 'freesansbold.ttf', 20, YELLOW)

        # Formatting the selected option (set font colour to green)
        if selected == "start":
            text_start = text_format("START", 'freesansbold.ttf', 75, GREEN)
        else:
            text_start = text_format("START", 'freesansbold.ttf', 75, WHITE)

        if selected == "quit":
            text_quit = text_format("QUIT", 'freesansbold.ttf', 75, GREEN)
        else:
            text_quit = text_format("QUIT", 'freesansbold.ttf', 75, WHITE)

        # Creates the text to display on main menu
        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        # Sets the coordinates of the text
        gameDisplay.blit(title, (DISPLAY_WIDTH/2 - (title_rect[2]/2), 80))
        gameDisplay.blit(win_rules, (415 - (title_rect[2]/2), 200))
        gameDisplay.blit(general_rules, (380 - (title_rect[2]/2), 230))
        gameDisplay.blit(text_start, (280 - (start_rect[2]/2), 300))
        gameDisplay.blit(text_quit, (530 - (quit_rect[2]/2), 300))

        # Updates the screen display and FPS
        pygame.display.update()
        clock.tick(60)


# Function for displaying text
def messageDisplay(text, y_position):
    largeText = pygame.font.Font(('freesansbold.ttf'), 75)
    textSurf, textRect = textObjects(text, largeText)
    textRect.center = ((DISPLAY_WIDTH/2), (y_position))
    gameDisplay.blit(textSurf, textRect)

    pygame.display.update()
    time.sleep(5)
    main()


# Defining paddle properties
def paddle(x_location_paddle, y_location_paddle, PADDLE_COLOUR):
    pygame.draw.rect(gameDisplay, PADDLE_COLOUR, (x_location_paddle, y_location_paddle, PADDLE_WIDTH, PADDLE_HEIGHT))


# Defining ball properties
def ball(x_location_ball, y_location_ball, BALL_COLOUR):
    pygame.draw.rect(gameDisplay, BALL_COLOUR, (x_location_ball, y_location_ball, BALL_WIDTH, BALL_HEIGHT))


# Game function
def gameloop_paddle():
    global PADDLE_HEIGHT, PADDLE_COLOUR, BALL_COLOUR

    BALL_COLOUR = (255, 255, 255)
    PADDLE_COLOUR = (255, 255, 255)

    # variable for score
    score = 0
    
    # Variable to gradually increase the R value in the RBG values of the paddle
    colour_incriment = 0

    PADDLE_HEIGHT = 150
    PADDLE_WIDTH = 2

    x_location_paddle = 760
    y_location_paddle = 100

    yVelocityPaddle = 0

    BALL_HEIGHT = 10
    BALL_WIDTH = 10

    x_location_ball = 400
    y_location_ball = 300

    ballSpeedX = 5
    ballSpeedY = -5

    while True:
        gameDisplay.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # Allows user to move paddle up and down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    yVelocityPaddle = -10
                elif event.key == pygame.K_DOWN:
                    yVelocityPaddle = 10

            # Only move the paddle if key is pressed down
            if event.type == pygame.KEYUP:
                yVelocityPaddle = 0


        # Moving the paddle
        y_location_paddle += yVelocityPaddle

        # Draws the paddle and the ball on screen
        paddle(x_location_paddle, y_location_paddle, PADDLE_COLOUR)
        ball(x_location_ball, y_location_ball, BALL_COLOUR)

        # Updating the score
        Balls_Hit(score)

        # Moving the ball
        y_location_ball += ballSpeedY
        x_location_ball += ballSpeedX

        pygame.display.update()
        clock.tick(60)

        # Don't let paddle leave the screen
        if y_location_paddle > DISPLAY_HEIGHT - PADDLE_HEIGHT or y_location_paddle < 0:
            y_location_paddle = y_location_paddle - yVelocityPaddle

        # Simulating ball bouncing on bottom and top edge
        if y_location_ball > (DISPLAY_HEIGHT - BALL_HEIGHT) or y_location_ball < 0:
            ballSpeedY *= -1

        # Simulating ball bouncing on left edge
        if x_location_ball < 0:
            ballSpeedX *= -1

        # Simulating ball hitting right edge
        if x_location_ball > DISPLAY_WIDTH:
            messageDisplay('GAME OVER', 300)

        # Simulating ball hitting the paddle
        if x_location_ball + BALL_WIDTH >= x_location_paddle and x_location_ball <= x_location_paddle and y_location_ball < y_location_paddle + PADDLE_HEIGHT and y_location_ball + BALL_HEIGHT > y_location_paddle and ballSpeedX > 0:
            ballSpeedX = (ballSpeedX + random.randint(1, 2)) * -1

            if ballSpeedY > 0:
                ballSpeedY = random.randint(1, 5)
            else:
                ballSpeedY = random.randint(1, 5) * -1

            colour_incriment += 16
            colour_incriment = min(colour_incriment, 255)

            score += 1

            # Simulating paddle shrinking, getting more red, and ball fading
            PADDLE_HEIGHT -= 10
            PADDLE_COLOUR = (255, 255 - colour_incriment, 255 - colour_incriment)
            BALL_COLOUR = (255 - colour_incriment, 255 - colour_incriment, 255 - colour_incriment)

        if score == 15 and x_location_ball < 700:
            messageDisplay('YOU WON', 300)
