import random


class ExploreFight:

    def next_scene(self):
        """
        移动至下一个场景，每次移动400像素
        """
        x0 = random.randint(510, 1126)
        x1 = x0 - 500
        y0 = random.randint(110, 210)
        y1 = random.randint(110, 210)
        self.yys.mouse_drag_bg((x0, y0), (x1, y1))
