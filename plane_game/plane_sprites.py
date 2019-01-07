# --*--coding:utf-8
# Author:cnn
import pygame
from pygame.sprite import Sprite
import os
from time import sleep
import random
import pygame.font

# 屏幕坐标即宽度、高度
SCREEN_RECT = pygame.Rect(0, 0, 480, 600)
# 每秒刷新60次
FRAME_PER_SEC = 60
# 定时器常量
ENEMY_TIMER_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1  # 因为上面已经调用了,所以此处需要eventid+1,不然是同一个了


class GameSprite(Sprite):
    # def __init__(self,img_path,hero_x,hero_y,hero_width,hero_height):
    object_path = os.path.dirname(os.path.dirname(__file__))

    def __init__(self, img_path, speed=1):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
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
        super().__init__(BackgroundSprite.object_path + "/images/background.png", speed=2)
        if is_alt:
            self.rect.y = -self.rect.height

class GameOverBackground(GameSprite):
    """
    背景精灵类
    """

    def __init__(self, is_alt=False):
        """
        :param is_alt: 是否是交替图片
        """
        super().__init__(BackgroundSprite.object_path + "/images/gameover.png", speed=0)
        self.rect=self.image.get_rect()


class PlaneSprite(GameSprite):
    # pos = (200, 400, 120, 124)

    def __init__(self):
        # 调用父类方法
        super().__init__(PlaneSprite.object_path + "/images/hero.gif", speed=0)
        # 设置英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        pass

    def move(self, key):
        if key == pygame.K_RIGHT:
            self.speed += 2
        elif key == pygame.K_LEFT:
            self.speed -= 2
        else:
            self.speed = 0
        # 更改x坐标
        self.rect.x += self.speed
        # 控制边界
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        if self.rect.x < 0:
            self.rect.x = 0

    def fire(self):
        # print("发射子弹")
        for i in (1, 2, 3):
            bullet = Bullet()
            if i == 1:
                bullet.rect.bottom = self.rect.y - 5
            elif i == 2:
                bullet.rect.bottom = self.rect.y - 30
            elif i == 3:
                bullet.rect.bottom = self.rect.y - 55
            # bullet.rect.bottom=self.rect.y-i*20
            bullet.rect.centerx = self.rect.centerx
            self.bullet_group.add(bullet)


class EnemySprite(GameSprite):
    def __init__(self):
        # 调用父类初始化图片
        super().__init__(EnemySprite.object_path + "/images/enemy0.png")
        # super().__init__(EnemySprite.object_path + "/images/enemy0.png")
        # 随机初始化位置
        # 设置y方向的初始位置
        self.rect.bottom = 0
        # y=-height,否则图片很突然的就出现了
        # x最大值,屏幕宽度-飞机图片宽度
        max_x = SCREEN_RECT.width - self.rect.width
        # self.rect.bottom=0
        # 随机初始化速度
        # pos_0 = (0,-124, 120, 124)
        random_x = round(random.uniform(0, max_x), 2)
        # random_x = random.randint(0,SCREEN_RECT.x)
        # list_pos = list(pos_0)
        # list_pos[0] = random_x
        # random_tuple_pos = tuple(list_pos)

        random_speed = random.randint(1, 3)
        # 更改速度
        self.speed = random_speed
        # 更改x坐标
        self.rect.x = random_x

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            # print("敌机飞出屏幕,从精灵组删除")
            self.kill()  # 将精灵从所有精灵组中删除

    def __del__(self):
        # print("敌机%s挂了"%self.rect)
        pass


class Bullet(GameSprite):
    def __init__(self):
        # 子弹初始速度-2,向上飞
        super().__init__(GameSprite.object_path + "/images/bullet-1.gif", -2)

    def update(self):
        # 调用父类方法,使得子弹垂直运行
        super().update()
        # 飞出屏幕,从内存清除
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # print("子弹%s消失了" % self.rect)
        pass


pass
if __name__ == '__main__':
    # pos = (200, 400, 120, 124)
    # hero = GameSprite("D:/python/script/PlaneGame/images/hero.gif", pos)
    pass
