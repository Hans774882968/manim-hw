from manim import *


# 为了方便使用，我们定义一些常用的颜色
class MyColors:
    BLUE = "#58C4DD"
    YELLOW = "#F0E442"
    GREEN = "#009E73"
    RED = "#CC79A7"
    ORANGE = "#D55E00"


class N2N2Mod12Eq0(Scene):
    def show_title(self):
        """展示标题页"""
        title_group = VGroup(
            Text("证明 12 | n^2(n^2-1) 的", font_size=60, color=BLUE),
            Text("多种方法及其变形扩展", font_size=60, color=BLUE)
        ).arrange(DOWN, buff=0.2)
        subtitle_arr = [
            Text("题源： https://www.bilibili.com/video/BV1LabczHEvn", font_size=24, color=YELLOW),
            MarkupText(f"作者：<span foreground=\"{MyColors.BLUE}\">hans7</span>", font_size=24),
            Text("我们必须想象，做题人是幸福的", font_size=24, color=MyColors.BLUE),
            Text("文字稿传送门：见视频简介", font_size=24, color=YELLOW),
        ]
        subtitle_group = VGroup(*subtitle_arr).arrange(DOWN, buff=0.2)
        subtitle_group.next_to(title_group, DOWN, buff=0.5)
        title_whole = VGroup(title_group, subtitle_group)
        title_whole.move_to(ORIGIN)
        self.play(Write(title_group), run_time=1)
        self.play(FadeIn(subtitle_group, shift=DOWN))
        self.play(Circumscribe(subtitle_arr[2], run_time=4, color=MyColors.BLUE))
        self.wait(8.1)
        self.play(FadeOut(title_whole))

    def construct_method1(self):
        """构建方法1：数学归纳法"""
        method1_title = Text("法1：数学归纳法（不推荐）", font_size=60, color=YELLOW)
        method1_thought = Text("关于自然数的命题 → 数学归纳法", font_size=36)
        method1_thought.next_to(method1_title, DOWN, buff=0.5)
        # 为了让表达式更清晰，我们分步写入
        step1 = MathTex(r"n=k+1", r": \frac{n^2(n^2-1)}{12}", r"= \frac{(k+1)^2k(k+2)}{12}")
        step2 = MathTex(r"= \frac{k^4+4k^3+5k^2+2k}{12}")
        method1_expr_group = VGroup(step1, step2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        method1_expr_group.next_to(method1_thought, DOWN, buff=0.5)
        method1_whole = VGroup(method1_title, method1_thought, method1_expr_group)
        method1_whole.move_to(ORIGIN)
        self.play(FadeIn(method1_title, shift=UP))
        self.play(Write(method1_thought))
        self.wait(5)
        self.play(Write(step1))
        self.wait(3)
        self.play(TransformMatchingTex(step1, step2, path_arc=90 * DEGREES))
        self.wait(4.263)
        # 解释思路：与n=k时的差是整数
        thought_text = Text("考虑与 n=k 时的差", font_size=36, color=MyColors.GREEN)
        thought_text.next_to(method1_expr_group, DOWN, buff=1)
        self.play(Write(thought_text))
        self.wait(4)
        method1_res_expr = MathTex(r"\frac{4k^3+6k^2+2k}{12}", r"= \frac{2k^3+3k^2+k}{6}")
        method1_res_expr.next_to(thought_text, DOWN, buff=0.5)
        self.play(
            FadeOut(thought_text),
            ReplacementTransform(method1_expr_group, method1_res_expr),
            FadeOut(method1_thought)
        )
        self.wait(4.5)
        conclusion_text = Text("这是平方的前缀和，必为整数", font_size=36, color=MyColors.GREEN)
        conclusion_text.next_to(method1_res_expr, DOWN, buff=0.5)
        self.play(Write(conclusion_text))
        self.wait(5)
        self.play(FadeOut(VGroup(method1_title, method1_res_expr, conclusion_text)))

    def construct_method2(self):
        """构建方法2：取模运算的性质"""
        method2_title = Text("法2：取模运算的性质（通解，推荐）", font_size=60, color=YELLOW)
        method2_properties = VGroup(
            Text("a % m + b % m = (a + b) % m", font_size=32),
            Text("a % m * b % m = (a * b) % m", font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        method2_thought = Text("根据唯一分解定理，分别证是4和3的倍数", font_size=36, color=MyColors.ORANGE)
        method2_thought.next_to(method2_properties, DOWN, buff=0.5)
        method2_whole = VGroup(method2_title, method2_properties, method2_thought).arrange(DOWN, buff=0.5)
        method2_whole.move_to(ORIGIN)
        self.play(FadeIn(method2_whole))
        self.wait(5)
        self.play(FadeOut(method2_properties))
        # 证明是3的倍数
        mod3_title = Text("1. 证明是3的倍数", font_size=48).next_to(method2_title, DOWN, buff=0.5)
        mod3_expr = MathTex(r"n^2(n^2-1) = n(n-1)n(n+1)").next_to(mod3_title, DOWN, buff=0.5)
        self.play(Write(mod3_title))
        self.play(Write(mod3_expr))
        self.wait(4)
        mod3_explain = Text("n, n-1, n+1 是三个连续整数，必有一个是3的倍数", font_size=32, color=MyColors.GREEN)
        mod3_explain.next_to(mod3_expr, DOWN, buff=0.5)
        self.play(Write(mod3_explain))
        # 高亮 n(n-1)(n+1)
        highlight_rect1 = SurroundingRectangle(mod3_expr[0][1:4], color=MyColors.GREEN, buff=0.1)
        self.play(Create(highlight_rect1))
        self.wait(5)
        self.play(FadeOut(VGroup(mod3_title, mod3_expr, mod3_explain, highlight_rect1)))
        # 证明是4的倍数
        mod4_title = Text("2. 证明是4的倍数", font_size=48).next_to(method2_title, DOWN, buff=0.5)
        mod4_expr1 = MathTex(r"n^2(n^2-1) = n^2 \cdot (n-1)(n+1)").next_to(mod4_title, DOWN, buff=0.5)
        self.play(Write(mod4_title))
        self.play(Write(mod4_expr1))
        self.wait(4)
        mod4_explain1 = Text("n-1, n, n+1 是两个连续整数，必有一个是2的倍数", font_size=32)
        mod4_explain2 = Text("n^2 提供了另一个因子2，合起来必有因子2*2=4", font_size=32)
        VGroup(mod4_explain1, mod4_explain2).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(mod4_expr1, DOWN, buff=0.5)
        self.play(Write(mod4_explain1))
        highlight_rect2 = SurroundingRectangle(mod4_expr1[0][3:6], color=MyColors.ORANGE, buff=0.1)
        self.play(Create(highlight_rect2))
        self.wait(3)
        self.play(Write(mod4_explain2))
        highlight_rect3 = SurroundingRectangle(mod4_expr1[0][0:2], color=MyColors.ORANGE, buff=0.1)
        self.play(Create(highlight_rect3))
        self.wait(5)
        self.play(FadeOut(VGroup(mod4_title, mod4_expr1, mod4_explain1, mod4_explain2, highlight_rect2, highlight_rect3)))
        # 结论
        conclusion_text = Text("因为 3 | n^2(n^2-1) 且 4 | n^2(n^2-1)", font_size=40)
        conclusion_text2 = Text("且 (3,4)=1，所以 12 | n^2(n^2-1)", font_size=40)
        VGroup(conclusion_text, conclusion_text2).arrange(DOWN, buff=0.2).next_to(method2_thought, DOWN, buff=0.5)
        self.play(Write(conclusion_text))
        self.wait(3)
        self.play(Write(conclusion_text2))
        self.wait(6)
        self.play(FadeOut(VGroup(method2_title, method2_thought, conclusion_text, conclusion_text2)))

    def construct_method3(self):
        """构建方法3：组合数"""
        method3_title = Text("法3：组合数", font_size=60, color=YELLOW)
        method3_thought = Text("构造连续自然数乘积的形式", font_size=36, color=MyColors.ORANGE)
        method3_thought.next_to(method3_title, DOWN, buff=0.5)
        self.play(FadeIn(method3_title, method3_thought))
        self.wait(4)
        # 公式推导
        step1 = MathTex(r"\frac{n^2(n^2-1)}{12} = n(n-1)(n+1)\frac{2n}{24}")
        step2 = MathTex(r"= n(n-1)(n+1)\frac{(n-2)+(n+2)}{24}")
        VGroup(step1, step2).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(method3_thought, DOWN, buff=0.5)
        self.play(Write(step1))
        self.wait(4)
        self.play(TransformMatchingTex(step1, step2))
        self.wait(4)
        # 标红 (n-2) 和 (n+2)
        step2[0][10:13].set_color(MyColors.RED)
        step2[0][14:17].set_color(MyColors.RED)
        self.wait(2)
        step3 = MathTex(r"= \frac{(n-2)(n-1)n(n+1)}{24} + \frac{(n-1)n(n+1)(n+2)}{24}")
        step3.next_to(step2, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(ReplacementTransform(step2, step3))
        self.wait(4)
        step4 = MathTex(r"= C_{n+1}^4 + C_{n+2}^4")
        step4.next_to(step3, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(TransformMatchingTex(step3, step4, key_map={r"24": r"4!"}))
        self.wait(3)
        circ1 = SurroundingRectangle(step4[0][0:6], color=MyColors.GREEN)
        circ2 = SurroundingRectangle(step4[0][7:13], color=MyColors.GREEN)
        self.play(Create(circ1), Create(circ2))
        self.wait(4)
        final_text = Text("组合数必为整数，证毕", font_size=40, color=MyColors.GREEN)
        final_text.next_to(step4, DOWN, buff=0.5)
        self.play(Write(final_text))
        self.wait(6)
        self.play(FadeOut(VGroup(method3_title, method3_thought, step4, circ1, circ2, final_text)))

    def construct_extension1(self):
        """构建扩展题1"""
        ext1_title = Text("扩展：证明 n^2(n^2-1)(n^2-4) / 360 是整数", font_size=50, color=YELLOW)
        self.play(FadeIn(ext1_title))
        self.wait(4)
        ext1_expr1 = MathTex(r"\frac{n^2(n^2-1)(n^2-4)}{360} = \frac{n^2(n-1)(n+1)(n-2)(n+2)}{360}")
        ext1_expr1.next_to(ext1_title, DOWN, buff=0.5)
        self.play(Write(ext1_expr1))
        self.wait(4)
        ext1_expr2 = MathTex(r"= \frac{(n-3)(n-2)(n-1)n(n+1)(n+2)}{720} + \frac{(n-2)(n-1)n(n+1)(n+2)(n+3)}{720}")
        ext1_expr2.next_to(ext1_expr1, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(ext1_expr2))
        self.wait(4)
        ext1_expr3 = MathTex(r"= C_{n+2}^6 + C_{n+3}^6")
        ext1_expr3.next_to(ext1_expr2, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(TransformMatchingTex(ext1_expr2, ext1_expr3, key_map={r"720": r"6!"}))
        self.wait(5)
        self.play(FadeOut(VGroup(ext1_title, ext1_expr1, ext1_expr2, ext1_expr3)))

    def construct_extension2(self):
        """构建扩展题2"""
        ext2_title = Text("扩展：讨论 n^2(n^2-1)(n+2) 何时整除 120", font_size=50, color=YELLOW)
        self.play(FadeIn(ext2_title))
        self.wait(4)
        # 展示JS代码
        js_code_text = Text("JS代码验证规律：", font_size=32)
        js_code = Code(
            code='''for (let n = 1; n <= 60; n++) {
    console.log((n * n * (n + 1) * (n - 1) * (n + 2)) % 120);
}''',
            language="javascript",
            font_size=24,
            line_spacing=0.5
        )
        VGroup(js_code_text, js_code).arrange(DOWN, buff=0.5).next_to(ext2_title, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(js_code_text), FadeIn(js_code, shift=LEFT))
        self.wait(6)
        # 发现规律
        finding_text = Text("发现 n = 5k+2 时余48，其余情况整除", font_size=36, color=MyColors.ORANGE)
        finding_text.next_to(js_code, DOWN, buff=0.5)
        self.play(Write(finding_text))
        self.wait(5)
        self.play(FadeOut(VGroup(js_code_text, js_code, finding_text)))
        # 代数推导
        ext2_expr1 = MathTex(r"\frac{n^2(n^2-1)(n+2)}{120} = (n-1)n(n+1)(n+2)\frac{(n-2)+2}{120}")
        ext2_expr1.next_to(ext2_title, DOWN, buff=0.5)
        self.play(Write(ext2_expr1))
        self.wait(4)
        ext2_expr2 = MathTex(r"= C_{n+2}^5 + \frac{2}{5}\frac{(n-1)n(n+1)(n+2)}{24}")
        ext2_expr2.next_to(ext2_expr1, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(TransformMatchingTex(ext2_expr1, ext2_expr2, key_map={r"120": r"5!", r"24": r"4!"}))
        self.wait(5)
        # 解释特例
        special_case_text = Text("关键在于分母的 5 能否被约掉", font_size=36, color=MyColors.GREEN)
        special_case_text.next_to(ext2_expr2, DOWN, buff=0.5)
        self.play(Write(special_case_text))
        self.wait(3)
        ext2_expr2[0][11:19].set_color(MyColors.BLUE)  # C_{n+2}^4
        highlight_rect = SurroundingRectangle(ext2_expr2[0][11:19], color=MyColors.BLUE, buff=0.1)
        self.play(Create(highlight_rect))
        self.wait(3)
        reason_text = Text("n = 5k+2 时, (n-1,n,n+1,n+2) 模5为 (1,2,3,4)", font_size=32)
        reason_text.next_to(special_case_text, DOWN, buff=0.5)
        self.play(Write(reason_text))
        self.wait(4)
        reason_text2 = Text("恰好避开了模5余0，无法约掉分母的5，所以不整除", font_size=32)
        reason_text2.next_to(reason_text, DOWN, buff=0.2)
        self.play(Write(reason_text2))
        self.wait(7)
        self.play(FadeOut(VGroup(ext2_title, ext2_expr2, special_case_text, highlight_rect, reason_text, reason_text2)))

    def construct_references(self):
        """构建参考资料页"""
        ref_title = Text("参考资料", font_size=60, color=YELLOW)
        self.play(FadeIn(ref_title))
        ref_arr = [
            Text("1. https://www.bilibili.com/video/BV1LabczHEvn", font_size=32, color=YELLOW),
            Text("2. 有时间研究一下里面的做法。", font_size=32),
            Text("   https://www.zhihu.com/question/552490365", font_size=32, color=YELLOW),
        ]
        ref_group = VGroup(*ref_arr).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        ref_group.next_to(ref_title, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(FadeIn(ref_group, shift=DOWN))
        self.wait(8)
        self.play(FadeOut(VGroup(ref_title, ref_group)))
        # 结束页
        end_text = Text("感谢观看", font_size=72, color=MyColors.BLUE)
        self.play(FadeIn(end_text, scale=1.5))
        self.wait(5)
        self.play(FadeOut(end_text))

    def construct(self):
        # 设置背景
        self.camera.background_color = "#1e1e1e"
        # 按顺序播放各个部分
        self.show_title()
        self.wait(1)
        self.construct_method1()
        self.wait(1)
        self.construct_method2()
        self.wait(1)
        self.construct_method3()
        self.wait(1)
        self.construct_extension1()
        self.wait(1)
        self.construct_extension2()
        self.wait(1)
        self.construct_references()
