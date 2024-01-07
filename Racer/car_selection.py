import pygame

class CarSelection:
    def __init__(self, cars):
        # Initialize the CarSelection object
        self.screen_width = 1200
        self.screen_height = 900
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Car Selection")
        self.selected_car = None
        self.cars = cars
        self.font = pygame.font.Font(None, 36)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen.fill((16, 16, 16))
        self.start_x = (self.screen_width - (350 * 2)) // 2
        self.start_y = (self.screen_height - (320 * 2)) // 2

    def draw_car_menu(self):
        # Draw the car selection menu
        car_text = self.font.render("Choose a Car:", True, (250, 250, 250))
        self.screen.blit(car_text, (self.screen_width // 2 - 100, 50))

        # Draw car buttons (two per row)
        for i, car in enumerate(self.cars):
            car_rect = pygame.Rect(self.start_x + (i % 2) * 400, self.start_y + (i // 2) * 400, 300, 300)
            car_img = pygame.image.load(car)
            car_img_original = pygame.transform.scale(car_img, (300, 300))  # Original size

            self.screen.blit(car_img_original, (self.start_x + 10 + (i % 2) * 400, self.start_y + 10 + (i // 2) * 400))

            # Highlight the selected car with a rectangle
            if self.selected_car == car:
                pygame.draw.rect(self.screen, (248, 232, 35), car_rect, 3)

        pygame.display.flip()
