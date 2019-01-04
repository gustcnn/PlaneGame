# --*--coding:utf-8
# Author:cnn
import pygame
import os


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img_path, speed=1):
        # 不是继承object,都需要首先调用父类的__init__()
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        #print(self.rect)


if __name__ == "__main__":
    object_path = os.path.dirname(os.path.dirname(__file__))
    sprite = GameSprite(object_path + "/images/bg.jpg", 2)
    sprite.update()
    print(sprite.rect)
