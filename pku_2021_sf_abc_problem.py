from manim import *


class PKU2021StrongFoundationAbcProblem(Scene):
    def construct(self):
        # 标题
        title = Text("2021 北大强基：求 a + b + c", font_size=36, color=BLUE)
        subtitle_arr = [
            Text("题目来源： https://www.bilibili.com/video/BV1nh4y1M7h9", font_size=24, color=YELLOW),
            Text("作者：hans7", font_size=24, color=YELLOW),
            Text("文字稿传送门：见视频简介", font_size=24, color=YELLOW)
        ]
        subtitle_group = VGroup(*subtitle_arr).arrange(DOWN, buff=0.2)
        subtitle_group.next_to(title, DOWN, buff=0.5)
        self.play(Write(title), run_time=1)
        self.play(FadeIn(subtitle_group, shift=DOWN))
        self.play(Indicate(subtitle_arr[1], scale_factor=1.2, color=YELLOW))
        self.wait(2)
        self.play(FadeOut(title, subtitle_group))

        # 初始条件
        eq1 = MathTex(r"a = ab + c")
        eq2 = MathTex(r"b = bc + a")
        eq3 = MathTex(r"c = ca + b")
        eqs = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.4)
        note = Text("且 a, b, c 是不全相等的实数，求 a + b + c", font_size=28, color=RED)
        note.next_to(eqs, DOWN, buff=0.5)

        self.play(Write(eqs), run_time=1.5)
        self.play(FadeIn(note, shift=UP))
        self.wait(2)
        self.play(FadeOut(note))

        thought_arr = [
            Text("思想", font_size=60, color=YELLOW),
            Text("对于三元对称式的题，我们一般考虑用", font_size=28),
            MathTex(r"a + b + c,\ ab + bc + ca,\ abc", font_size=28, color=BLUE),
            Text("表示一切，所以我们要处理约束方程，弄出这3个式子", font_size=28),
        ]
        thought_group = VGroup(*thought_arr).arrange(DOWN, buff=0.3)
        self.play(ReplacementTransform(eqs, thought_group))
        self.play(Indicate(thought_arr[2], scale_factor=1.2, color=BLUE))
        self.wait(4)

        # Step 1: 三式相加
        step1_arr = [
            Text("三式相加："),
            MathTex(r"a + b + c = ab + bc + ca + (a + b + c)"),
            Text("移项得"),
            MathTex(r"ab + bc + ca = 0", color=GREEN)
        ]
        step1_group = VGroup(*step1_arr).arrange(DOWN, buff=0.3)
        self.play(ReplacementTransform(thought_group, step1_group))
        self.wait(2)

        # Step 2: 分别乘 c, a, b
        step2_arr = [
            Text("为了弄出 abc ，我们分别乘c、a、b："),
            MathTex(r"ac = abc + c^2"),
            MathTex(r"ab = abc + a^2"),
            MathTex(r"bc = abc + b^2")
        ]
        step2_group = VGroup(step2_arr).arrange(DOWN, buff=0.3)
        self.play(ReplacementTransform(step1_group, step2_group))
        self.wait(2)

        # 三式相加
        sum_mult_arr = [
            Text("三式相加："),
            MathTex(r"ab + bc + ca = 3abc + (a^2 + b^2 + c^2)"),
            Text("代入 ab+bc+ca = 0 得"),
            MathTex(r"0 = 3abc + (a^2 + b^2 + c^2)", color=GREEN)
        ]
        sum_mult_group = VGroup(*sum_mult_arr).arrange(DOWN, buff=0.3)
        self.play(ReplacementTransform(step2_group, sum_mult_group))
        self.play(Indicate(sum_mult_arr[-1], scale_factor=1.2, color=GREEN))
        self.wait(2)

        # Step 3: 展开 (a+b+c)^2 并代入 ab+bc+ca = 0
        square_arr = [
            Text("又因为"),
            MathTex(r"(a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca)"),
            Text("代入 ab+bc+ca = 0 得"),
            MathTex(r"(a + b + c)^2 = a^2 + b^2 + c^2", color=GREEN),
            Text("结合上式得"),
            MathTex(r"(a + b + c)^2 = -3abc", color=BLUE)
        ]
        square_group = VGroup(*square_arr).arrange(DOWN, buff=0.3)
        self.play(ReplacementTransform(sum_mult_group, square_group))
        self.play(Indicate(square_arr[-1], scale_factor=1.2, color=BLUE))
        self.wait(2)

        # Step 4: 移项并相乘
        shift_arr = [
            Text("为求出答案，我们还需要找1种方式构造出 abc"),
            Text("为此，对原方程移项："),
            MathTex(r"a(1 - b) = c"),
            MathTex(r"b(1 - c) = a"),
            MathTex(r"c(1 - a) = b"),
            Text("三式相乘得"),
            MathTex(r"abc(1 - a)(1 - b)(1 - c) = abc", color=BLUE),
        ]
        shift_group = VGroup(*shift_arr).arrange(DOWN, buff=0.3)
        self.play(ReplacementTransform(square_group, shift_group))
        self.play(Indicate(shift_arr[-1], scale_factor=1.2, color=BLUE))
        self.wait(2)

        # 讨论 abc 能否为 0
        abc_discuss_arr = [
            Text("若 abc = 0，不妨设 a = 0", font_size=28),
            Text("代入得 a = b = c = 0 ，与“不全相等”矛盾！故", font_size=28, color=RED),
            MathTex(r"abc \neq 0", color=GREEN)
        ]
        abc_discuss_group = VGroup(*abc_discuss_arr).arrange(DOWN, buff=0.3)
        self.play(ReplacementTransform(shift_group, abc_discuss_group))
        self.play(Indicate(abc_discuss_arr[-1], scale_factor=1.2, color=GREEN))
        self.wait(2)

        # 展开 (1-a)(1-b)(1-c) = 1
        expand_arr = [
            Text("因此："),
            MathTex(r"(1 - a)(1 - b)(1 - c) = 1"),
            Text("展开左边："),
            MathTex(r"1 - (a + b + c) + (ab + bc + ca) - abc = 1"),
            Text("代入 ab+bc+ca = 0 得"),
            MathTex(r"1 - (a + b + c) - abc = 1", color=GREEN),
            Text("化简得"),
            MathTex(r"a + b + c = -abc", color=BLUE)
        ]
        expand_group = VGroup(*expand_arr).arrange(DOWN, buff=0.3)
        self.play(ReplacementTransform(abc_discuss_group, expand_group))
        self.play(Indicate(expand_arr[-1], scale_factor=1.2, color=BLUE))
        self.wait(2)

        # 联立两式
        solve_arr = [
            Text("联立："),
            MathTex(r"\begin{cases} (a + b + c)^2 = -3abc \\ a + b + c = -abc \end{cases}"),
            Text("令 S = a + b + c ，则 S = -abc ，代入得"),
            MathTex(r"S^2 = -3abc = 3S \Rightarrow S^2 - 3S = 0"),
            MathTex(r"S(S - 3) = 0 \Rightarrow S = 0 \text{ or } S = 3")
        ]
        solve_group = VGroup(*solve_arr).arrange(DOWN, buff=0.4)
        self.play(ReplacementTransform(expand_group, solve_group))
        self.wait(2)

        # 排除 S=0
        exclude_s_eq_0_arr = [
            Text("若 S = 0，则 abc = 0，导致 a = b = c = 0，"),
            Text("与题设矛盾，舍去。故："),
            MathTex(r"a + b + c = 3", font_size=60, color=YELLOW)
        ]
        exclude_s_eq_0_group = VGroup(*exclude_s_eq_0_arr).arrange(DOWN, buff=0.4)
        self.play(ReplacementTransform(solve_group, exclude_s_eq_0_group))
        self.play(Indicate(exclude_s_eq_0_group[-1], scale_factor=1.2, color=YELLOW))
        self.wait(2)

        postscript_arr = [
            Text("后记", font_size=60, color=YELLOW),
            Text("这是我第一次用 manim 做数学题解的视频", font_size=28),
            Text("大佬们觉得这种展现形式与博客相比如何？", font_size=28),
            Text("欢迎在评论区留言，谢谢观看~", font_size=28),
        ]
        postscript_group = VGroup(*postscript_arr).arrange(DOWN, buff=0.4)
        self.play(ReplacementTransform(exclude_s_eq_0_group, postscript_group))
        self.wait(4)
