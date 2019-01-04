#--*--coding:utf-8
#Author:cnn
import pygame
import os

class GameWindow(object):
    def __init__(self,screen_x,screen_y):
        self.screen=pygame.display.set_mode((screen_x,screen_y))
    def show_bg(self,img_path):
        bg=pygame.image.load(img_path)
        self.screen.blit(bg,(0,0))
        pygame.display.update()
if __name__=="__main__":
    object_path=os.path.dirname(os.path.dirname(__file__))
    window=GameWindow(480,600)
    window.show_bg(object_path+"/images/bg.jpg")
