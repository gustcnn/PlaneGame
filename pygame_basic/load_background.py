# --*--coding:utf-8
# Author:cnn
import pygame
import os
from time import sleep

# 加载背景图片
pygame.init()
# 创建主窗口
screen = pygame.display.set_mode((480, 852))
# 加载图片
# print(os.path.dirname(os.path.dirname(__file__)))
image_path = os.path.dirname(os.path.dirname(__file__))
# print(image_path+"/images/background.png")
#加载背景图像
bg = pygame.image.load(image_path + "/images/background.png")
# 绘制背景图像(0,0),绘制的位置
screen.blit(bg, (0, 0))
# 更新屏幕
pygame.display.update()
sleep(1)
pygame.quit()
