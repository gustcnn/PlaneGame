# --*--coding:utf-8
# Author:cnn
import pygame
import os


class GameWindow(object):
    def __init__(self, screen_x, screen_y, img_path):
        self.screen = pygame.display.set_mode((screen_x, screen_y))
        self.bg = pygame.image.load(img_path)

    #加载背景图片
    def upload_image(self):
        self.screen.blit(self.bg, (0, 0))


if __name__ == "__main__":
    object_path = os.path.dirname(os.path.dirname(__file__))
    window = GameWindow(480, 600, object_path + "/images/bg.jpg")
    # window.show_bg(object_path+"/images/bg.jpg")