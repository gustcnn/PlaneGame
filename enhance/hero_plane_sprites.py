# --*--coding:utf-8
# Author:cnn
#from 包名.模块名 import 类
from pygame.sprite import Sprite
import pygame


class HeroPlaneSprite(Sprite):
    def __init__(self, img_path, hero_x, hero_y, hero_width, hero_height, speed=1):
        super().__init__()
        self.image=pygame.image.load(img_path)
        #self.rect=args#plane的x,y轴坐标,width,height
        self.rect=pygame.Rect(hero_x, hero_y, hero_width, hero_height)
        self.speed=speed
    def update(self):
        self.rect.y-=self.speed
