#--*--coding:utf-8
#Author:cnn
import pygame
#矩形由坐标点、宽度、高度组成
hero_react=pygame.Rect(100,500,120,125)#pygame.Rect()描述矩形区域
print("原点%d %d"%(hero_react.x,hero_react.y))
print("尺寸%d %d"%(hero_react.width,hero_react.height))
print("%d %d"%hero_react.size)#返回宽度和高度元组
