from manim import *


class TriSinAAdd2sinBEq2sinC(Scene):
    def show_bg(self):
        background = ImageMobject("assets/南澳岛.jpg")
        background.set_opacity(0.4)
        background.stretch_to_fit_width(config.frame_width)
        background.stretch_to_fit_height(config.frame_height)
        self.add(background)

    def show_title(self):
        title_group = VGroup(
            Text("颇有难度的解三角形题", font_size=60, color=BLUE),
            Text("sin A + 2sin B = 2sin C", font_size=60, color=BLUE)
        ).arrange(DOWN, buff=0.2)
        subtitle_arr = [
            Text("题源： https://www.bilibili.com/video/BV12DJXzoEgK", font_size=24, color=YELLOW),
            MarkupText("作者：<span foreground=\"#58C4DD\">hans7</span>", font_size=24),
            Text("我们必须想象，做题人是幸福的", font_size=24, color=BLUE),
            Text("文字稿传送门：见视频简介", font_size=24, color=YELLOW),
        ]
        subtitle_group = VGroup(*subtitle_arr).arrange(DOWN, buff=0.2)
        subtitle_group.next_to(title_group, DOWN, buff=0.5)

        title_whole = VGroup(title_group, subtitle_group)
        title_whole.move_to(ORIGIN)

        self.play(Write(title_group), run_time=1)
        self.play(FadeIn(subtitle_group, shift=DOWN))
        self.play(Circumscribe(subtitle_arr[2], run_time=4, color=BLUE))
        self.wait(17)
        self.play(FadeOut(title_group, subtitle_group))

    def show_problem_stmt(self):
        title = Text("题干", font_size=60, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=UP))

        stmt = VGroup(
            Text("三角形ABC中有"),
            MathTex(r"\sin A+2\sin B=2\sin C"),
            Text("求"),
            MathTex(r"\frac{1}{\sin A}+\frac{1}{\sin B}-\frac{1}{\sin C}"),
            Text("最小值"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        stmt.next_to(title, DOWN, buff=0.5)
        self.play(Write(stmt))
        self.wait(16)  # “我觉得题源视频”

        gossip = VGroup(
            Text("强注意力 → 打咩 ×", color=RED),
            Text("水到渠成 → 我要 √", color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        gossip.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(stmt, gossip))
        self.wait(20)  # “今天我带来了3种解法”

        problem_stmt_to_remove = VGroup(title, gossip)
        return problem_stmt_to_remove

    def show_thought(self, problem_stmt_to_remove):
        title = Text("思想", font_size=60, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(ReplacementTransform(problem_stmt_to_remove, title))

        thought = VGroup(
            Text("通过题设和数学对象自带的约束方程"),
            Text("把多元函数转化为一元函数求解")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        thought.next_to(title, DOWN, buff=0.5)
        self.play(Write(thought))
        self.wait(20)  # “这个视频讲难度最小的解法3”

        thought_to_remove = VGroup(title, thought)
        return thought_to_remove

    def show_method3(self, last_section_to_remove):
        title = Text("法3：双曲线", font_size=60, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(ReplacementTransform(last_section_to_remove, title))
        self.wait(16)  # “注意到 a/2 = c-b 满足”

        let_a_eq_2 = VGroup(
            MathTex(r"\frac{a}{2}=c-b"),
            Text("→ 不失一般性，令 ", font_size=36),
            MathTex(r"a=2"),
        ).arrange(RIGHT, buff=0.3)
        let_a_eq_2.next_to(title, DOWN, buff=0.5)
        self.play(Write(let_a_eq_2))
        self.wait(16)  # “不难写出焦点”

        hyperbola_tex = MathTex(r"\frac{x^2}{\frac{1}{4}}-\frac{y^2}{\frac{3}{4}}=1", color=BLUE)
        hyperbola_equation_group = VGroup(
            MathTex(r"C(1,0),\ B(-1,0),\ a_{0}=\frac{a}{4}=\frac{1}{2}"),
            hyperbola_tex
        ).arrange(DOWN, buff=0.5)
        hyperbola_equation_group.next_to(let_a_eq_2, DOWN, buff=0.5)
        self.play(Write(hyperbola_equation_group))
        frame_box = SurroundingRectangle(hyperbola_tex, buff=.1, color=BLUE)
        self.play(Create(frame_box))
        self.wait(13)  # “这里我们通过三角换元”
        self.remove(frame_box)

        trigo_substitution = VGroup(
            MathTex(r"x=\frac{1}{2}\sec u,y=\frac{\sqrt{ 3 }}{2}\tan u"),
            VGroup(
                Text("我们只取双曲线右支，故", font_size=36),
                MathTex(r"\sec u \geq 1")
            ).arrange(RIGHT, buff=0.3)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        trigo_substitution.next_to(title, DOWN, buff=0.5)
        hyperbola_page = VGroup(let_a_eq_2, hyperbola_equation_group)
        self.play(ReplacementTransform(hyperbola_page, trigo_substitution))
        self.wait(10)  # “由焦半径公式”

        focal_radius = VGroup(
            MarkupText("由<span foreground=\"#58C4DD\">焦半径公式</span>：", font_size=36),
            MathTex(r"\begin{cases} c=ex+a_{0}=\sec u+\frac{1}{2} \\ b=ex-a_{0}=\sec u-\frac{1}{2} \end{cases}")
        )
        focal_radius.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        focal_radius.next_to(trigo_substitution, DOWN, buff=0.5)
        self.play(Write(focal_radius))
        self.wait(12)  # “又因为我们有这些等式”

        b_c_expr_remove = VGroup(trigo_substitution, focal_radius)
        sin_exprs = VGroup(
            Text("又有", font_size=36),
            MathTex(r"\sin B=\frac{y}{c}"),
            MathTex(r"\sin C=\frac{y}{b}"),
            MathTex(r"\sin A=2(\sin C-\sin B)"),
            Text("于是目标函数可以化为只有u的形式", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        sin_exprs.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(b_c_expr_remove, sin_exprs))
        self.wait(10)  # “就像屏幕上展示的这样”

        res_exprs1 = VGroup(
            MathTex(r"f = \frac{1}{\sin A}+\frac{1}{\sin B}-\frac{1}{\sin C}", font_size=36),
            MathTex(r"= \frac{1}{2(\sin C-\sin B)}+\frac{c-b}{y}", font_size=36),
            MathTex(r"= \frac{bc}{2y(c-b)}+\frac{c-b}{y}", font_size=36),
            MathTex(r"= \frac{\frac{bc}{2}+1}{y}", font_size=36)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        res_exprs1.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(sin_exprs, res_exprs1))
        self.wait(6)  # “再用个均值不等式”

        res_val_tex = MathTex(r"\geq \frac{2}{\sqrt{ 3 }}\sqrt{ \frac{11}{4} }", r"=\frac{\sqrt{ 33 }}{3}")
        res_exprs2 = VGroup(
            MathTex(r"= \frac{\frac{\sec^2u}{2}+\frac{7}{8}}{\frac{\sqrt{ 3 }}{2}\tan u}"),
            MathTex(r"=\frac{\tan^2u+\frac{11}{4}}{\sqrt{ 3 }\tan u}"),
            res_val_tex
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        res_exprs2.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(res_exprs1, res_exprs2))
        frame_box = SurroundingRectangle(res_val_tex[1], buff=.1, color=BLUE)
        self.play(Create(frame_box))
        self.wait(10)  # “我之所以把”
        self.remove(frame_box)

        method3_to_remove = VGroup(title, res_exprs2)
        return method3_to_remove

    def show_ending(self, method3_to_remove):
        postscript_arr = [
            Text("后记", font_size=60, color=YELLOW),
            Text("分P是因为电脑性能差，见谅~", font_size=28),
            Text("为做题人的精神自留地添砖加瓦", font_size=28, color=RED),
            Text("喜欢本期视频的话，别忘了一键三连哦", font_size=28, color=PINK),
            Text("谢谢观看~", font_size=28),
        ]
        postscript_group = VGroup(*postscript_arr).arrange(DOWN, buff=0.4)
        self.play(ReplacementTransform(method3_to_remove, postscript_group))
        self.play(
            Wiggle(postscript_group[-3]),
            Circumscribe(postscript_group[-2], run_time=4, color=PINK)
        )
        self.play(
            Wiggle(postscript_group[-3]),
            Wiggle(postscript_group[-2])
        )
        self.wait(28)

    def construct(self):
        self.show_bg()
        self.show_title()
        problem_stmt_to_remove = self.show_problem_stmt()
        thought_to_remove = self.show_thought(problem_stmt_to_remove)
        method3_to_remove = self.show_method3(thought_to_remove)
        self.show_ending(method3_to_remove)
