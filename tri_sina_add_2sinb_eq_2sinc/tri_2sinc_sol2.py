from manim import *


class Tri2sinCSol2(Scene):
    def show_bg(self):
        background = ImageMobject("assets/南澳岛.jpg")
        background.set_opacity(0.4)
        background.stretch_to_fit_width(config.frame_width)
        background.stretch_to_fit_height(config.frame_height)
        self.add(background)

    def show_method2(self, last_section_to_remove=None):
        title = Text("法2：纯三角变换", font_size=60, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        if last_section_to_remove:
            self.play(ReplacementTransform(last_section_to_remove, title))
        else:
            self.play(Write(title))
        self.wait(8)  # “注意到约束方程里只有 sinA 系数是1”

        step1 = VGroup(
            Text("目标：将目标函数化为仅含 A 的表达式", font_size=36),
            MathTex(r"f = \frac{1}{\sin A} + \frac{1}{\sin B} - \frac{1}{\sin C}"),
            MathTex(r"= \frac{1}{\sin A} + \frac{\sin C - \sin B}{\sin B \sin C}"),
            MathTex(r"= \frac{1}{\sin A} + \frac{\sin A}{2 \sin B \sin C}")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step1.next_to(title, DOWN, buff=0.5)
        self.play(Write(step1))
        self.wait(10)  # “对分母用一次积化和差”

        step2 = VGroup(
            Text("对分母用一次积化和差：", font_size=36),
            MathTex(r"2\sin B \sin C = \cos(C - B) - \cos(C + B)"),
            MathTex(r"= \cos(C - B) + \cos A \quad (\because C + B = \pi - A)"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step2.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(step1, step2))
        self.wait(8)  # “为了干掉 C-B，回到约束方程”

        step3 = VGroup(
            Text("为了把 C-B 转化为 A ，对 ", font_size=36),
            MathTex(r"\sin C - \sin B"),
            Text(" 用和差化积：", font_size=36)
        ).arrange(RIGHT, buff=0.3)
        step3_eq1 = MathTex(r"\sin C - \sin B = 2\cos\frac{C+B}{2}\sin\frac{C-B}{2}")
        step3_eq2 = MathTex(r"= 2\cos\left(\frac{\pi}{2} - \frac{A}{2}\right)\sin\frac{C-B}{2} = 2\sin\frac{A}{2}\sin\frac{C-B}{2}")
        step3_group = VGroup(step3, step3_eq1, step3_eq2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        step3_group.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(step2, step3_group))
        self.wait(16)  # “我们回看约束方程，对左边的 sin A”

        step4_eq = MathTex(r"\Rightarrow ", r"\cos\frac{A}{2} = 2\sin\frac{C-B}{2}")
        step4 = VGroup(
            VGroup(
                Text("由题设 "),
                MathTex(r"\frac{\sin A}{2} = \sin C - \sin B = 2\sin\frac{A}{2}\sin\frac{C-B}{2}"),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("又由二倍角公式 "),
                MathTex(r"\sin A = 2\sin\frac{A}{2}\cos\frac{A}{2}"),
            ).arrange(RIGHT, buff=0.3),
            step4_eq
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step4.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(step3_group, step4))
        self.play(Indicate(step4_eq, scale_factor=1.2, color=BLUE))
        frame_box = SurroundingRectangle(step4_eq[-1], buff=0.1, color=BLUE)
        self.play(Create(frame_box))
        self.wait(13)  # “我们对 cos(C-B) 用一次二倍角公式”
        self.remove(frame_box)

        step5 = VGroup(
            VGroup(
                Text("对 cos(C-B) 用一次二倍角公式，就能弄出", font_size=36),
                MathTex(r"\sin\frac{C-B}{2}")
            ).arrange(RIGHT, buff=0.3),
            Text("进而全部转化为关于A的式子，完成消元", font_size=36),
            MathTex(r"\cos(C - B) = 1 - 2\sin^2\frac{C - B}{2}"),
            MathTex(r"= 1 - 2\left(\frac{1}{2}\cos\frac{A}{2}\right)^2 = 1 - \frac{1}{2}\cos^2\frac{A}{2}")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        step5.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(step4, step5))
        self.wait(14)  # “我们现在看到，屏幕上的式子”

        f_expr = VGroup(
            Text("所以"),
            MathTex(r"f = \frac{1}{\sin A} + \frac{\sin A}{\cos A + \cos(C - B)}"),
            MathTex(r"= \frac{1}{\sin A} + \frac{\sin A}{(\cos A + 1) - \frac{1}{2}\cos^2\frac{A}{2}}")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        f_expr.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(step5, f_expr))
        self.wait(8)  # “对它用一次二倍角公式”

        step6 = VGroup(
            VGroup(
                Text("用一次二倍角公式 ", font_size=36),
                MathTex(r"\cos A + 1 = 2\cos^2\frac{A}{2}"),
            ).arrange(RIGHT, buff=0.3),
            MathTex(r"\Rightarrow f = \frac{1}{\sin A} + \frac{\sin A}{2\cos^2\frac{A}{2} - \frac{1}{2}\cos^2\frac{A}{2}} = \frac{1}{\sin A} + \frac{\sin A}{\frac{3}{2}\cos^2\frac{A}{2}}"),
            MathTex(r"= \frac{1}{\sin A} + \frac{2\sin A}{3\cos^2\frac{A}{2}}")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step6.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(f_expr, step6))
        self.wait(9)  # “然后用二倍角公式把所有的 sin A 拆开”

        step7 = VGroup(
            VGroup(
                Text("拆开 sinA ，全部化为关于", font_size=36),
                MathTex(r"\tan\frac{A}{2}"),
                Text("的式子", font_size=36)
            ).arrange(RIGHT, buff=0.3),
            Text("注：也可以直接代入万能公式", font_size=36),
            MathTex(r"f = \frac{\sin^2 \frac{A}{2}+\cos^2 \frac{A}{2}}{2\sin \frac{A}{2}\cos \frac{A}{2}}+\frac{4}{3}\tan \frac{A}{2}"),
            MathTex(r"= \frac{1}{2}\tan \frac{A}{2}+\frac{1}{2\tan \frac{A}{2}}+\frac{4}{3}\tan \frac{A}{2}"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step7.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(step6, step7))
        self.wait(14)  # “最后用均值不等式就拿到答案啦”

        final_expr = MathTex(
            r"f = \frac{1}{2}\left( \frac{11}{3}t + \frac{1}{t} \right) \geq \frac{1}{2} \cdot 2 \sqrt{ \frac{11}{3}t \cdot \frac{1}{t} } = \sqrt{ \frac{11}{3} }",
            r"= \frac{\sqrt{33}}{3}")
        final_page_group = VGroup(
            VGroup(
                Text("令 ", font_size=36),
                MathTex(r"t = \tan \frac{A}{2} > 0"),
                Text(" ，则 ", font_size=36)
            ).arrange(RIGHT, buff=0.3),
            final_expr,
            VGroup(
                Text("当且仅当 ", font_size=36),
                MathTex(
                    r"\frac{11}{3}t = \frac{1}{t} \Rightarrow t = \sqrt{\frac{3}{11}}",
                    font_size=36)
            ).arrange(RIGHT, buff=0.3)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        final_page_group.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(step7, final_page_group))
        frame_box = SurroundingRectangle(final_expr[-1], buff=0.1, color=BLUE)
        self.play(Create(frame_box))
        self.wait(10)
        self.remove(frame_box)

        method2_to_remove = VGroup(title, final_page_group)
        return method2_to_remove

    def construct(self):
        self.show_bg()
        self.show_method2()
