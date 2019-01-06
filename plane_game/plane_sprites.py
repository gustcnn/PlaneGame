# --*--coding:utf-8
# Author:cnn
import pygame
from pygame.sprite import Sprite
import os
from time import sleep
import random

#屏幕坐标即宽度、高度
SCREEN_RECT = pygame.Rect(0, 0, 480, 600)
#每秒刷新60次
FRAME_PER_SEC = 60
#定时器常量
ENEMY_TIMER_EVENT = pygame.USEREVENT

class GameSprite(Sprite):
    # def __init__(self,img_path,hero_x,hero_y,hero_width,hero_height):
    object_path = os.path.dirname(os.path.dirname(__file__))

    def __init__(self, img_path, *args, speed=1):
        super().__init__()
        self.image = pygame.image.load(img_path)
        # self.rect=pygame.Rect(hero_x,hero_y,hero_width,hero_height)
        self.rect = pygame.Rect(args)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class BackgroundSprite(GameSprite):
    """
    背景精灵类
    """

    def __init__(self, is_alt=False):
        """
        :param is_alt: 是否是交替图片
        """
        super().__init__(BackgroundSprite.object_path + "/images/background.png", SCREEN_RECT, speed=3)
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        """
        修改y坐标
        :return:
        """
        super().update()
        # 判断图片是否移除屏幕,移除屏幕的话,将图片放到屏幕正上方,以实现滚动效果
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class PlaneSprite(GameSprite):
    pos = (200, 400, 120, 124)

    def __init__(self):
        super().__init__(PlaneSprite.object_path + "/images/hero.gif", PlaneSprite.pos, speed=2)

    def update(self):
        pass


class EnemySprite(GameSprite):


    def __init__(self):
        #调用父类初始化放阿飞
        #随机初始化位置
        #随机初始化速度
        pos_0 = (0, 0, 120, 124)
        random_x = round(random.uniform(0, SCREEN_RECT.width), 2)
        # random_x = random.randint(0,SCREEN_RECT.x)
        list_pos = list(pos_0)
        list_pos[0] = random_x
        random_tuple_pos = tuple(list_pos)
        random_speed=random.randint(1,5)
        super().__init__(EnemySprite.object_path + "/images/enemy0.png",random_tuple_pos,speed=random_speed)
        #print(EnemySprite.random_tuple_pos)
    def update(self):
        super().update()
        if self.rect.y>=SCREEN_RECT.height:
            print("敌机飞出屏幕,从精灵组删除")


pass
if __name__ == '__main__':
    #pos = (200, 400, 120, 124)
    #hero = GameSprite("D:/python/script/PlaneGame/images/hero.gif", pos)
    print(EnemySprite.random_pos)