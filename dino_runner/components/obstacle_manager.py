import pygame
from components.cactus import Cactus
from components.bird import Bird
from utils.constants import LARGE_CACTUS, SMALL_CACTUS
from utils.constants import BIRD

class ObstacleManager():
    
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            
            self.obstacles.append(Bird(BIRD))
            self.obstacles.append(Cactus(SMALL_CACTUS)) or self.obstacles.append(Cactus(LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.dinosaur.dino_rect.colliderect(obstacle.rect):
                if not game.dinosaur_shield:
                    pygame.time.delay(300)
                    game.playing = False
                else:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []