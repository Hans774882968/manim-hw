from manim import MathTex, Scene, SurroundingRectangle, BLUE, Create, Write, ReplacementTransform


class TexDemo(Scene):
    def construct(self):
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=", "f(x)\\frac{d}{dx}g(x)", "+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=.1, color=BLUE)
        framebox2 = SurroundingRectangle(text[3], buff=.1, color=BLUE)
        self.play(
            Create(framebox1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1, framebox2),
        )
        self.wait()
