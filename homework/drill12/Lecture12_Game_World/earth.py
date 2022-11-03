from pico2d import *


class Earth:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 20)

    def update(self):
        pass


