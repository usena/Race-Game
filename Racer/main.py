import pygame
import sys
from others import *  # Assuming this contains necessary functions, adjust as needed
from display import *
from car import *
from move_keys import *
from track_selection import *
from car_selection import *
import time

# Constants
PHASE_TRACK_SELECTION = 0
PHASE_CAR_SELECTION = 1
PHASE_RACE = 2

# Dictionary containing track information (image paths)
tracks = {
    "track_1": ("D:\\CS_Major\\Python\\Racer\\image\\track.png", "D:\\CS_Major\\Python\\Racer\\image\\track-border.png"),
    "track_2": ("D:\\CS_Major\\Python\\Racer\\image\\track1.png", "D:\\CS_Major\\Python\\Racer\\image\\track-border1.png"),
    "track_3": ("D:\\CS_Major\\Python\\Racer\\image\\track2.png", "D:\\CS_Major\\Python\\Racer\\image\\track-border2.png"),
    "track_4": ("D:\\CS_Major\\Python\\Racer\\image\\track3.png", "D:\\CS_Major\\Python\\Racer\\image\\track-border3.png"),
}

# List containing car image paths
cars = ["D:\CS_Major\Python\Racer\image/blue-car.png", "D:\CS_Major\Python\Racer\image/purple-car.png", "D:\CS_Major\Python\Racer\image/green-car.png"]

# Initialize pygame
pygame.init()

# Function for the track selection phase
def track_selection_phase():
    track_selection = TrackSelection(tracks)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, (track, (track_x, track_y)) in enumerate(tracks.items()):
                    track_rect = pygame.Rect(track_selection.start_x + (i % 2) * 400, track_selection.start_y + (i // 2) * 400, 300, 300)
                    if track_rect.collidepoint(event.pos):
                        track_selection.selected_track = track
                        return track_selection.selected_track, track_x, track_y

        track_selection.draw_track_menu()

# Function for the car selection phase
def car_selection_phase():
    car_selection = CarSelection(cars)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, car in enumerate(cars):
                    car_rect = pygame.Rect(car_selection.start_x + (i % 2) * 400, car_selection.start_y + (i // 2) * 400, 300, 300)
                    if car_rect.collidepoint(event.pos):
                        car_selection.selected_car = car
                        return car_selection.selected_car

        car_selection.draw_car_menu()

# Function for the race phase
def race_phase(track, track_x, track_y, selected_car):
    pygame.display.set_caption("Racer")
    game_asset = LoadAsset(track_x, track_y, "D:\CS_Major\Python\Racer\image/grass.webp", "D:\CS_Major\Python\Racer\image/finish.png")
    lap_start_time = time.time()
    # Set up game assets and car based on the selected track
    if track == "track_1":
        game_asset.scale_grass(2)
        game_asset.set_finish(375, 727.5)
        game_car = Collision(selected_car, 4, 4)
        game_car.scale_car(0.05)
        game_car.position_car(550, 755)
    elif track == "track_2":
        game_asset.scale_grass(2)
        game_asset.set_finish(350, 480)
        game_car = Collision(selected_car, 4, 4)
        game_car.scale_car(0.05)
        game_car.position_car(500, 500)
    elif track == "track_3":
        game_asset.scale_grass(3)
        game_asset.set_finish(375, 130)
        game_car = Collision(selected_car, 4, 4)
        game_car.scale_car(0.05)
        game_car.position_car(550, 150)
    elif track == "track_4":
        game_asset.scale_grass(2)
        game_asset.set_finish(280, 230)
        game_car = Collision(selected_car, 4, 4)
        game_car.scale_car(0.05)
        game_car.position_car(360, 260)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        move_player(game_car)
        draw(game_asset.screen, game_asset.asset, game_car)
        font = pygame.font.Font(None,36)
        pygame.display.flip()
        finish_mask = pygame.mask.from_surface(game_asset.finish)
        track_mask = pygame.mask.from_surface(game_asset.track_border)
        if game_car.collide(track_mask) != None:
            game_car.bounce()
        finish_poi_collide = game_car.collide(finish_mask, *game_asset.finish_position)
        if finish_poi_collide != None:
            if finish_poi_collide[0] == 0:
                lap_time = time.time() - lap_start_time
                time_display = font.render(f'Lap Time: {lap_time:.2f} seconds',True,(255,255,255))
                game_asset.screen.blit(time_display,(10,10))
                print(f'Lap time: {lap_time: .2f} seconds')
                pygame.display.flip()
                time.sleep(3)
                return True  # Restart race
            else:
                game_car.bounce()

# Function to control the overall flow of the game
def run_game():
    phase = PHASE_TRACK_SELECTION
    selected_track = None
    selected_track_x = None
    selected_track_y = None
    selected_car = None

    while True:
        if phase == PHASE_TRACK_SELECTION:
            selected_track, selected_track_x, selected_track_y = track_selection_phase()
            phase = PHASE_CAR_SELECTION

        elif phase == PHASE_CAR_SELECTION:
            selected_car = car_selection_phase()
            phase = PHASE_RACE

        elif phase == PHASE_RACE:
            restart_race = race_phase(selected_track, selected_track_x, selected_track_y, selected_car)
            if not restart_race:
                phase = PHASE_TRACK_SELECTION

# Run the game if the script is executed directly
if __name__ == "__main__":
    run_game()
