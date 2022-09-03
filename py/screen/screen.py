import os
import subprocess
import sys

import cv2 as cv
import random
import time
import numpy as np


# from matplotlib import pyplot as plt


def screencap():
    time.sleep(1)
    res = os.system("adb shell screencap -p /sdcard/tmp/test.png")
    if res == 0:
        res = os.system("adb pull /sdcard/tmp/test.png .")
        if res == 0:
            return cv.imread('screen.png', 0)
    return None


def click_point(dx, dy):
    print("click {} {} ".format(dx, dy))
    os.system("adb shell input tap {} {}".format(dx, dy))


def match_template(img, template):
    res = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    max_loc = res.max()
    if max_loc >= threshold:
        loc = np.where(res >= max_loc)
        for lt in zip(*loc[::-1]):
            w, h = template.shape[::-1]
            dx = random.randint(lt[0], lt[0] + w)
            dy = random.randint(lt[1], lt[1] + h)
            return dx, dy
    return None


def match_template_return_lt(img, template):
    res = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    max_loc = res.max()
    if max_loc >= threshold:
        loc = np.where(res >= max_loc)
        for lt in zip(*loc[::-1]):
            w, h = template.shape[::-1]
            cv.rectangle(img, lt, (lt[0] + w, lt[1] + h), (0, 0, 255), 2)
            print(lt)
            # cv.imwrite('res.png', img)
            return lt
    return None


def next_scene(times):
    """
    移动至下一个场景，每次移动400像素
    """
    x0 = random.randint(510, 1126)
    x1 = x0 - 500
    y0 = random.randint(110, 210)
    y1 = random.randint(110, 210)
    os.system('adb shell input swipe {} {} {} {}'.format(x0, y0, x1, y1))
    return times + 1


def is_explore(screen, template):
    res = match_template(screen, template)
    if res is None:
        return False
    else:
        return True


def main():
    screencap()
    screen = cv.imread('screen.png', 1)
    template = cv.imread('monster.png', 0)
    # match_template_return_lt(screen, template)
    cv.imshow('image', screen)
    cv.waitKey()


#


def main_test_no_file():
    res = subprocess.run(args=['adb', 'shell', 'screencap', ' -p'], capture_output=True)
    bng_bytes = res.stdout
    bng_bytes_array = bytearray(bng_bytes)
    bng_np_bytes_array = np.array(bng_bytes_array, dtype='uint8')
    img = cv.imdecode(bng_np_bytes_array, cv.IMREAD_UNCHANGED)
    cv.imshow('image', img)
    cv.waitKey()
    # f = open("test.png", "wb")
    # f.write(bng_bytes)
    # f.close()
    # img = cv.imread('test.png')
    # print(img)
    # print(cv)
    # cv.imwrite('test.png', img)


def screen_cap_from_phone():
    res = subprocess.run(args=['adb', 'shell', 'screencap', ' -p'], capture_output=True)
    bng_bytes = res.stdout
    print(bng_bytes)


if __name__ == '__main__':
    screen_cap_from_phone()
