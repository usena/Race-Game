import pygame

class TrackSelection:
    def __init__(self, tracks):
        """
        Initialize the TrackSelection object.

        :param tracks: A dictionary containing track names as keys and corresponding image paths as values.
        """
        self.screen_width = 1200
        self.screen_height = 900
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Track Selection")
        self.selected_track = None
        self.tracks = tracks
        self.font = pygame.font.Font(None, 36)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen.fill((16, 16, 16))
        self.start_x = (self.screen_width - (350 * 2)) // 2
        self.start_y = (self.screen_height - (320 * 2)) // 2

    def draw_track_menu(self):
        """
        Draw the track selection menu on the screen.

        Displays a list of tracks with buttons for selection.

        """
        track_text = self.font.render("Choose a Track:", True, (250, 250, 250))
        self.screen.blit(track_text, (self.screen_width // 2 - 100, 50))

        # Draw track buttons (two per row)
        for i, (track, (track_x, track_y)) in enumerate(self.tracks.items()):
            track_rect = pygame.Rect(self.start_x + (i % 2) * 400, self.start_y + (i // 2) * 400, 300, 300)
            track_img = pygame.image.load(track_x)
            track_img_original = pygame.transform.scale(track_img, (300, 300))  # Original size

            self.screen.blit(track_img_original, (self.start_x + 10 + (i % 2) * 400, self.start_y + 10 + (i // 2) * 400))

            if self.selected_track == track:
                pygame.draw.rect(self.screen, (248, 232, 35), track_rect, 3)

        pygame.display.flip()
