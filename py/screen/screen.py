import os
import subprocess
import cv2 as cv
from PIL import Image

print(cv.__version__)


def main():
    screen_img = os.popen('adb shell screencap -p')
    print(screen_img.encoding)
    res = subprocess.run('adb shell screencap -p', capture_output=True)
    bng_bytes = res.stdout
    f = open("test.png", "wb")
    f.write(bng_bytes)
    f.close()
    cv.bootstrap()
    img = cv.imread('test.png')
    print(img)
    print(cv)


if __name__ == '__main__':
    main()
