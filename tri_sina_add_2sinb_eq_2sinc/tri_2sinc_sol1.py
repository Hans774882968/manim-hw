from manim import *


class Tri2sinCSol1(Scene):
    def show_bg(self):
        background = ImageMobject("assets/南澳岛.jpg")
        background.set_opacity(0.4)
        background.stretch_to_fit_width(config.frame_width)
        background.stretch_to_fit_height(config.frame_height)
        self.add(background)

    def show_method1(self):
        title = Text("法1：正弦定理 + 余弦定理", font_size=60, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(10)  # “我搜到另一道相似但更简单的题”

        # Step 0: 讲解相似但更简单的题
        step0 = VGroup(
            Text("先看个更简单的题（链接见视频简介）", font_size=36),
            VGroup(
                Text("已知", font_size=36),
                MathTex(r"\sin A + \sqrt{2}\sin B = 2\sin C"),
                Text("，求", font_size=36),
                MathTex(r"\cos C"),
                Text("的最小值", font_size=36)
            ).arrange(RIGHT, buff=0.3),
            MarkupText("我们只需要用<span foreground=\"#58C4DD\">余弦定理</span>并代入约束方程，消去c：", font_size=36),
            MathTex(r"\cos C = \frac{a^2 + b^2 - c^2}{2ab} = \frac{a^2 + b^2 - (\frac{a + \sqrt{2}b}{2})^2}{2ab} = \frac{3a^2+2b^2}{8ab} - \frac{\sqrt{2}}{4}", font_size=36),
            VGroup(
                Text("最后一个均值不等式就做完~答案 ", font_size=36),
                MathTex(r"\frac{\sqrt{6}-\sqrt{2}}{4}")
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step0.next_to(title, DOWN, buff=0.5)
        self.play(Write(step0))
        self.wait(25)  # “我们先让目标函数出现三角形的边长”

        # Step 1: 定义目标函数 f，用正弦定理搞出边长
        step1 = VGroup(
            Text("由正弦定理，让f出现三角形的边长：", font_size=36),
            MathTex(r"f = \frac{1}{\sin A} + \frac{1}{\sin B} - \frac{1}{\sin C}"),
            MathTex(r"= \frac{1}{\sin A} \left( 1 + \frac{\sin A}{\sin B} - \frac{\sin A}{\sin C} \right)"),
            MathTex(r"= \frac{1}{\sin A} \left( 1 + \frac{a}{b} - \frac{a}{c} \right)")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step1.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(step0, step1))
        self.wait(7)  # “由正弦定理，约束方程相当于”

        # Step 2: 利用约束 a + 2b = 2c 消元
        step2_final_expr = MathTex(r"= \frac{1}{\sin A} \left( 2 \cdot", r"\frac{b^2 + c^2}{bc}", r"- 3 \right)", font_size=36, color=BLUE)
        step2 = VGroup(
            VGroup(
                Text("由正弦定理，题设约束相当于：", font_size=36),
                MathTex(r"a + 2b = 2c \Rightarrow a = 2(c - b)"),
            ).arrange(RIGHT, buff=0.3),
            Text("代入目标函数，消去a：", font_size=36),
            MathTex(r"f = \frac{1}{\sin A} \left( 1 + \frac{2(c - b)}{b} - \frac{2(c - b)}{c} \right)", font_size=36),
            MathTex(r"= \frac{1}{\sin A} \left( 1 + 2\left( \frac{c}{b} - 1 - 1 + \frac{b}{c} \right) \right)", font_size=36),
            step2_final_expr
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step2.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(step1, step2))
        self.play(Indicate(step2_final_expr[1], scale_factor=1.2, color=BLUE))
        frame_box = SurroundingRectangle(step2_final_expr[1], buff=0.1, color=BLUE)
        self.play(Create(frame_box))
        self.wait(12)  # “我们发现，f里出现了”
        self.remove(frame_box)

        # Step 3: 联想余弦定理，构造 cos A
        step3 = VGroup(
            VGroup(
                Text("在哪会出现", font_size=36),
                MathTex(r"\frac{b^2 + c^2}{bc}"),
                Text("这样的结构呢？", font_size=36),
            ).arrange(RIGHT, buff=0.3),
            Text("余弦定理", font_size=80, color=BLUE),
        ).arrange(DOWN, buff=0.4)
        step3.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(step2, step3))
        self.play(Indicate(step3[-1], scale_factor=1.2, color=BLUE))
        self.wait(14)  # “于是我们把”

        step3_2_final_expr = MathTex(r"= \frac{-3(b^2 + c^2) + 8bc}{2bc} = 4 - \frac{3}{2} \cdot", r"\frac{b^2 + c^2}{bc}", font_size=36, color=BLUE)
        step3_2 = VGroup(
            MathTex(r"\cos A = \frac{b^2 + c^2 - a^2}{2bc}", font_size=36),
            MathTex(r"= \frac{b^2 + c^2 - [2(c - b)]^2}{2bc}", font_size=36),
            MathTex(r"= \frac{b^2 + c^2 - 4(c^2 - 2bc + b^2)}{2bc}", font_size=36),
            step3_2_final_expr
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step3_2.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(step3, step3_2))
        frame_box = SurroundingRectangle(step3_2_final_expr[-1], buff=0.1, color=BLUE)
        self.play(Create(frame_box))
        self.wait(6)  # “代回f，”
        self.remove(frame_box)

        # Step 4: 代回 f 表达式，化简为仅含 A 的函数
        step4_eq1 = MathTex(r"\Rightarrow \frac{b^2 + c^2}{bc} = \frac{2}{3}(4 - \cos A)", font_size=36)
        step4_eq2 = MathTex(r"f = \frac{1}{\sin A} \left( \frac{2}{3}(4 - \cos A) \cdot 2 - 3 \right)", font_size=36),
        step4_eq3 = MathTex(r"= \frac{1}{\sin A} \left( \frac{16 - 4\cos A}{3} - 3 \right)", font_size=36)
        step4_eq4 = MathTex(r"= \frac{7 - 4\cos A}{3\sin A}", font_size=36, color=BLUE)
        step4 = VGroup(
            step4_eq1,
            step4_eq2,
            step4_eq3,
            step4_eq4
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step4.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(step3_2, step4))
        self.play(Indicate(step4_eq4, scale_factor=1.2, color=BLUE))
        frame_box = SurroundingRectangle(step4_eq4, buff=0.1, color=BLUE)
        self.play(Create(frame_box))
        self.wait(7)  # “这就是一道高中数学的基本题了”
        self.remove(frame_box)

        # Step 5: 几何意义解释 —— 单位圆上斜率
        step5 = VGroup(
            Text("", font_size=36),
            MathTex(r"f = \frac{7 - 4\cos A}{3\sin A} = -\frac{4}{3} \cdot \frac{ \frac{7}{4} - \cos A }{ 0 - \sin A }"),
            VGroup(
                Text("几何意义法：考虑单位圆上点 ", font_size=36),
                MathTex(r"P = (\cos A, \sin A), \quad A \in (0, \pi)"),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("则上式为 ", font_size=36),
                MathTex(r"-\frac{4}{3} \times"),
                MathTex(r"PQ"),
                Text("斜率的倒数"),
                MathTex(r", Q = \left( \frac{7}{4}, 0 \right)")
            ).arrange(RIGHT, buff=0.3)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step5.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(step4, step5))
        self.wait(26)  # “我们不妨在这里画张图”
        self.play(FadeOut(step5))

        plane = NumberPlane(x_range=[-2.5, 2.5, 0.5], y_range=[-2.5, 2.5, 0.5], axis_config={"stroke_opacity": 0.5})
        unit_circle = Circle(radius=1, color=BLUE)
        # 点Q
        point_q_coords = np.array([7 / 4, 0, 0])
        point_q_label = MathTex(r"Q(\frac{7}{4}, 0)").next_to(point_q_coords, RIGHT, buff=0.2).scale(0.8)
        dot_q = Dot(point=point_q_coords, color=RED)
        # 随便取一个起始角度 A ，让它运动到相切位置
        angle_A_whatever_val = 30 * DEGREES
        point_p_coords = np.array([np.cos(angle_A_whatever_val), np.sin(angle_A_whatever_val), 0])
        dot_p = Dot(point=point_p_coords, color=BLUE)
        point_p_label = MathTex(r"P(\cos A, \sin A)").next_to(point_p_coords, UP + LEFT, buff=0.2).scale(0.8)
        # 半径OP
        line_op = Line(ORIGIN, point_p_coords, color=WHITE)
        # 连线PQ
        line_pq = Line(point_p_coords, point_q_coords, color=GREEN)
        self.play(Create(plane), Create(unit_circle))
        self.play(Create(dot_q), Write(point_q_label))
        self.play(Create(dot_p), Write(point_p_label))
        self.play(Create(line_op))
        self.play(Create(line_pq))
        cos_tan, sin_tan = 4 / 7, np.sqrt(33) / 7
        point_tan_coords = np.array([cos_tan, sin_tan, 0])
        self.play(
            dot_p.animate.move_to(point_tan_coords),
            point_p_label.animate.next_to(point_tan_coords, UP + LEFT, buff=0.2),
            line_op.animate.put_start_and_end_on(ORIGIN, point_tan_coords),
            line_pq.animate.put_start_and_end_on(point_tan_coords, point_q_coords),
            run_time=3
        )
        # 标记直角。两条射线起点相同才能标在正确位置
        line_po_tmp = Line(point_tan_coords, ORIGIN, color=WHITE)
        right_angle = RightAngle(line_po_tmp, line_pq, length=0.2, color=BLUE)
        self.play(Create(right_angle))
        self.wait(4)  # “根据勾股定理，最小斜率就是这个数”
        plane_drawing_to_remove = VGroup(plane, unit_circle, dot_q, point_q_label, dot_p, point_p_label, line_op, line_pq, right_angle)

        # Step 6: 最小值计算（勾股定理）
        step6 = VGroup(
            Text(
                "当 PQ 与单位圆相切时，斜率的绝对值最大",
                font_size=36),
            MathTex(
                r"|PQ|_{\min} = \sqrt{ \left( \frac{7}{4} \right)^2 - 1^2 } = \sqrt{ \frac{49}{16} - 1 } = \sqrt{ \frac{33}{16} } = \frac{\sqrt{33}}{4}",
                font_size=36),
            VGroup(
                MathTex(
                    r"\Rightarrow",
                    font_size=36),
                Text(
                    "最小斜率",
                    font_size=36),
                MathTex(
                    r" = -\frac{1}{|PQ|_{\min}} = -\frac{4}{\sqrt{33}}",
                    font_size=36),
            ).arrange(
                RIGHT,
                buff=0.3),
            MathTex(
                r"\Rightarrow f_{\min} = -\frac{4}{3} \cdot \left( -\frac{\sqrt{33}}{4} \right) = \frac{\sqrt{33}}{3}",
                font_size=36)).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.5)
        step6.next_to(title, DOWN, buff=0.5)
        self.play(ReplacementTransform(plane_drawing_to_remove, step6))
        frame_box = SurroundingRectangle(step6[-1], buff=0.1, color=BLUE)
        self.play(Create(frame_box))
        self.wait(10)
        self.remove(frame_box)

    def construct(self):
        self.show_bg()
        self.show_method1()
