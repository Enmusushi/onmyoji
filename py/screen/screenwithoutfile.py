import os
import sys

origin = sys.stdout

f = open('test.png', 'wb')
sys.stdout = f

res = os.system("adb shell screencap -p ")

sys.stdout = origin
#os.dup2(sys.stdout.fileno(), f.fileno())
# out = sys.stdout
# print(out.fileno())
# print(sys.stdout)
#
# f.write(sys.stdout)
# f.close()
