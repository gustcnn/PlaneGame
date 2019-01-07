#--*--coding:utf-8
#Author:cnn
import pygame
pygame.init()
screen=pygame.display.set_mode((480,600))
text=pygame.font.SysFont("宋体",50)
text_format=text.render("game over",1,(255,255,255))
screen.blit(text_format,(0,0))
pygame.display.flip()
print(pygame.font.get_fonts())