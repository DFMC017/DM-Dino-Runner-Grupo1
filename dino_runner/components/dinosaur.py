from pygame.sprite import Sprite
from utils.constants import RUNNING
from time import sleep

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 475

    def __init__(self):
        self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.image = RUNNING[0] if self.step_index < 6 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def update(self):
        self.run()