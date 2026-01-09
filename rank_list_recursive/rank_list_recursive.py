from manim import *
import os
import sys
from pathlib import Path

sys.path.append(os.getcwd())

from m_objects.moving_watermark import MovingWatermark

ASSETS_DIR = Path("assets") / "rank_list_recursive"

'''前端'''
# 拉
ANGULAR_SVG = ASSETS_DIR / 'angularjs-plain.svg'
REDUX_SVG = ASSETS_DIR / 'redux-original.svg'
# npc
REACT_SVG = ASSETS_DIR / 'react-original.svg'
TAILWIND_SVG = ASSETS_DIR / 'tailwindcss-original-wordmark.svg'
TS_SVG = ASSETS_DIR / 'typescript-original.svg'
VITE_PNG = ASSETS_DIR / 'vite.png'
VUE_SVG = ASSETS_DIR / 'vuejs-original-wordmark.svg'
# 人上人
BUN_SVG = ASSETS_DIR / 'bun-original.svg'
# 顶级
WASM_SVG = ASSETS_DIR / 'wasm-original-wordmark.svg'
'''后端'''
# 拉
PANDAS_SVG = ASSETS_DIR / 'pandas-original-wordmark.svg'
# 夯
POSTGRESQL_SVG = ASSETS_DIR / 'postgresql-original-wordmark.svg'
REDIS_SVG = ASSETS_DIR / 'redis-original-wordmark.svg'


class RankListBg:
    def __init__(self, rank_list_rows, label_rect_list, content_rect_list):
        self.rank_list_rows = rank_list_rows
        self.label_rect_list = label_rect_list
        self.content_rect_list = content_rect_list


class RankListDemo(Scene):
    def setup(self):
        TOTAL_HEIGHT = config.frame_height * 0.9
        RANK_LABELS = ["夯", "顶级", "人上人", "NPC", "拉"]
        ROW_COUNT = len(RANK_LABELS)
        STROKE_WIDTH = 2
        STROKE_LOGIC_WIDTH = STROKE_WIDTH / config.pixel_width * config.frame_width
        STROKE_LOGIC_HEIGHT = STROKE_WIDTH / config.pixel_height * config.frame_height
        LABEL_WIDTH = config.frame_width * 0.2 - STROKE_LOGIC_WIDTH
        self.RANK_LIST_BG_CFG = {
            "total_height": TOTAL_HEIGHT,
            "colors": [PURE_RED, "#ffc000", YELLOW, "#fff2cc", WHITE],
            "rank_labels": RANK_LABELS,
            "row_count": len(RANK_LABELS),
            "stroke_width": STROKE_WIDTH,
            "stroke_logic_width": STROKE_LOGIC_WIDTH,
            "stroke_logic_height": STROKE_LOGIC_HEIGHT,
            "label_width": LABEL_WIDTH,
            "content_rect_width": config.frame_width - LABEL_WIDTH - STROKE_LOGIC_WIDTH,
            "row_height": (TOTAL_HEIGHT - STROKE_LOGIC_HEIGHT) / ROW_COUNT,
            "content_left_buff": STROKE_LOGIC_WIDTH * 0.5,
            "svg_final_gap": 0.1,
        }

    def add_watermark(self):
        watermark = MovingWatermark("Hans码数理哲", font_size=20, color="#a1a1a1", z_index=114)
        watermark.add_updater(watermark.update_position)
        self.add(watermark)

    def draw_rank_list_bg(self):
        rank_list_rows = VGroup()

        label_rect_list = []
        content_rect_list = []

        for i in range(self.RANK_LIST_BG_CFG['row_count']):
            label_rect = Rectangle(
                width=self.RANK_LIST_BG_CFG['label_width'],
                height=self.RANK_LIST_BG_CFG['row_height'],
                fill_color=self.RANK_LIST_BG_CFG['colors'][i],
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=self.RANK_LIST_BG_CFG['stroke_width']
            )

            label_text = Text(self.RANK_LIST_BG_CFG['rank_labels'][i], font_size=60, weight=ULTRABOLD, color=BLACK)
            label_text.move_to(label_rect.get_center())

            content_rect = Rectangle(
                width=self.RANK_LIST_BG_CFG['content_rect_width'],
                height=self.RANK_LIST_BG_CFG['row_height'],
                fill_color="#1a1a17",
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=self.RANK_LIST_BG_CFG['stroke_width']
            )
            content_rect.next_to(label_rect, RIGHT, buff=0)

            placeholder_text = Text("拖放内容到这里", font_size=24, color=GRAY)
            placeholder_text.move_to(content_rect.get_center())

            row = VGroup(label_rect, label_text, content_rect, placeholder_text)
            rank_list_rows.add(row)

            label_rect_list.append(label_rect)
            content_rect_list.append(content_rect)

        rank_list_rows.arrange(DOWN, buff=0)
        self.add(rank_list_rows)

        return RankListBg(rank_list_rows, label_rect_list, content_rect_list)

    def bg_insert_into_rank(self, to_shrink: Group, next_bg: RankListBg, label_index: int, img_final_height):
        self.play(to_shrink.animate.scale(0.8))
        self.play(
            to_shrink.animate.scale_to_fit_height(img_final_height).next_to(next_bg.label_rect_list[label_index], RIGHT, buff=self.RANK_LIST_BG_CFG['content_left_buff']),
            run_time=1.5
        )
        self.wait()

    def construct(self):
        self.add_watermark()

        bg1 = self.draw_rank_list_bg()
        bg2 = self.draw_rank_list_bg()
        bg3 = self.draw_rank_list_bg()
        bg4 = self.draw_rank_list_bg()

        img_initial_height = 1.5 * self.RANK_LIST_BG_CFG['row_height']
        svg_wordmark_initial_height = 0.3 * self.RANK_LIST_BG_CFG['row_height']
        img_final_height = self.RANK_LIST_BG_CFG['row_height'] - 0.5 * self.RANK_LIST_BG_CFG['stroke_logic_height']

        react_svg_mo = SVGMobject(REACT_SVG)
        tailwind_svg_mo = SVGMobject(TAILWIND_SVG)
        ts_svg_mo = SVGMobject(TS_SVG)
        vite_png_mo = ImageMobject(VITE_PNG)
        vue_svg_mo = SVGMobject(VUE_SVG)
        react_svg_mo.scale_to_fit_height(img_initial_height)
        react_svg_mo.move_to(ORIGIN + 2 * UL)
        tailwind_svg_mo.scale_to_fit_height(svg_wordmark_initial_height)
        tailwind_svg_mo.next_to(react_svg_mo, RIGHT)
        ts_svg_mo.scale_to_fit_height(img_initial_height)
        ts_svg_mo.next_to(react_svg_mo, DOWN)
        vite_png_mo.scale_to_fit_height(img_initial_height)
        vite_png_mo.next_to(ts_svg_mo, RIGHT)
        vue_svg_mo.scale_to_fit_height(img_initial_height)
        vue_svg_mo.next_to(vite_png_mo, RIGHT)

        self.play(
            LaggedStart(
                FadeIn(react_svg_mo),
                FadeIn(tailwind_svg_mo),
                FadeIn(ts_svg_mo),
                FadeIn(vite_png_mo),
                FadeIn(vue_svg_mo),
                lag_ratio=0.3
            )
        )
        self.play(
            react_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(bg1.label_rect_list[3], RIGHT, buff=self.RANK_LIST_BG_CFG['content_left_buff']),
            run_time=0.4
        )
        self.play(
            tailwind_svg_mo.animate.next_to(react_svg_mo, RIGHT, buff=self.RANK_LIST_BG_CFG['svg_final_gap']),
            run_time=0.4
        )
        self.play(
            ts_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(tailwind_svg_mo, RIGHT, buff=self.RANK_LIST_BG_CFG['svg_final_gap']),
            run_time=0.4
        )
        self.play(
            vite_png_mo.animate.scale_to_fit_height(img_final_height).next_to(ts_svg_mo, RIGHT, buff=self.RANK_LIST_BG_CFG['svg_final_gap']),
            run_time=0.4
        )
        self.play(
            vue_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(vite_png_mo, RIGHT, buff=self.RANK_LIST_BG_CFG['svg_final_gap']),
            run_time=0.4
        )
        frontend_svg_npc = Group(react_svg_mo, tailwind_svg_mo, ts_svg_mo, vite_png_mo, vue_svg_mo)

        angular_svg_mo = SVGMobject(ANGULAR_SVG)
        redux_svg_mo = SVGMobject(REDUX_SVG)
        angular_svg_mo.scale_to_fit_height(img_initial_height)
        angular_svg_mo.move_to(ORIGIN + LEFT)
        redux_svg_mo.scale_to_fit_height(img_initial_height)
        redux_svg_mo.next_to(angular_svg_mo, RIGHT)
        self.play(
            LaggedStart(
                FadeIn(angular_svg_mo),
                FadeIn(redux_svg_mo),
                lag_ratio=0.3
            )
        )
        self.play(
            angular_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(bg1.label_rect_list[4], RIGHT, buff=self.RANK_LIST_BG_CFG['content_left_buff']),
            run_time=0.5
        )
        self.play(
            redux_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(angular_svg_mo, RIGHT, buff=self.RANK_LIST_BG_CFG['svg_final_gap']),
            run_time=0.5
        )
        frontend_svg_la = VGroup(angular_svg_mo, redux_svg_mo)

        bun_svg_mo = SVGMobject(BUN_SVG)
        bun_svg_mo.scale_to_fit_height(img_initial_height)
        self.play(FadeIn(bun_svg_mo))
        self.play(
            bun_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(bg1.label_rect_list[2], RIGHT, buff=self.RANK_LIST_BG_CFG['content_left_buff']),
        )

        wasm_svg_mo = SVGMobject(WASM_SVG)
        wasm_svg_mo.scale_to_fit_height(img_initial_height)
        self.play(FadeIn(wasm_svg_mo))
        self.play(
            wasm_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(bg1.label_rect_list[1], RIGHT, buff=self.RANK_LIST_BG_CFG['content_left_buff']),
        )

        postgresql_svg_mo = SVGMobject(POSTGRESQL_SVG)
        redis_svg_mo = SVGMobject(REDIS_SVG)
        postgresql_svg_mo.scale_to_fit_height(img_initial_height)
        postgresql_svg_mo.move_to(ORIGIN + LEFT)
        redis_svg_mo.scale_to_fit_height(img_initial_height)
        redis_svg_mo.next_to(postgresql_svg_mo, RIGHT)
        self.play(
            LaggedStart(
                FadeIn(postgresql_svg_mo),
                FadeIn(redis_svg_mo),
                lag_ratio=0.3
            )
        )
        self.play(
            postgresql_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(bg1.label_rect_list[0], RIGHT, buff=self.RANK_LIST_BG_CFG['content_left_buff']),
            run_time=0.5
        )
        self.play(
            redis_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(postgresql_svg_mo, RIGHT, buff=self.RANK_LIST_BG_CFG['svg_final_gap']),
            run_time=0.5
        )
        backend_svg_hang = VGroup(postgresql_svg_mo, redis_svg_mo)

        pandas_svg_mo = SVGMobject(PANDAS_SVG)
        pandas_svg_mo.scale_to_fit_height(img_initial_height)
        self.play(FadeIn(pandas_svg_mo))
        self.play(
            pandas_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(redux_svg_mo, RIGHT, buff=self.RANK_LIST_BG_CFG['svg_final_gap']),
        )

        # TODO: 对顺序有依赖，这可能不是一个好做法。 bg1 必须放最前面
        to_shrink1 = Group(bg1.rank_list_rows, frontend_svg_npc, frontend_svg_la, bun_svg_mo, wasm_svg_mo, backend_svg_hang, pandas_svg_mo)
        self.bg_insert_into_rank(to_shrink1, bg2, 0, img_final_height)

        to_shrink2 = Group(bg2.rank_list_rows, to_shrink1)
        self.bg_insert_into_rank(to_shrink2, bg3, 4, img_final_height)

        to_shrink3 = Group(bg3.rank_list_rows, to_shrink2)
        self.bg_insert_into_rank(to_shrink3, bg4, 3, img_final_height)
