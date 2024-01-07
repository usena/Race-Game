import pygame
import math
from others import *
from display import *

class Car:
    def __init__(self, car, max_vel, rotation_vel):
        """
        Initialize the Car object with the given parameters.

        :param car: Path to the image file for the car.
        :param max_vel: Maximum velocity of the car.
        :param rotation_vel: Velocity at which the car can rotate.
        """
        self.car = pygame.image.load(car)
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = -90
        self.START_POS = (0, 0)
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def scale_car(self, factor):
        """
        Scale the car image by the given factor.

        :param factor: Scaling factor.
        """
        self.car = scale_image(self.car, factor)

    def position_car(self, x, y):
        """
        Set the initial position of the car.

        :param x: X-coordinate of the starting position.
        :param y: Y-coordinate of the starting position.
        """
        self.START_POS = x, y
        self.x, self.y = self.START_POS

    def rotate(self, left=False, right=False):
        """
        Rotate the car left or right based on the boolean flags.

        :param left: Rotate left if True.
        :param right: Rotate right if True.
        """
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, display):
        """
        Draw the car on the specified display.

        :param display: Pygame display surface.
        """
        blit_rotate_center(display, self.car, (self.x, self.y), self.angle)

    def move_forward(self, level):
        """
        Move the car forward with acceleration based on the given level.

        :param level: Acceleration level.
        """
        self.vel = min(self.vel + self.acceleration, self.max_vel + (1 * level))
        self.move()

    def move_backward(self):
        """Move the car backward with deceleration."""
        self.vel = max(self.vel - self.acceleration, -self.max_vel / 2)
        self.move()

    def move(self):
        """Move the car based on its current velocity and angle."""
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reset(self):
        """Reset the car's position and angle to the starting position."""
        self.x, self.y = self.START_POS
        self.angle = -90
        self.vel = 0

    def reduce_speed(self):
        """Reduce the car's speed through deceleration."""
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()


class Collision(Car):
    def collide(self, mask, x=0, y=0):
        """
        Check for collision between the car and another mask.

        :param mask: Pygame mask to check collision against.
        :param x: X-offset for the collision check.
        :param y: Y-offset for the collision check.
        :return: Point of intersection between masks, if any.
        """
        car_mask = pygame.mask.from_surface(self.car)
        margin = 0.1
        offset = (int(self.x - x) - margin, int(self.y - y) - margin)
        point_of_intersection = mask.overlap(car_mask, offset)
        return point_of_intersection

    def bounce(self):
        """Bounce the car back by reversing its velocity."""
        self.vel = -self.vel
        self.move()
