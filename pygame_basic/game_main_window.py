# --*--coding:utf-8
# Author:cnn
import pygame

pygame.init()
# 创建主窗口
screnn = pygame.display.set_mode((480, 853))
count = 0
while True:
    count += 1
    if count == 100:
        break
pygame.quit()
