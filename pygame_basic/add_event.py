# --*--coding:utf-8
# Author:cnn
"""
增加事件
"""
import pygame
import os
import sys

pygame.init()
window_x = 480
window_y = 600
plane_x = 200
plane_y = 400
plane_width = 100
plane_height = 124
screen = pygame.display.set_mode((window_x, window_y))
object_path = os.path.dirname(os.path.dirname(__file__))
bg = pygame.image.load(object_path + "/images/bg.jpg")
plane = pygame.image.load(object_path + "/images/hero.gif")
screen.blit(bg, (0, 0))
screen.blit(plane, (plane_x, plane_y))
pygame.display.update()
clock = pygame.time.Clock()
plane_rect = pygame.Rect(plane_x, plane_y, plane_width, plane_height)
while True:
    clock.tick(60)
    if plane_rect.y + plane_height <= 0:
        plane_rect.y = window_y - plane_height

    event_list = pygame.event.get()
    if len(event_list)>0:
        print(event_list)
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                plane_rect.y -= 5
                screen.blit(bg, (0, 0))
                screen.blit(plane, (plane_rect.x, plane_rect.y))
        pygame.display.update()