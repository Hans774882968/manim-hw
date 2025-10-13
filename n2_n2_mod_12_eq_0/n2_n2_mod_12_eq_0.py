from manim import *


class N2N2Mod12Eq0(Scene):
    def show_title(self):
        title_group = VGroup(
            Text("证明 12 | n^2(n^2-1) 的", font_size=60, color=BLUE),
            Text("多种方法及其变形扩展", font_size=60, color=BLUE)
        ).arrange(DOWN, buff=0.2)
        subtitle_arr = [
            Text("题源： https://www.bilibili.com/video/BV1LabczHEvn", font_size=24, color=YELLOW),
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
        self.wait(16)
        self.play(FadeOut(title_group, subtitle_group))

    def show_method1(self):
        method1_title = Text("法1：数学归纳法", font_size=60, color=YELLOW)
        method1_title.to_edge(UP, buff=0.5)
        method1_thought = Text("关于自然数的命题 → 数学归纳法")
        method1_thought.next_to(method1_title, DOWN, buff=0.5)
        self.play(FadeIn(method1_title, shift=UP))
        self.play(Write(method1_thought))
        self.wait(8) # “n=1 显然成立”
        method1_expr_group = VGroup(
            MathTex(r"\frac{n^2(n^2-1)}{12}"),
            MathTex(r"= \frac{(k+1)^2k(k+2)}{12}"),
            MathTex(r"= \frac{k^4+4k^3+5k^2+2k}{12}"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        method1_expr_group.next_to(method1_thought, DOWN, buff=0.5)
        self.play(Write(method1_expr_group))
        self.wait(22) # “做差以后得到”

        method1_result_tex = MathTex(r"= \frac{4k^3+6k^2+2k}{12} = ", r"\frac{2k^3+3k^2+k}{6}", font_size=36)
        method1_res_expr = VGroup(
            Text("考虑与 n=k 时的差："),
            MathTex(r"\frac{k^4+4k^3+5k^2+2k-((k-1)^4+4(k-1)^3+5(k-1)^2+2(k-1))}{12}", font_size=36),
            method1_result_tex
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(ReplacementTransform(VGroup(method1_thought, method1_expr_group), method1_res_expr))
        res_frame_box = SurroundingRectangle(method1_result_tex[1], buff=.1, color=BLUE)
        self.play(
            Create(res_frame_box),
        )
        self.wait(27)
        self.remove(res_frame_box)
        method1_to_remove = VGroup(method1_title, method1_res_expr)
        return method1_to_remove

    def show_method2(self, method1_to_remove):
        method2_title = Text("法2：取模运算的性质", font_size=60, color=YELLOW)
        method2_title.to_edge(UP, buff=0.5)
        method2_character_group = VGroup(
            Text("a % m + b % m = (a + b) % m"),
            Text("a % m * b % m = (a * b) % m"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        method2_character_group.next_to(method2_title, DOWN, buff=0.5)
        method2_initial_view = VGroup(method2_title, method2_character_group)
        self.play(ReplacementTransform(method1_to_remove, method2_initial_view))
        self.wait(14)

        method2_thought_txt = MarkupText("根据<span foreground=\"#58C4DD\">唯一分解定理</span>，只需证它是3和4的倍数", font_size=36)
        method2_thought_txt.next_to(method2_title, DOWN, buff=0.5)
        self.play(ReplacementTransform(method2_character_group, method2_thought_txt))
        method2_example_3 = VGroup(
            Text("以3为例，把 n 换成 3k+v ，其中 v = 0, 1, 2", font_size=36),
            Text("一一验证即可", font_size=36, color=BLUE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        method2_example_3.next_to(method2_thought_txt, DOWN, buff=0.5)
        self.play(Write(method2_example_3))
        self.wait(19)
        method2_to_remove = VGroup(method2_title, method2_thought_txt, method2_example_3)
        return method2_to_remove

    def show_method3(self, method2_to_remove):
        method3_title = Text("法3：组合数", font_size=60, color=YELLOW)
        method3_title.to_edge(UP, buff=0.5)
        method3_thought_group = VGroup(
            MarkupText("题干的分子和分母都几乎是几个<span foreground=\"#58C4DD\">连续自然数</span>的乘积", font_size=36),
            Text("分子： (n-1)n(n+1) ，但多了一个n", font_size=36),
            Text("分母： 12 = 4! / 2", font_size=36)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        method3_thought_group.next_to(method3_title, DOWN, buff=0.5)
        self.play(FadeOut(method2_to_remove))
        self.play(FadeIn(method3_title, shift=UP))
        self.play(Write(method3_thought_group))
        self.wait(22)

        method3_thought2_group = VGroup(
            Text("拿出 (n-1)n(n+1) ，分子分母都乘2，让剩余部分为 2n", font_size=36),
            MathTex(r"\frac{n^2(n^2-1)}{12} = n(n-1)(n+1)\frac{2n}{24}"),
            MathTex(r"= n(n-1)(n+1)\frac{(n-2)+(n+2)}{24}")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        method3_res_expr = VGroup(
            MathTex(r"= \frac{(n-2)(n-1)n(n+1)}{24} + \frac{(n-1)n(n+1)(n+2)}{24}", color=BLUE),
            MathTex(r"= C_{n+1}^4 + C_{n+2}^4", color=BLUE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        method3_res_expr.next_to(method3_thought2_group, DOWN, buff=0.5)
        method3_last_view = VGroup(method3_thought2_group, method3_res_expr)
        method3_last_view.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        method3_last_view.next_to(method3_title, DOWN, buff=0.5)
        self.play(ReplacementTransform(method3_thought_group, method3_thought2_group))
        self.wait(12)
        self.play(Write(method3_res_expr))
        self.play(Indicate(method3_res_expr, scale_factor=1.2, color=BLUE))
        self.wait(8)
        method3_to_remove = VGroup(method3_title, method3_last_view)
        return method3_to_remove

    def show_method3_ext1(self, method3_to_remove):
        method3_ext1_title = Text("法3扩展：证个类似的式子", font_size=60, color=YELLOW)
        method3_ext1_title.to_edge(UP, buff=0.5)
        self.play(ReplacementTransform(method3_to_remove, method3_ext1_title))
        method3_ext1_stmt = VGroup(
            Text("证明"),
            MathTex(r"\frac{n^2(n^2-1)(n^2-4)}{360} \in Z", color=BLUE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        method3_ext1_stmt.next_to(method3_ext1_title, DOWN, buff=0.5)
        self.play(Write(method3_ext1_stmt))
        self.wait(8)

        method3_res_expr = VGroup(
            MathTex(r"= \frac{(n-3)(n-2)(n-1)n(n+1)(n+2)}{720} + \frac{(n-2)(n-1)n(n+1)(n+2)(n+3)}{720}", font_size=28, color=BLUE),
            MathTex(r"= C_{n+2}^6 + C_{n+3}^6", font_size=28, color=BLUE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        method3_ext1_res_group = VGroup(
            Text("同样的手法，拆出 n-3 和 n+3"),
            method3_res_expr
        )
        method3_ext1_res_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        method3_ext1_res_group.next_to(method3_ext1_stmt, DOWN, buff=0.5)
        self.play(Write(method3_ext1_res_group))
        self.play(Indicate(method3_res_expr, scale_factor=1.2, color=BLUE))
        self.wait(12)

        method3_ext1_to_remove = VGroup(method3_ext1_title, method3_ext1_stmt, method3_ext1_res_group)
        return method3_ext1_to_remove

    def show_method3_ext2(self, method3_ext1_to_remove):
        method3_ext2_title = Text("继续扩展：不那么优雅的式子", font_size=60, color=YELLOW)
        method3_ext2_title.to_edge(UP, buff=0.5)
        self.play(ReplacementTransform(method3_ext1_to_remove, method3_ext2_title))
        method3_ext2_stmt = VGroup(
            MathTex(r"n^2(n^2-1)(n+2)", color=BLUE),
            Text("何时整除120？")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        method3_ext2_stmt.next_to(method3_ext2_title, DOWN, buff=0.5)
        self.play(Write(method3_ext2_stmt))
        self.wait(14)

        js_code = Code(
            code_string='''for (let n = 1; n <= 60; n++) {
    console.log((n * n * (n + 1) * (n - 1) * (n + 2)) % 120);
}''',
            language="javascript"
        )
        method3_ext2_thought = VGroup(
            Text("我们不妨写点JS代码"),
            js_code
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        method3_ext2_thought.next_to(method3_ext2_stmt, DOWN, buff=0.5)
        self.play(Write(method3_ext2_thought))
        self.wait(8)

        method3_ext2_discovery = VGroup(
            Text("n = 5k+2 时余48，其余情况整除")
        )
        method3_ext2_discovery.next_to(method3_ext2_title, DOWN, buff=0.5)
        self.play(ReplacementTransform(
            VGroup(method3_ext2_stmt, method3_ext2_thought),
            method3_ext2_discovery
        ))
        self.wait(5)  # 等到“我们不难展开得到屏幕中的式子”开始

        method3_ext2_expand = VGroup(
            MathTex(r"\frac{n^2(n^2-1)(n+2)}{120}", font_size=36),
            MathTex(r"= (n-1)n(n+1)(n+2)\frac{(n-2)+2}{120}", font_size=36),
            MathTex(r"= C_{n+2}^5 + \frac{2}{5}\frac{(n-1)n(n+1)(n+2)}{24}", font_size=36),
            MathTex(r"= C_{n+2}^5 + \frac{2}{5}C_{n+2}^4", font_size=36)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        method3_ext2_expand.next_to(method3_ext2_discovery, DOWN, buff=0.5)
        self.play(Write(method3_ext2_expand))
        self.wait(3)

        method3_ext2_result_expr = MathTex(r"C_{n+2}^5 + \frac{2}{5}C_{n+2}^4", color=BLUE),
        method3_ext2_res = VGroup(
            method3_ext2_result_expr,
            Text("仅 n = 5k+2 时可以让这", font_size=36),
            Text("4个连续自然数刚好避开模5余0", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        method3_ext2_res.next_to(method3_ext2_discovery, DOWN, buff=0.5)
        self.play(ReplacementTransform(method3_ext2_expand, method3_ext2_res))
        res_frame_box = SurroundingRectangle(method3_ext2_result_expr[0], buff=.1, color=BLUE)
        self.play(
            Create(res_frame_box),
        )
        self.wait(10)
        self.remove(res_frame_box)

        method3_ext2_to_remove = VGroup(method3_ext2_title, method3_ext2_discovery, method3_ext2_res)
        return method3_ext2_to_remove

    def show_ending(self, method3_ext2_to_remove):
        postscript_arr = [
            Text("后记", font_size=60, color=YELLOW),
            Text("为做题人的精神自留地添砖加瓦", font_size=28, color=RED),
            Text("喜欢本期视频的话，别忘了一键三连哦", font_size=28, color=PINK),
            Text("谢谢观看~", font_size=28),
        ]
        postscript_group = VGroup(*postscript_arr).arrange(DOWN, buff=0.4)
        self.play(ReplacementTransform(method3_ext2_to_remove, postscript_group))
        self.play(
            Wiggle(postscript_group[-3]),
            Circumscribe(postscript_group[-2], run_time=4, color=PINK)
        )
        self.play(
            Wiggle(postscript_group[-3]),
            Wiggle(postscript_group[-2])
        )
        self.wait(22)

    def construct(self):
        self.show_title()
        method1_to_remove = self.show_method1()
        method2_to_remove = self.show_method2(method1_to_remove)
        method3_to_remove = self.show_method3(method2_to_remove)
        method3_ext1_to_remove = self.show_method3_ext1(method3_to_remove)
        method3_ext2_to_remove = self.show_method3_ext2(method3_ext1_to_remove)
        self.show_ending(method3_ext2_to_remove)
