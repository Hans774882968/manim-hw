from manim import *

BACKGROUND_IMAGE_PATH = "assets/南澳岛.jpg"
BACKGROUND_OPACITY = 0.4


class ImgMobjDemo(Scene):
    def construct(self):
        background = ImageMobject(BACKGROUND_IMAGE_PATH)
        background.set_opacity(BACKGROUND_OPACITY)
        background.stretch_to_fit_width(config.frame_width)
        background.stretch_to_fit_height(config.frame_height)
        # 和 VMobject 不同， Mobject 用的是 Group 和配套的 add
        gp = Group(background)
        self.add(gp)
        self.wait(2)
