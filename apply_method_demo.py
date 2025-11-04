from manim import *


class ApplyMethodDemo(Scene):
    def construct(self):
        s1 = Square(color=BLUE, fill_color=BLUE, fill_opacity=0.5)
        s2 = Circle(color=RED, fill_color=RED, fill_opacity=0.5)
        self.add(s1, s2)
        # self.play(ApplyMethod(s1.shift, RIGHT))
        self.play(s1.animate.shift(RIGHT))
        # 都是 [1. 0. 0.]
        print("s1 中心", s1.get_center())
        self.wait()
        # self.play(s2.animate.shift(RIGHT))
        self.play(ApplyMethod(s2.shift, RIGHT))
        print("s2 中心", s2.get_center())
        self.wait()
