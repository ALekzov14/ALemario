import pygame
from pygame.locals import *
from Settings import player_left,player_right,x_position,y_position,movement

# initiate pygame and give permission
# to use pygame's functionality.
clock = pygame.time.Clock()
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((800, 700))

player_count = 0

# Add caption in the window
pygame.display.set_caption('ALemario')

# Initializing the clock
# Clocks are used to track and
# control the frame-rate of a game


# Add player sprite
image = pygame.image.load(r'../Sprite/Mem1.png')

# Creating an Infinite loop
run = True

animate_left = False
animate_right = False
animation_frame = 0 #Номер анимации

is_jump = False
jump_count = 7

while run:
    # Filling the background with
    # white color
    window.fill((0, 0, 0))

    key_pressed_is = pygame.key.get_pressed()
    if key_pressed_is[pygame.K_LEFT]:
        animate_left = True
        animate_right = False
    elif key_pressed_is[pygame.K_RIGHT]:
        animate_left = False
        animate_right = True
    else:
        animate_left = False
        animate_right = False

    # Animation
    if animate_left:
        animation_frame = (animation_frame + 1) % len(player_left)
        window.blit(player_left[animation_frame], (x_position, y_position))
    elif animate_right:
        animation_frame = (animation_frame + 1) % len(player_right)
        window.blit(player_right[animation_frame], (x_position, y_position))
    else:
        window.blit(image, (x_position, y_position))

    if player_count == 1:
        player_count = 0
    else:
        player_count += 1

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
        # Closing the window and program if the
        # type of the event is QUIT
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

    # Changing the coordinates
    # of the player
    if key_pressed_is[K_LEFT] and x_position > 10:
        x_position -= movement
    if key_pressed_is[K_RIGHT] and x_position < 700:
        x_position += movement
    if not is_jump:
        if key_pressed_is[K_UP]:
            is_jump = True
    else:
        if jump_count >= -7:
            if jump_count > 0:
                y_position -= (jump_count ** 2) / 2
            else:
                y_position += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 7

    # Draws the surface object to the screen.
    pygame.display.update()