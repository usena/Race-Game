import pygame

def move_player(player_car):
    """
    Update the position and orientation of the player car based on user input.

    :param player_car: The player's car object.
    """
    keys = pygame.key.get_pressed()
    moved = False

    # Rotate the car based on left and right arrow keys
    if keys[pygame.K_LEFT]:
        player_car.rotate(left=True)
    if keys[pygame.K_RIGHT]:
        player_car.rotate(right=True)

    # Move the car forward with different levels of acceleration based on numeric keys (1, 2, 3)
    if keys[pygame.K_1]:
        moved = True
        player_car.move_forward(1)
    if keys[pygame.K_2]:
        moved = True
        player_car.move_forward(2)
    if keys[pygame.K_3]:
        moved = True
        player_car.move_forward(3)

    # Move the car backward with deceleration when the spacebar is pressed
    if keys[pygame.K_SPACE]:
        moved = True
        player_car.move_backward()

    # If no movement keys are pressed, gradually reduce the car's speed
    if not moved:
        player_car.reduce_speed()
