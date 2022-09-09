import pygame
from utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT
from components.dinosaur import Dinosaur
from components.obstacle_manager import ObstacleManager
from components.power_up_manager import PowerUpManager
from utils import texts_file

class Game:
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.dinosaur = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.working = True
        self.dinosaur_shield = False
        self.power_up_manager = PowerUpManager()

    def execute(self):
        while self.working:
            if not self.playing:
                self.show_menu()

    def run(self):
        self.reset_components()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.working = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.dinosaur.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.dinosaur.draw(self.screen)
        self.show_score()
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
        
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1

        text, text_rect = texts_file.get_score_element(self.points)
        self.screen.blit(text, text_rect)

    def show_menu(self):
        FONT_COLOR_WHITE = (255, 255, 255)

        self.working = True
        self.screen.fill(FONT_COLOR_WHITE)
        self.show_menu_options()
        self.hand_event_menu()
        pygame.display.update()

    def show_menu_options(self):
        text, text_rect = texts_file.get_text_element('PRESIONA CUALQUIER TECLA PARA COMENZAR', HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT)
        self.screen.blit(text, text_rect)

    def hand_event_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.working = False
                pygame.display.quit()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                pygame.mixer.music.load('C:\\Users\\dougl\\Downloads\\PRTDC.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.play(0)
                self.run()
                self.obstacle_manager.obstacles.clear()

    def reset_components(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.points = 0