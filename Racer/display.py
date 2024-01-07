import pygame
from others import *
from car import *

class LoadAsset:
    def __init__(self, track, track_border, grass, finish):
        """
        Initialize the LoadAsset object with the provided images.

        :param track: Path to the track image.
        :param track_border: Path to the track border image.
        :param grass: Path to the grass image.
        :param finish: Path to the finish line image.
        """
        self.FPS = 60
        self.clock = pygame.time.Clock().tick(self.FPS)
        self.track = pygame.image.load(track)
        self.track_border = pygame.image.load(track_border)
        self.grass = pygame.image.load(grass)
        self.finish = pygame.image.load(finish)
        self.asset = [(self.grass, (0, 0)), (self.track, (0, 0)), (self.finish, (0, 0)), (self.track_border, (0, 0))]
        self.screen = pygame.display.set_mode((self.track.get_width(), self.track.get_height()))

    def scale_grass(self, factor):
        """
        Scale the grass image by the given factor.

        :param factor: Scaling factor.
        """
        self.grass = scale_image(self.grass, factor)
        self.asset[0] = (self.grass, (0, 0))

    def scale_finish(self, factor):
        """
        Scale the finish line image by the given factor.

        :param factor: Scaling factor.
        """
        self.finish = scale_image(self.finish, factor)
        self.asset[2] = (self.finish, self.finish_position)

    def set_finish(self, x, y):
        """
        Set the position of the finish line.

        :param x: X-coordinate of the finish line.
        :param y: Y-coordinate of the finish line.
        """
        self.finish_position = (x, y)
        self.asset[2] = (self.finish, self.finish_position)
