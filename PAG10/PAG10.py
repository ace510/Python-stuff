import pygame

# Defining colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


def draw_swiss(pygame_screen, x, y):
    pygame.draw.rect(pygame_screen, RED, [x, y, 50, 50])
    pygame.draw.rect(pygame_screen, WHITE, [x + 17, y + 4, 16, 40])
    pygame.draw.rect(pygame_screen, WHITE, [x + 5, y + 16, 40, 16])


pygame.init()

# 640 by 480 is default screen size
size = (640, 480)
screen = pygame.display.set_mode(size)

# this is the name of the game
pygame.display.set_caption('name o game')

# Make mouse invisible
pygame.mouse.set_visible(False)

# this code is only run once
done = False
x_motion = 0
y_motion = 0

x_coord = 10
y_coord = 10


joystick_count = pygame.joystick.get_count()
controller_enabled = False
if 0 < joystick_count <= 2:
    print 'controller recognized'
    controller_enabled = True
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()


if joystick_count > 2:
    print "Error, game only works with one controller, strangeness may occur"
    controller_enabled = False
elif joystick_count < 0 and joystick_count <= 2:
    print 'controller recognized'
    controller_enabled = True
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()
else:
    controller_enabled = False


# use this to limit frame rate, RIP CPU
clock = pygame.time.Clock()

# Main game loop
while not done:
    # this loop catches ALL input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and controller_enabled is False:
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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_motion = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
                y_motion = 0

    # Game logic goes here (score, timers)
    if controller_enabled is True:
        horiz_axis_pos = my_joystick.get_axis(0)
        vert_axis_pos = my_joystick.get_axis(1)
        x_motion = int(horiz_axis_pos * 3)
        y_motion = int(vert_axis_pos * 3)
    x_coord += x_motion
    y_coord += y_motion

    if x_coord > (size[0]) - 50:
        x_coord = (size[0]) - 50
    elif x_coord < 0:
        x_coord = 0
    if y_coord > (size[1]) - 50:
        y_coord = (size[1]) - 50
    elif y_coord < 0:
        y_coord = 0

    # Screen clearing happens here, either a solid BLACK, or a BG image
    screen.fill(BLACK)

    # Drawing happens here
    draw_swiss(screen, x_coord, y_coord)
    # screen flips here
    pygame.display.flip()

    # also the screen fips
    clock.tick(60)

# Close the window and quit.
pygame.quit()
