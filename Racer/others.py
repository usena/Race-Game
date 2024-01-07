import pygame

def scale_image(img, factor):
    """
    Scale the given image by a specified factor.

    :param img: The original pygame image.
    :param factor: The scaling factor.
    :return: The scaled pygame image.
    """
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

def blit_rotate_center(display, image, top_left, angle):
    """
    Rotate and blit an image onto the display around its center.

    :param display: The pygame display surface.
    :param image: The image to rotate and blit.
    :param top_left: The top-left position of the image.
    :param angle: The rotation angle in degrees.
    """
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    display.blit(rotated_image, new_rect.topleft)

def draw(screen, asset, player_car):
    """
    Draw the game elements on the screen.

    :param screen: The pygame display surface.
    :param asset: A list of tuples, each containing an image and its position.
    :param player_car: The player's car object.
    """
    # Draw background images
    for img, pos in asset:
        screen.blit(img, pos)
    
    # Draw the player's car on top of the background
    player_car.draw(screen)

    # Update the display
    pygame.display.update()
