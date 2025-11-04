from manim import *


class AnimeCombineDemo(Scene):
    def construct(self):
        text1 = Text("死去元知万事空").shift(UP * 2)
        text2 = Text("但悲不见九州同").next_to(
            text1, DOWN, buff=0.5
        )
        text3 = Text("王师北定中原日").next_to(
            text2, DOWN, buff=0.5
        )
        text4 = Text("家祭无忘告乃翁").next_to(
            text3, DOWN, buff=0.5
        )

        anim_text1 = FadeIn(text1)
        anim_text2 = FadeIn(text2)
        anim_text3 = FadeIn(text3)
        anim_text4 = FadeIn(text4)

        # 按顺序逐个启动动画，每个动画之间的延迟由 lag_ratio 决定。但 lag_ratio 不影响 run_time
        self.play(
            LaggedStart(
                anim_text1,
                anim_text2,
                anim_text3,
                anim_text4,
                lag_ratio=0.15,
            ),
            run_time=6,
        )
