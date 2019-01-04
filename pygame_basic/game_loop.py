# --*--coding:utf-8
# Author:cnn
import pygame
import os
import sys
from time import sleep

pygame.init()
# 创建主窗口,返回sur
screen = pygame.display.set_mode((480, 600))
project_path = os.path.dirname(os.path.dirname(__file__))
# print(project_path)
# 加载背景图片
bg = pygame.image.load(project_path + "/images/bg.jpg")
# 绘制背景图片
screen.blit(bg, (0, 0))
# 更新屏幕
#pygame.display.update()
# 加载飞机图片
hero_image = pygame.image.load(project_path + "/images/hero.gif")
# 绘制飞机图片到屏幕,(200,500)水平和垂直方向的坐标
hero_x = 200
hero_y = 400
screen.blit(hero_image, (hero_x, hero_y))
# 可以在所有blit之后，统一更新屏幕,可以提高绘制效率
pygame.display.update()
#创建时钟对象
clock=pygame.time.Clock()
count=0
while True:
    clock.tick(60)#每秒内循环要运行的次数，所以这个循环应当每秒运行60次
    print(count)
    count+=1

# while True:
#     #循环事件
#     for event in pygame.event.get():
#         if event.type ==pygame.QUIT:#点击x关闭窗口
#             pygame.quit()
#             sys.exit(0)


