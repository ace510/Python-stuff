import pygame
import random

# Defining colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# 640 by 480 is default screen size
size = (640, 480)
screen = pygame.display.set_mode(size)
HACK_FONT = pygame.font.SysFont('Hack', 22, False, False)
rect_x = 50
rect_y = 50
rect_change_x = 3
rect_change_y = 2
snow_list = []
snow_drift = [-1, 0, 1]

for i in range(150):
    x = random.randrange(0, 640)
    y = random.randrange(0, 480)
    snow_list.append([x, y])


def abs_increment(number):
    """this function increments a number away from 0"""
    if number < 0:
        number -= 1
    elif number >= 0:
        number += 1
    else:
        print 'improper number given'
    return number


def abs_decrement(number):
    """this function decrements a number towards zero"""
    if number <= 0:
        number += 1
    elif number > 0:
        number -= 1
    else:
        print 'improper input given'
    return number


# this is the name of the game
pygame.display.set_caption('Bouncing Rectangle')

# this code loops until the game closes
done = False

# use this to limit frame rate, RIP CPU
clock = pygame.time.Clock()

# Main game loop
while not done:
    # this loop catches ALL input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game logic goes here (score, timers)
    FPS_count = str(int(clock.get_fps()))
    Game_Timer = str((pygame.time.get_ticks()/1000))
    FPS_counter_text = HACK_FONT.render(FPS_count, False, GREEN)
    Game_Timer_text = HACK_FONT.render(Game_Timer, False, GREEN)

    # Screen clearing happens here, either a solid BLACK, or a BG image
    screen.fill(BLACK)

    # Drawing happens here
    screen.blit(FPS_counter_text, [600, 460])
    screen.blit(Game_Timer_text, [20, 460])

    pygame.draw.rect(screen, RED, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, WHITE, [rect_x + 17, rect_y + 4, 16, 40])
    pygame.draw.rect(screen, WHITE, [rect_x + 5, rect_y + 16, 40, 16])
    if rect_y > 430:
        rect_y = 430
    elif rect_y < 0:
        rect_y = 0

    if rect_x > 590:
        rect_x = 590
    elif rect_x < 0:
        rect_x = 0

    if rect_y == 430 or rect_y == 0:
        rect_change_y = abs_decrement(rect_change_y)
        rect_change_x = abs_increment(rect_change_x)
        rect_change_y = rect_change_y * -1

    if rect_x == 590 or rect_x == 0:
        rect_change_x = abs_decrement(rect_change_x)
        rect_change_y = abs_increment(rect_change_y)
        rect_change_x = rect_change_x * -1

    rect_x += rect_change_x
    rect_y += rect_change_y

    for i in range(len(snow_list)):
        if snow_list[i][1] > 480:
            snow_list[i][1] = random.randrange(-50, 0, 1)
            snow_list[i][0] = random.randrange(0, 640)
        pygame.draw.circle(screen, WHITE, snow_list[i], 1)
        snow_list[i][1] += 1
        snow_list[i][0] += random.choice(snow_drift)

    # screen flips here
    pygame.display.flip()

    # also the screen fps
    clock.tick(60)
# Close the window and quit.
pygame.quit()
