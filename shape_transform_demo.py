from manim import Create, BLUE, RED, Square, Circle, RIGHT, Scene, Transform, Text, Write, ReplacementTransform, FadeTransform, FadeOut


class BasicShapesAndTransform(Scene):
    def construct(self):
        circle = Circle(
            radius=1.0,
            color=BLUE,
            stroke_width=2.0,
            fill_opacity=0.4
        )

        self.play(Create(circle))
        self.wait(1)

        square = Square(
            side_length=2.0,
            color=RED,
            fill_opacity=0.5
        )

        square.next_to(circle, RIGHT)

        self.play(Create(square))
        self.wait(1)

        self.play(Transform(square, circle))
        self.wait(1)

        # 如果不把 square 干掉，就无法实现从圆到文字的过渡动画
        self.remove(square)

        text1 = Text("你好", font="SimHei")
        text2 = Text("世界", font="SimHei")

        self.play(FadeTransform(circle, text1))
        # 两种都 OK ，但个人认为用 FadeTransform 的观感比用 FadeOut + Write 的好
        # self.play(FadeOut(circle))
        # self.play(Write(text1))

        self.wait(1)
        self.play(ReplacementTransform(text1, text2))
        self.wait(1)
