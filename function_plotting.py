from manim import Scene, Axes, GREEN, BLUE, Create, Write, MathTex, UR, DR, Dot, ValueTracker, always_redraw, Rotate, ORIGIN, FadeIn, PI, RED


class FunctionPlotting(Scene):
    def construct(self):
        # 把 x 坐标轴范围设得比曲线宽点，才能看到函数标签
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-4, 4],
            axis_config={"include_numbers": True}
        )

        labels = axes.get_axis_labels(
            x_label="x", y_label="f(x)"
        )

        self.play(Create(axes), Write(labels))
        self.wait(0.5)

        parabola = axes.plot(
            lambda x: x**2,
            color=BLUE,
            x_range=[-2, 2]
        )

        func_label = MathTex("f(x)=x^2").next_to(parabola, UR)

        self.play(Create(parabola), Write(func_label))
        self.wait(0.5)

        parabola_rotated = parabola.copy()

        self.play(
            Rotate(parabola_rotated, angle=PI, about_point=ORIGIN),
            run_time=2
        )

        new_func_label = MathTex("g(x) = -x^2").next_to(parabola_rotated, DR)
        self.play(Write(new_func_label))
        self.wait(0.5)

        # 创建一个值追踪器，控制 x 从 -2 到 2
        x_tracker = ValueTracker(-2)

        moving_dot_P = always_redraw(
            lambda: Dot(
                point=axes.c2p(x_tracker.get_value(), x_tracker.get_value()**2),
                color=RED
            )
        )

        moving_dot_P_prime = always_redraw(
            lambda: Dot(
                point=axes.c2p(-x_tracker.get_value(), -(x_tracker.get_value()**2)),
                color=GREEN
            )
        )

        # 同时显示两个点
        self.play(
            FadeIn(moving_dot_P),
            FadeIn(moving_dot_P_prime)
        )

        # 同步运动：x从-2到2
        self.play(
            x_tracker.animate.set_value(2),
            run_time=4,
            rate_func=lambda t: t  # 线性运动
        )
        self.wait(0.5)
