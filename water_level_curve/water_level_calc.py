from manim_slides.slide import Slide
from manim import *


class WaterLevelCalc(Slide):
    def construct(self):
        title1 = Text("旋转体体积公式", font_size=36).to_edge(UP)
        formula1 = MathTex(
            r"V = \int_{0}^{h} \pi f^2(x) \, dx",
            font_size=40
        )
        text1 = Text("设高度 $x$ 对应的截面与圆心的距离为 $f(x)$",
                     font_size=28, t2c={"$f(x)$": YELLOW}).next_to(formula1, DOWN, buff=0.6)

        self.play(Write(title1))
        self.play(Write(formula1))
        self.play(Write(text1))
        self.next_slide()

        title2 = Text("圆锥体积推导", font_size=36).to_edge(UP)
        derivation = MathTex(
            r"V &= \int_{0}^{h} \pi \left(r - \frac{r}{h}x\right)^2 dx \\",
            r"&= \pi r^2 \int_{0}^{h} \left(\frac{x^2}{h^2} - \frac{2x}{h} + 1\right) dx \\",
            r"&= \pi r^2 \left( \frac{x^3}{3h^2} - \frac{x^2}{h} + x \right) \bigg|_{0}^{h} \\",
            r"&= \frac{\pi r^2 h}{3}",
            font_size=36
        ).shift(DOWN * 0.5)

        self.play(
            FadeOut(title1, formula1, text1),
            Write(title2)
        )
        self.play(Write(derivation[0]))
        self.next_slide()
        self.play(Write(derivation[1]))
        self.next_slide()
        self.play(Write(derivation[2]))
        self.next_slide()
        self.play(Write(derivation[3]))
        self.next_slide()

        title3 = Text("完全浸没时的水位", font_size=36).to_edge(UP)
        eq1 = MathTex(
            r"SH = Sc + \frac{\pi r^2 h}{3}",
            font_size=40
        )
        eq2 = MathTex(
            r"\Rightarrow H = c + \frac{\pi r^2 h}{3S}",
            font_size=40
        ).next_to(eq1, DOWN, buff=0.6)

        self.play(
            FadeOut(title2, derivation),
            Write(title3)
        )
        self.play(Write(eq1))
        self.next_slide()
        self.play(Write(eq2))
        self.next_slide()

        title4 = Text("临界高度（H = h）", font_size=36).to_edge(UP)
        crit_eq = MathTex(
            r"H = \frac{Sc}{S - \frac{\pi r^2}{3}}",
            font_size=40
        )

        self.play(
            FadeOut(title3, eq1, eq2),
            Write(title4)
        )
        self.play(Write(crit_eq))
        self.next_slide()

        self.wait()
