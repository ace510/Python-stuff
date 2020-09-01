import pygame

# Defining colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# 640 by 480 is default screen size
size = (480, 640)
screen = pygame.display.set_mode(size)
background_image = pygame.image.load_basic("Background.bmp").convert()

# setting image called Background.bmp as our background, converting it as well
player_img = pygame.image.load_basic("Ship_orange.bmp").convert()
# setting chromakey for player avatar, isn't strictly needed
player_img.set_colorkey(BLACK)

fire_sound = pygame.mixer.Sound("sfx_laser1.ogg")

# this is the name of the game
pygame.display.set_caption("Macog")

# this code loops until the game closes
done = False
x_motion = 0
y_motion = 0

x_coord = 10
y_coord = 10

# use this to limit frame rate, RIP CPU
clock = pygame.time.Clock()

# Main game loop
while not done:
    # this loop catches ALL input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_motion = -3
            elif event.key == pygame.K_RIGHT:
                x_motion = 3
            elif event.key == pygame.K_DOWN:
                y_motion = 3
            elif event.key == pygame.K_UP:
                y_motion = -3
            elif event.key == pygame.K_r:
                x_coord = 0
                y_coord = 0
            elif event.key == pygame.K_x:
                fire_sound.play()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_motion = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_motion = 0

    # Game logic goes here (score, timers)
    x_coord += x_motion
    y_coord += y_motion

    if x_coord > (size[0]) - 112:
        x_coord = (size[0]) - 112
    elif x_coord < 0:
        x_coord = 0
    if y_coord > (size[1]) - 75:
        y_coord = (size[1]) - 75
    elif y_coord < 0:
        y_coord = 0

    # Screen clearing happens here, either a solid BLACK, or a BG image
    screen.blit(background_image, [0, 0])

    # Drawing happens here
    screen.blit(player_img, [x_coord, y_coord])
    # screen flips here
    pygame.display.flip()

    # also the screen fips
    clock.tick(60)

# Close the window and quit.
pygame.quit()
