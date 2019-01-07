#--*--coding:utf-8
#Author:cnn
import pygame
import os
from time import sleep

class GameWindow(object):
    pygame.init()
    def __init__(self,screen_x,screen_y):
        self.screen=pygame.display.set_mode((screen_x,screen_y))
    def show_bg(self,img_path):
        bg=pygame.image.load(img_path)
        self.screen.blit(bg,(0,0))
        pygame.display.update()

    def show_text(self, surface_handle, pos, text, color, font_bold=False, font_size=13, font_italic=False):
        '''
        Function:文字处理函数
        Input：surface_handle：surface句柄
               pos：文字显示位置
               color:文字颜色
               font_bold:是否加粗
               font_size:字体大小
               font_italic:是否斜体
        Output: NONE
        author: socrates
        blog:http://blog.csdn.net/dyx1024
        date:2012-04-15
        '''
        # 获取系统字体，并设置文字大小
        cur_font = pygame.font.SysFont("宋体", font_size)
        # 设置是否加粗属性
        cur_font.set_bold(font_bold)
        # 设置是否斜体属性
        cur_font.set_italic(font_italic)
        # 设置文字内容
        text_fmt = cur_font.render(text, 1, color)
        # 绘制文字
        surface_handle.blit(text_fmt, pos)

if __name__=="__main__":
    object_path=os.path.dirname(os.path.dirname(__file__))
    window=GameWindow(480,600)
    text=pygame.font.SysFont("宋体",50)
    text_format=text.render("游戏结束",1,(255,255,255))
    window.screen.blit(text_format,(0,0))
    #window.show_bg(object_path+"/images/background.png")
    # window.show_text(window.screen,(200, 300),"游戏结束",(0,0,255),True,13,True)
    # sleep(5)