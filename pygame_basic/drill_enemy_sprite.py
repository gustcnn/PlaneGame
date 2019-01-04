#--*--coding:utf-8
#Author:cnn
#演练游戏精灵
#--*--coding:utf-8
#Author:cnn
import pygame
import os
import sys
from pygame_basic.enemy_plane_sprites import *

pygame.init()
#创建主窗口
screen_x=480
screen_y=600
screen=pygame.display.set_mode((screen_x,screen_y))
object_path=os.path.dirname(os.path.dirname(__file__))
#加载背景图片
bg=pygame.image.load(object_path+"/images/bg.jpg")
#绘制背景图片
screen.blit(bg,(0,0))
hero_plane=pygame.image.load(object_path+"/images/hero.gif")
hero_x=200
hero_y=400
plane_width=100
plane_height=124
screen.blit(hero_plane,(hero_x,hero_y))
pygame.display.update()
#创建时钟对象
clock=pygame.time.Clock()
hero_rect=pygame.Rect(hero_x,hero_y,plane_width,plane_height)
enemy_01=GameSprite(object_path + "/images/enemy0.png", 1)
enemy_02=GameSprite(object_path+"/images/enemy1.png",2)
enemy_group=pygame.sprite.Group(enemy_01,enemy_02)
while True:
    clock.tick(60)#每秒执行60次
    if hero_rect.y+plane_height<=0:#y坐标+飞机的高度<=0的时候,飞机完全出去到窗口外
        hero_rect.y=screen_y-plane_height
    hero_rect.y-=1
    #先加载背景,否则有飞机路径痕迹
    screen.blit(bg,(0,0))
    # enemy_01.update()
    # enemy_02.update()
    #让组中所有精灵更新方法
    enemy_group.update()
    #将所有精灵绘制到screen上
    enemy_group.draw(screen)
    #在屏幕上更新飞机
    screen.blit(hero_plane,(hero_rect.x,hero_rect.y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

