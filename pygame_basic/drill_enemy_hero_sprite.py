# --*--coding:utf-8
# Author:cnn
# 演练游戏精灵
# --*--coding:utf-8
# Author:cnn
import pygame
import os
import sys
from pygame_basic.enemy_plane_sprites import *
from pygame_basic.hero_plane_sprites import *

pygame.init()
# 创建主窗口
screen_x = 480
screen_y = 600
hero_x = 200
hero_y = 400
plane_width = 100
plane_height = 124
screen = pygame.display.set_mode((screen_x, screen_y))
object_path = os.path.dirname(os.path.dirname(__file__))
# 加载背景图片
bg = pygame.image.load(object_path + "/images/bg.jpg")
# 绘制背景图片
screen.blit(bg, (0, 0))
pygame.display.update()
# 创建时钟对象
clock = pygame.time.Clock()
enemy_01 = GameSprite(object_path + "/images/enemy0.png", 1)
enemy_02 = GameSprite(object_path + "/images/enemy1.png", 2)
enemy_group = pygame.sprite.Group(enemy_01, enemy_02)
hero_plane = HeroPlaneSprite(object_path + "/images/hero.gif",
                             hero_x, hero_y, plane_width, plane_height,3)
hero_group=pygame.sprite.Group(hero_plane)
while True:
    clock.tick(60)  # 每秒执行60次

    # 先加载背景,否则有飞机路径痕迹
    screen.blit(bg, (0, 0))
    # 让组中所有敌人精灵更新方法
    enemy_group.update()
    #组中飞机精灵更新方法
    hero_group.update()
    #将飞机精灵绘制到screen上
    hero_group.draw(screen)
    # 将所有精灵绘制到screen上
    enemy_group.draw(screen)
    # 在屏幕上更新飞机
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()