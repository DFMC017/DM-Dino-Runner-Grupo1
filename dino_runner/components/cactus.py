import random
from components.obstacle import Obstacle

class Cactus(Obstacle):
    
    def __init__(self, image):
        self.index = random.randint(0,2)
        super().__init__(image, self.index)
        self.rect.y = 320