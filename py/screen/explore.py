import cv2 as cv
import screen
import numpy as np
import random
import time


def click_random_point(lt, template_png):
    w, h = template_png.shape[::-1]
    dx = random.randint(lt[0], lt[0] + w)
    dy = random.randint(lt[1], lt[1] + h)
    screen.click_point(dx, dy)


class Explore:
    def __init__(self, scene=0):
        """
            scene 0 默认是未进入探索，1-是探索中
        """
        self.scene = scene
        self.explore_png = cv.imread('explore.png', 0)
        self.monster_png = cv.imread('monster.png', 0)
        self.reward_png = cv.imread('reward.png', 0)
        self.boss_png = cv.imread('boss.png', 0)
        self.sakura_mochi_png = cv.imread('SakuraMochi.png', 0)
        self.quit_png = cv.imread('quit.png', 0)
        self.ok_png = cv.imread('ok.png', 0)
        self.chapter_28_png = cv.imread('chapter28.png', 0)
        self.is_end_explore = True
        self.scene_switch_times = 0

    def fight_in_explore(self):
        while True:
            if self.is_end_explore is True:
                self.enter_explore()
                time.sleep(2)
            if self.is_end_explore is False:
                self.find_monster()
                time.sleep(2)
                self.quit_explore()
                time.sleep(2)

    def enter_explore(self):
        print('enter in explore ... ')
        img = screen.screencap()
        if img is not None:
            left_top = screen.match_template_return_lt(img, self.chapter_28_png)
            if left_top is not None:
                click_random_point(left_top, self.chapter_28_png)
            img = screen.screencap()
            lt = screen.match_template_return_lt(img, self.explore_png)
            if lt is not None:
                click_random_point(lt, self.explore_png)
                # 等待进入探索
                time.sleep(2)
                img = screen.screencap()
                sakura = screen.match_template_return_lt(img, self.sakura_mochi_png)
                if sakura is not None:
                    self.is_end_explore = False
                else:
                    self.enter_explore()

    def quit_explore(self):
        if self.is_end_explore is True:
            img = screen.screencap()
            lt = screen.match_template_return_lt(img, self.quit_png)
            if lt is not None:
                sakura_png = screen.match_template_return_lt(img, self.sakura_mochi_png)
                if sakura_png is not None:
                    click_random_point(lt, self.quit_png)
                    img = screen.screencap()
                    lt = screen.match_template_return_lt(img, self.ok_png)
                    if lt is not None:
                        click_random_point(lt, self.ok_png)

    def find_monster(self):
        screen_img = screen.screencap()
        if screen_img is not None:
            if self.is_end_explore is True:
                return
            self.find_boss(screen_img)
            lt = screen.match_template_return_lt(screen_img, self.monster_png)
            if lt is not None:
                w, h = self.monster_png.shape[::-1]
                self.battle(lt, w, h)
                self.find_monster()
            else:
                sakura = screen.match_template_return_lt(screen_img, self.sakura_mochi_png)
                if sakura is not None:
                    self.scene_switch_times = screen.next_scene(self.scene_switch_times)
                    self.find_monster()
                    if self.scene_switch_times == 4:
                        self.is_end_explore = True
                        return
                # self.find_monster()

    def battle(self, lt, w, h):
        dx = random.randint(lt[0], lt[0] + w)
        dy = random.randint(lt[1], lt[1] + h)
        screen.click_point(dx, dy)
        time.sleep(2)
        self.check_battle_end()

    # 还要根据是否在战斗中判断
    def check_battle_end(self):
        if self.is_end_explore is True:
            return
        screen_img = screen.screencap()
        res = screen.match_template(screen_img, self.reward_png)
        if res is None:
            sakura = screen.match_template_return_lt(screen_img, self.sakura_mochi_png)
            if sakura is not None:
                return
            else:
                self.check_battle_end()
        else:
            # 随机点击屏幕一下,不能随机点
            screen.click_point(res[0], res[1])
            time.sleep(1)

    def find_boss(self, screen_img):
        w, h = self.boss_png.shape[::-1]
        res = screen.match_template(screen_img, self.boss_png)
        if res is not None:
            screen.click_point(res[0], res[1])
            # cv.rectangle(screen_img, res, (res[0] + w, res[1] + h), (0, 0, 255), 2)
            self.check_battle_end()
            self.is_end_explore = True


if __name__ == '__main__':
    explore = Explore()
    explore.fight_in_explore()
    # explore.find_monster()
    # explore.is_end_explore = True
    # explore.quit_explore()

    # screen_png = screen.screencap()
    # explore.find_boss(screen_png)
    print(explore.is_end_explore)
