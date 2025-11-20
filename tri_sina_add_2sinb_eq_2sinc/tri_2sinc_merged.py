from manim import *
from tri_sina_add_2sinb_eq_2sinc import TriSinAAdd2sinBEq2sinC
from tri_2sinc_sol1 import Tri2sinCSol1
from tri_2sinc_sol2 import Tri2sinCSol2


class Tri2sinCMerged(TriSinAAdd2sinBEq2sinC, Tri2sinCSol1, Tri2sinCSol2):
    def construct(self):
        self.show_bg()
        self.show_title()
        problem_stmt_to_remove = self.show_problem_stmt()
        thought_to_remove = self.show_thought(problem_stmt_to_remove)
        method1_to_remove = self.show_method1(thought_to_remove)
        method2_to_remove = self.show_method2(method1_to_remove)
        method3_to_remove = self.show_method3(method2_to_remove)
        self.show_ending(method3_to_remove)
