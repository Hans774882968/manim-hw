from manim import *
import numpy as np
import sympy as sp

S_val = 120   # 水箱底面积
c_val = 3     # 初始水位
r_val = 8     # 圆锥、抛物线旋转体底面半径

# 圆锥、抛物线旋转体临界高度
cone_h_crit = S_val * c_val / (S_val - (1 / 3) * np.pi * r_val**2)  # 6.795099492796862
parabola_h_crit = S_val * c_val / (S_val - (8 / 15) * np.pi * r_val**2)  # 28.197761774413703

H_sym = sp.Symbol('H')


def solve_H_for_h_sympy(h):
    """用 sympy 求解三次方程，返回满足 c < H < h 的实根"""
    a = float(np.pi * r_val**2 / (3 * h**2))
    b = float(-np.pi * r_val**2 / h)
    c = float(np.pi * r_val**2 - S_val)
    d = float(S_val * c_val)

    poly = sp.Poly(a * H_sym**3 + b * H_sym**2 + c * H_sym + d, H_sym)

    # 求所有数值根（包括复数）
    roots = poly.nroots()

    for root in roots:
        if abs(sp.im(root)) < 1e-8:
            H_real = float(sp.re(root))
            if c_val < H_real < h:
                return H_real

    # 如果没找到有效根（理论上不应发生），直接给 0 ，让开发者感知到异常
    return 0


def H_of_h_cone(h):
    """完整的圆锥 H(h) 分段函数"""
    if h <= 0:
        return c_val
    if h <= cone_h_crit:
        return c_val + (np.pi * r_val**2 / (3 * S_val)) * h
    return solve_H_for_h_sympy(h)


def linear_model_H_cone(h):
    """圆锥完全浸没线性模型（用于计算误差）"""
    return c_val + (np.pi * r_val**2 / (3 * S_val)) * h


def solve_H_for_h_parabola_sympy(h):
    """用 sympy 求解五次方程，返回满足 c < H < h 的实根"""
    a5 = np.pi * r_val**2 / (5 * h**4)
    a3 = -2 * np.pi * r_val**2 / (3 * h**2)
    a1 = np.pi * r_val**2 - S_val
    a0 = S_val * c_val

    H = H_sym
    poly_expr = a5 * H**5 + a3 * H**3 + a1 * H + a0
    poly = sp.Poly(poly_expr, H)

    roots = poly.nroots()
    for root in roots:
        if abs(sp.im(root)) < 1e-8:
            H_real = float(sp.re(root))
            if c_val < H_real < h:
                return H_real
    return 0


def H_of_h_parabola(h):
    """抛物线旋转体的完整 H(h) 分段函数"""
    if h <= 0:
        return c_val
    if h <= parabola_h_crit:
        return c_val + (8 * np.pi * r_val**2 / (15 * S_val)) * h
    return solve_H_for_h_parabola_sympy(h)


def linear_model_H_parabola(h):
    """抛物线旋转体完全浸没线性模型（用于误差计算）"""
    return c_val + (8 * np.pi * r_val**2 / (15 * S_val)) * h


class WaterLevelCurve(Scene):
    def show_cone_h_H_curve(self, cone_h_min, cone_h_max, cone_H_min, cone_H_max):
        axes1 = Axes(
            x_range=(cone_h_min, cone_h_max),
            y_range=(cone_H_min, cone_H_max),
            axis_config={"include_numbers": True}
        )
        axes_labels1 = axes1.get_axis_labels(x_label="h", y_label="H")
        cone_h_H_title = Text("圆锥高度h与水位H关系图", font_size=36).to_edge(UP)

        h_values = np.linspace(cone_h_min, cone_h_max, 400)
        points_purple = []  # h <= cone_h_crit
        points_pink = []    # h > cone_h_crit

        for h in h_values:
            try:
                H = H_of_h_cone(h)
                if not np.isfinite(H) or H < cone_H_min or H > cone_H_max:
                    continue
                point = axes1.c2p(h, H)
                if h <= cone_h_crit:
                    points_purple.append(point)
                else:
                    points_pink.append(point)
            except Exception:
                continue

        curve_purple = VMobject()
        curve_pink = VMobject()

        if points_purple:
            curve_purple.set_points_smoothly(points_purple)
            curve_purple.set_color(PURPLE)

        if points_pink:
            curve_pink.set_points_smoothly(points_pink)
            curve_pink.set_color(PINK)

        crit_point = axes1.c2p(cone_h_crit, cone_h_crit)
        dot_crit = Dot(crit_point, color=PINK)
        label_crit = MathTex(
            f"h_{{\\text{{crit}}}} = {cone_h_crit:.3f}",
            font_size=36,
            color=PINK
        ).next_to(dot_crit, UP, buff=0.2)

        self.play(Write(cone_h_H_title))
        self.play(Create(axes1), Write(axes_labels1))
        if points_purple:
            self.play(Create(curve_purple), run_time=2)
        self.play(Create(dot_crit), Write(label_crit))
        if points_pink:
            self.play(Create(curve_pink), run_time=2)

        self.wait(6)

        cone_h_H_to_remove = VGroup(axes1, axes_labels1, curve_purple, curve_pink, dot_crit, label_crit)
        return cone_h_H_title, cone_h_H_to_remove

    def show_cone_err_H_H_linear_curve(self, cone_h_max, cone_h_H_title, cone_h_H_to_remove):
        err_cone_h_min, err_cone_h_max = cone_h_crit, cone_h_max
        err_min, err_max = 0, 0.4

        axes2 = Axes(
            x_range=(err_cone_h_min, err_cone_h_max),
            y_range=(err_min, err_max, 0.08),
            axis_config={"include_numbers": True}
        )
        axes_labels2 = axes2.get_axis_labels(x_label="h", y_label=r"H_{\text{linear}} - H")
        title2 = Text("圆锥部分浸没时的误差分析", font_size=36).to_edge(UP)

        err_h_vals = np.linspace(err_cone_h_min, err_cone_h_max, 250)
        err_points = []
        for h in err_h_vals:
            try:
                H_actual = H_of_h_cone(h)
                H_linear = linear_model_H_cone(h)
                error = H_linear - H_actual
                if err_min <= error <= err_max:
                    err_points.append(axes2.c2p(h, error))
            except Exception:
                continue

        error_curve = VMobject()
        if err_points:
            error_curve.set_points_smoothly(err_points)
            error_curve.set_color(PINK)

        initial_view = VGroup(axes2, axes_labels2)

        self.play(
            ReplacementTransform(cone_h_H_to_remove, initial_view),
            ReplacementTransform(cone_h_H_title, title2)
        )
        self.play(Create(error_curve), run_time=2)

        self.wait(4)

        self.play(FadeOut(initial_view), FadeOut(error_curve), FadeOut(title2))

    def show_parabola_h_H_curve(self, parabola_h_min, parabola_h_max, parabola_H_min, parabola_H_max):
        axes1 = Axes(
            x_range=(parabola_h_min, parabola_h_max, 8),
            y_range=(parabola_H_min, parabola_H_max, 8),
            axis_config={"include_numbers": True}
        )
        axes_labels1 = axes1.get_axis_labels(x_label="h", y_label="H")
        title = Text("抛物线旋转体高度h与水位H关系图", font_size=36).to_edge(UP)

        h_values = np.linspace(parabola_h_min, parabola_h_max, 1200)
        points_purple = []  # h <= parabola_h_crit
        points_pink = []    # h > parabola_h_crit

        for h in h_values:
            try:
                H = H_of_h_parabola(h)
                if not np.isfinite(H) or H < parabola_H_min or H > parabola_H_max:
                    continue
                point = axes1.c2p(h, H)
                if h <= parabola_h_crit:
                    points_purple.append(point)
                else:
                    points_pink.append(point)
            except Exception:
                continue

        curve_purple = VMobject()
        curve_pink = VMobject()

        if points_purple:
            curve_purple.set_points_smoothly(points_purple)
            curve_purple.set_color(PURPLE)

        if points_pink:
            curve_pink.set_points_smoothly(points_pink)
            curve_pink.set_color(PINK)

        crit_point = axes1.c2p(parabola_h_crit, H_of_h_parabola(parabola_h_crit))
        dot_crit = Dot(crit_point, color=PINK)
        label_crit = MathTex(
            f"h_{{\\text{{crit}}}} = {parabola_h_crit:.3f}",
            font_size=36,
            color=PINK
        ).next_to(dot_crit, DOWN + RIGHT, buff=0.2)

        self.play(Write(title))
        self.play(Create(axes1), Write(axes_labels1))
        if points_purple:
            self.play(Create(curve_purple), run_time=2)
        self.play(Create(dot_crit), Write(label_crit))
        if points_pink:
            self.play(Create(curve_pink), run_time=2)

        self.wait(6)

        parabola_h_H_to_remove = VGroup(axes1, axes_labels1, curve_purple, curve_pink, dot_crit, label_crit)
        return title, parabola_h_H_to_remove

    def show_parabola_err_H_H_linear_curve(self, parabola_h_max, title_old, group_old):
        err_h_min, err_h_max = parabola_h_crit, parabola_h_max
        err_min, err_max = 0, 0.03

        axes2 = Axes(
            x_range=(err_h_min, err_h_max, 4),
            y_range=(err_min, err_max, 0.006),
            axis_config={"include_numbers": True}
        )
        axes_labels2 = axes2.get_axis_labels(x_label="h", y_label=r"H_{\text{linear}} - H")
        title2 = Text("抛物线旋转体部分浸没时的误差分析", font_size=36).to_edge(UP)

        err_h_vals = np.linspace(err_h_min, err_h_max, 600)
        err_points = []
        for h in err_h_vals:
            try:
                H_actual = H_of_h_parabola(h)
                H_linear = linear_model_H_parabola(h)
                error = H_linear - H_actual
                if err_min <= error <= err_max:
                    err_points.append(axes2.c2p(h, error))
            except Exception:
                continue

        error_curve = VMobject()
        if err_points:
            error_curve.set_points_smoothly(err_points)
            error_curve.set_color(PINK)

        initial_view = VGroup(axes2, axes_labels2)

        self.play(
            ReplacementTransform(group_old, initial_view),
            ReplacementTransform(title_old, title2)
        )
        self.play(Create(error_curve), run_time=2)
        self.wait(4)

        parabola_err_curve_to_remove = VGroup(title2, axes2, axes_labels2, error_curve)
        return parabola_err_curve_to_remove

    def construct(self):
        cone_h_min, cone_h_max = 0, 20
        cone_H_min, cone_H_max = 0, 16

        cone_h_H_title, cone_h_H_to_remove = self.show_cone_h_H_curve(cone_h_min, cone_h_max, cone_H_min, cone_H_max)

        self.show_cone_err_H_H_linear_curve(cone_h_max, cone_h_H_title, cone_h_H_to_remove)

        parabola_h_min, parabola_h_max = 0, 60
        parabola_H_min, parabola_H_max = 0, 60
        parabola_title, parabola_h_H_to_remove = self.show_parabola_h_H_curve(
            parabola_h_min, parabola_h_max, parabola_H_min, parabola_H_max
        )

        self.show_parabola_err_H_H_linear_curve(parabola_h_max, parabola_title, parabola_h_H_to_remove)
