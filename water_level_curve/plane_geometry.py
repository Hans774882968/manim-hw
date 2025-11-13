from manim import *


class PlaneCuboid:
    def __init__(self, length, width, height, color=WHITE, front_center=(0, 0), need_top_face=False):
        self.front_center_3d = np.array((*front_center, 0))
        A = self.front_center_3d + np.array([-length / 2, -height / 2, 0])  # 前左下
        B = self.front_center_3d + np.array([length / 2, -height / 2, 0])   # 前右下
        C = self.front_center_3d + np.array([length / 2, height / 2, 0])    # 前右上
        D = self.front_center_3d + np.array([-length / 2, height / 2, 0])   # 前左上

        A_prime = A + np.array([width / 2, width / 2, 0])  # 后左下
        B_prime = B + np.array([width / 2, width / 2, 0])  # 后右下
        C_prime = C + np.array([width / 2, width / 2, 0])  # 后右上
        D_prime = D + np.array([width / 2, width / 2, 0])  # 后左上

        self.bottom_center = (A + B_prime) / 2
        self.top_center = (D + C_prime) / 2

        self.edges = [
            Line(A, B, color=color), Line(B, C, color=color), Line(C, D, color=color), Line(D, A, color=color),
            Line(A_prime, B_prime, color=color), Line(B_prime, C_prime, color=color), Line(C_prime, D_prime, color=color), Line(D_prime, A_prime, color=color),
            Line(A, A_prime, color=color), Line(B, B_prime, color=color), Line(C, C_prime, color=color), Line(D, D_prime, color=color)
        ]

        if need_top_face:
            self.top_face = Polygon(D, C, C_prime, D_prime, color=BLUE, fill_opacity=0.6)
            self.top_face.move_to((D + C + C_prime + D_prime) / 4)

        self.cuboid = VGroup(*self.edges, *([self.top_face] if need_top_face else []))

    def add_height(self, delta: float):
        add_height_animates = [
            self.edges[1].animate.put_start_and_end_on(self.edges[1].get_start(), self.edges[1].get_end() + delta * UP),
            self.edges[3].animate.put_start_and_end_on(self.edges[3].get_start() + delta * UP, self.edges[3].get_end()),
            self.edges[5].animate.put_start_and_end_on(self.edges[5].get_start(), self.edges[5].get_end() + delta * UP),
            self.edges[7].animate.put_start_and_end_on(self.edges[7].get_start() + delta * UP, self.edges[7].get_end()),

            self.edges[2].animate.put_start_and_end_on(self.edges[2].get_start() + delta * UP, self.edges[2].get_end() + delta * UP),
            self.edges[6].animate.put_start_and_end_on(self.edges[6].get_start() + delta * UP, self.edges[6].get_end() + delta * UP),
            self.edges[10].animate.put_start_and_end_on(self.edges[10].get_start() + delta * UP, self.edges[10].get_end() + delta * UP),
            self.edges[11].animate.put_start_and_end_on(self.edges[11].get_start() + delta * UP, self.edges[11].get_end() + delta * UP),
            *([self.top_face.animate.shift(delta * UP)] if self.top_face else []),
        ]
        self.top_center = self.bottom_center + delta * (self.top_center - self.bottom_center)
        return add_height_animates


class PlaneCylinder:
    def __init__(self, radius, height, color=WHITE, center=(0, 0)):
        self.center_3d = np.array((*center, 0))
        self.top_center = self.center_3d + np.array([0, height / 2, 0])
        self.bottom_center = self.center_3d + np.array([0, -height / 2, 0])

        top_ellipse = Ellipse(width=2 * radius, height=2 * radius / 2, color=color)
        top_ellipse.move_to(self.top_center)

        bottom_ellipse = Ellipse(width=2 * radius, height=2 * radius / 2, color=color)
        bottom_ellipse.move_to(self.bottom_center)

        left_edge = Line(
            self.top_center + np.array([-radius, 0, 0]),
            self.bottom_center + np.array([-radius, 0, 0]),
            color=color
        )

        right_edge = Line(
            self.top_center + np.array([radius, 0, 0]),
            self.bottom_center + np.array([radius, 0, 0]),
            color=color
        )

        self.cylinder = VGroup(
            top_ellipse, bottom_ellipse,
            left_edge, right_edge,
        )
