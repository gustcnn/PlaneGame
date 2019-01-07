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
    hit_score = 0

    def __init__(self):
        print("游戏初始化...")
        pygame.init()
        # 创建主窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # self.show_text()
        # 创建时钟对象,控制刷新频率
        self.clock = pygame.time.Clock()
        # 调用私有方法,创建精灵和精灵组
        self.__create_sprite()
        # 设置定时器
        pygame.time.set_timer(ENEMY_TIMER_EVENT, 2000)
        # 设置发射子弹定时器,每隔0.5秒
        pygame.time.set_timer(HERO_FIRE_EVENT, 1000)

    def __create_sprite(self):
        bg1 = BackgroundSprite()
        bg2 = BackgroundSprite(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.hero = PlaneSprite()
        self.hero_group = pygame.sprite.Group(self.hero)
        # 创建敌机精灵组,因为敌人飞机是定时创建的
        self.enemy_group = pygame.sprite.Group()
        # self.bullet1=Bullet()
        # self.bullet_group=pygame.sprite.Group(self.bullet1)
        self.end_group = pygame.sprite.Group()

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
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
                # elif event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
                #     print("向右移动")
                #     self.hero.move("")
        key_pressed = pygame.key.get_pressed()  # 键盘事件
        if key_pressed[pygame.K_RIGHT]:
            self.hero.move(pygame.K_RIGHT)
        elif key_pressed[pygame.K_LEFT]:
            self.hero.move(pygame.K_LEFT)
        else:
            self.hero.move("")

    def __check_collision(self):
        collide_enemy_list = []
        # 子弹摧毁敌机
        hit_list = pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
        if len(hit_list) > 0:
            for hit in hit_list:
                PlaneGame.hit_score += 1
        # if PlaneGame.hit_score!=0:
        #     print(PlaneGame.hit_score)
        # 敌机销毁
        enemis = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 判断列表是否有内容,如果有内容,英雄牺牲
        if len(enemis) > 0:
            self.hero.kill()
            self.show_text()
            sleep(2)
            # self.show_text()
            PlaneGame.__game_over()

    def __update_sprites(self):
        """更新精灵"""
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)
        self.end_group.update()
        self.end_group.draw(self.screen)

    def show_text(self):
        text = pygame.font.SysFont("宋体",50)
        # text_format = text.render("game over", 1, (255, 0, 0))
        text_format = text.render("game over", 1, (255, 0, 0))
        self.screen.blit(text_format, (100,260))
        text_format = text.render("total score:%d"%PlaneGame.hit_score, 1, (255, 0, 0))
        self.screen.blit(text_format, (100, 300))
        pygame.display.flip()

    @staticmethod
    def __game_over():

        # pass
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    object_path = os.path.dirname(os.path.dirname(__file__))
    game = PlaneGame()
    game.start_game()
