# --*--coding:utf-8
# Author:cnn
import pygame
import os
import sys
from plane_game.plane_sprites import *


# 游戏主类,初始化(创建窗口,创建时钟对象,创建精灵和精灵组),开始游戏
class PlaneGame(object):
    """飞机大战主游戏"""

    # # 类的属性,窗口宽度常量
    # SCREEN_WIDTH = 480
    # # 类的属性,窗口高度常量
    # SCREEN_HEIGHT = 600

    def __init__(self):
        print("游戏初始化...")
        pygame.init()
        # 创建主窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建时钟对象,控制刷新频率
        self.clock = pygame.time.Clock()
        # 调用私有方法,创建精灵和精灵组
        self.__create_sprite()
        # 设置定时器
        pygame.time.set_timer(ENEMY_TIMER_EVENT, 2000)

    def __create_sprite(self):
        bg1 = BackgroundSprite()
        bg2 = BackgroundSprite(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        hero = PlaneSprite()
        self.hero_group = pygame.sprite.Group(hero)
        # 创建敌机精灵组,因为敌人飞机是定时创建的
        self.enemy_group = pygame.sprite.Group()
        # enemy0 = EnemySprite(0)
        # enemy1 = EnemySprite(1)
        # enemy2 = EnemySprite(2)
        # self.enemy_group = pygame.sprite.Group(enemy0, enemy1, enemy2)

    def start_game(self):
        print("游戏开始了...")
        while True:
            # 创建时钟对象
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collision()
            # 更新精灵
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    def __event_handler(self):
        """事件监听"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == ENEMY_TIMER_EVENT:

                enemy = EnemySprite()
                self.enemy_group.add(enemy)

    def __check_collision(self):
        pass

    def __update_sprites(self):
        """更新精灵"""
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

    @staticmethod
    def __game_over():
        # pass
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    object_path = os.path.dirname(os.path.dirname(__file__))
    game = PlaneGame()
    game.start_game()
