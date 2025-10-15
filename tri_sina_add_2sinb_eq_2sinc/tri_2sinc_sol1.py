from manim import *


class Tri2sinCSol2(Scene):
    def show_bg(self):
        background = ImageMobject("assets/南澳岛.jpg")
        background.set_opacity(0.4)
        background.stretch_to_fit_width(config.frame_width)
        background.stretch_to_fit_height(config.frame_height)
        self.add(background)

    def show_method1(self):
        pass

    def construct(self):
        self.show_bg()
        self.show_method1()
