import pygame

pygame.init()

# Set Width and Height
screenWidth, screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
# screenWidth = 100
# screenHeight = 100

# Player one
playerOnePosX=screenWidth/2-1
playerOnePosY=screenHeight-50

# Player Two
playerTwoPosX=screenWidth-50
playerTwoPosY=screenHeight/2-1

# Player Three
playerThreePosX=screenWidth/2-1
playerThreePosY=50

# Player Four
playerFourPosX=50
playerFourPosY=screenHeight/2-1

# Player intro text offset
playerIntroTextOffset = 180
playerIntroTextOffsetFromBorder = 100