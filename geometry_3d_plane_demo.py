from manim import *
from water_level_curve.plane_geometry import PlaneCuboid, PlaneCylinder


class Geometry3dPlaneDemo(Scene):
    def construct(self):
        water_tank = PlaneCuboid(2, 1, 4)
        self.play(FadeIn(water_tank.cuboid))
        water = PlaneCuboid(2, 1, 2, color=BLUE, front_center=(0, -1), need_top_face=True)
        self.play(FadeIn(water.cuboid))
        cylinder = PlaneCylinder(0.5, 2, center=(0.25, 1.25))
        self.play(FadeIn(cylinder.cylinder))
        self.wait(2)

        for _ in range(3):
            add_height_animates1 = water.add_height(0.5)
            self.play(
                cylinder.cylinder.animate.shift(2 * DOWN),
                *add_height_animates1
            )
            self.wait()
            add_height_animates2 = water.add_height(-0.5)
            self.play(
                cylinder.cylinder.animate.shift(2 * UP),
                *add_height_animates2
            )
            self.wait()

        geometries_to_move = VGroup(water_tank.cuboid, water.cuboid, cylinder.cylinder)
        self.play(geometries_to_move.animate.shift(5.5 * RIGHT + 2 * UP).scale(0.5))
        self.wait(2)
