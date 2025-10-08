from manim import Text, Write, Scene


class HelloManim(Scene):
    def construct(self):
        text = Text("你好，Manim！", font="SimHei")
        self.play(Write(text))
        self.wait(2)
