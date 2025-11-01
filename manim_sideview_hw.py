from manim import *


# manim sideview vscode 插件的使用
class ManimSideViewHw(Scene):
    def construct(self):
        yellow_arrow = NumberLine(  # HEREFROM
            x_range=[0, 4, 1],
            length=2,
            include_tip=True,
            color=YELLOW,
            include_numbers=True,
            rotation=30 * DEGREES,
        )
        self.add(yellow_arrow.move_to(ORIGIN))  # HERETO
        self.wait()

        for _ in range(3):
            self.play(yellow_arrow.animate.rotate(30 * DEGREES))
            self.wait()

        check = Tex(r'\checkmark', color=GREEN, stroke_width=8).scale(3)
        check.stretch(0.8, dim=1)
        check.stretch(1.1, dim=0)
        check.next_to(yellow_arrow, DOWN)
        self.add(check)
        self.wait()

        self.play(FadeOut(check), FadeOut(yellow_arrow))

        matrix_foo = Matrix([[11, 45, 14], [-19, 198, 10]],
                            v_buff=0.8,
                            h_buff=1.2,
                            bracket_h_buff=SMALL_BUFF,
                            bracket_v_buff=SMALL_BUFF)
        matrix_foo.set_row_colors(YELLOW, YELLOW)
        self.add(matrix_foo)
        self.wait()
        self.play(FadeOut(matrix_foo))

        plane = ComplexPlane().add_coordinates()
        d1 = Dot(plane.n2p(2 + 1j), color=YELLOW)
        d2 = Dot(plane.n2p(-3 - 2j), color=YELLOW)
        label1 = MathTex('2+i').next_to(d1, UR, 0.1)
        label2 = MathTex('-3-2i').next_to(d2, UR, 0.1)
        self.add(plane, d1, label1, d2, label2)
        self.wait(3)
        self.play(FadeOut(plane), FadeOut(d1), FadeOut(label1), FadeOut(d2), FadeOut(label2))

        def stream_func(pos):
            return ((pos[0] * UR + pos[1] * LEFT) - pos)
        stream_lines = StreamLines(stream_func, x_range=[-5, 5, 1], y_range=[-5, 5, 1], stroke_width=3)
        self.add(stream_lines)
        self.wait(3)
        self.play(FadeOut(stream_lines))

        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                 (2, 8), (3, 4), (6, 1), (6, 2),
                 (6, 3), (7, 2), (7, 4)]
        g = Graph(vertices, edges, layout='circular', layout_scale=3,
                  labels=True, vertex_config={7: {'fill_color': RED}},
                  edge_config={(1, 7): {'stroke_color': RED},
                               (2, 7): {'stroke_color': RED},
                               (4, 7): {'stroke_color': RED}})
        self.add(g)
        self.wait(3)
