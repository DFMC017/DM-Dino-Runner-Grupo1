import random
from components.obstacle import Obstacle

class Bird(Obstacle):
    
    def __init__(self, image):
        self.index = random.randint(0,1)
        super().__init__(image, self.index)
        self.rect.x = random.randint(100, 1100)
        self.rect.y = 150

        