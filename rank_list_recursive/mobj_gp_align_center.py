from manim import *
from pathlib import Path

ASSETS_DIR = Path("assets") / "rank_list_recursive"

REACT_SVG = ASSETS_DIR / 'react-original.svg'
TAILWIND_SVG = ASSETS_DIR / 'tailwindcss-original-wordmark.svg'
TS_SVG = ASSETS_DIR / 'typescript-original.svg'
VITE_PNG = ASSETS_DIR / 'vite.png'
VUE_SVG = ASSETS_DIR / 'vuejs-original-wordmark.svg'


class MobjGpAlignCenter(Scene):
    def construct(self):
        initial_height_large = 1.5
        initial_height_small = 0.3
        img_final_height = 1

        react_svg_mo = SVGMobject(REACT_SVG)
        tailwind_svg_mo = SVGMobject(TAILWIND_SVG)
        ts_svg_mo = SVGMobject(TS_SVG)
        vite_png_mo = ImageMobject(VITE_PNG)
        vue_svg_mo = SVGMobject(VUE_SVG)
        react_svg_mo.scale_to_fit_height(initial_height_large)
        tailwind_svg_mo.scale_to_fit_height(initial_height_small)
        tailwind_svg_mo.next_to(react_svg_mo, RIGHT)
        ts_svg_mo.scale_to_fit_height(initial_height_large)
        ts_svg_mo.next_to(react_svg_mo, DOWN)
        vite_png_mo.scale_to_fit_height(initial_height_large)
        vite_png_mo.next_to(ts_svg_mo, RIGHT)
        vue_svg_mo.scale_to_fit_height(initial_height_large)
        vue_svg_mo.next_to(vite_png_mo, RIGHT)

        # 直接这样就能轻松实现居中，不需要像 rank_list_recursive.py 那样写 react_svg_mo.move_to(ORIGIN + 2 * UL)
        frontend_svg_npc = Group(react_svg_mo, tailwind_svg_mo, ts_svg_mo, vite_png_mo, vue_svg_mo)
        frontend_svg_npc.move_to(ORIGIN)

        self.play(
            LaggedStart(
                FadeIn(react_svg_mo),
                FadeIn(tailwind_svg_mo),
                FadeIn(ts_svg_mo),
                FadeIn(vite_png_mo),
                FadeIn(vue_svg_mo),
                lag_ratio=0.3,
                run_time=2
            )
        )
        self.wait(2)

        self.play(
            react_svg_mo.animate.scale_to_fit_height(img_final_height).to_edge(UL, buff=0),
            run_time=0.25
        )
        self.play(
            tailwind_svg_mo.animate.next_to(react_svg_mo, RIGHT, buff=0.1),
            run_time=0.25
        )
        self.play(
            ts_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(tailwind_svg_mo, RIGHT, buff=0.1),
            run_time=0.25
        )
        self.play(
            vite_png_mo.animate.scale_to_fit_height(img_final_height).next_to(ts_svg_mo, RIGHT, buff=0.1),
            run_time=0.25
        )
        self.play(
            vue_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(vite_png_mo, RIGHT, buff=0.1),
            run_time=0.25
        )
        self.wait(2)
