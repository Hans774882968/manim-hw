from manim import *
import os
import sys
from pathlib import Path
from typing import List

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
        COLORS = [PURE_RED, "#ffc000", YELLOW, "#fff2cc", WHITE]
        RANK_LABELS = ["夯", "顶级", "人上人", "NPC", "拉"]
        RANK_COLOR_MP = {
            "夯": PURE_RED,
            "顶级": "#ffc000",
            "人上人": YELLOW,
            "NPC": "#fff2cc",
            "拉": WHITE
        }
        ROW_COUNT = len(RANK_LABELS)
        STROKE_WIDTH = 2
        STROKE_LOGIC_WIDTH = STROKE_WIDTH / config.pixel_width * config.frame_width
        STROKE_LOGIC_HEIGHT = STROKE_WIDTH / config.pixel_height * config.frame_height
        LABEL_WIDTH = config.frame_width * 0.2 - STROKE_LOGIC_WIDTH
        self.RANK_LIST_BG_CFG = {
            "total_height": TOTAL_HEIGHT,
            "colors": COLORS,
            "rank_labels": RANK_LABELS,
            "rank_color_mp": RANK_COLOR_MP,
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

    def bg_insert_into_rank(self, to_shrink: Group, next_bg: RankListBg, label_index: int, img_final_height, pre_wait=0, move_run_time=1):
        self.play(to_shrink.animate.scale(0.8))
        if pre_wait:
            self.wait(pre_wait)
        self.play(
            to_shrink.animate.scale_to_fit_height(img_final_height).next_to(next_bg.label_rect_list[label_index], RIGHT, buff=self.RANK_LIST_BG_CFG['content_left_buff']),
            run_time=move_run_time
        )

    def draw_label_rect_list(self, labels: List[str]):
        label_rect_list = []
        label_text_list = []
        for label in labels:
            fill_color = self.RANK_LIST_BG_CFG['rank_color_mp'].get(label, WHITE)
            rect_height = self.RANK_LIST_BG_CFG['row_height'] * 1.5
            label_rect = Rectangle(
                width=rect_height,
                height=rect_height,
                fill_color=fill_color,
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=self.RANK_LIST_BG_CFG['stroke_width']
            )

            label_text = Text(label, font_size=40, weight=ULTRABOLD, color=BLACK)
            if label_rect_list:
                label_rect.next_to(label_rect_list[-1], RIGHT, buff=0)
            label_text.move_to(label_rect.get_center())

            label_rect_list.append(label_rect)
            label_text_list.append(label_text)

        label_rect_vg = VGroup(*label_rect_list, *label_text_list)
        label_rect_vg.move_to(ORIGIN)
        return label_rect_vg

    def construct(self):
        self.add_watermark()

        bg1 = self.draw_rank_list_bg()
        bg2 = self.draw_rank_list_bg()
        bg3 = self.draw_rank_list_bg()
        bg4 = self.draw_rank_list_bg()
        bg5 = self.draw_rank_list_bg()

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

        self.wait(7)  # 首先出场的是

        self.play(
            LaggedStart(
                FadeIn(react_svg_mo),
                FadeIn(tailwind_svg_mo),
                FadeIn(ts_svg_mo),
                FadeIn(vite_png_mo),
                FadeIn(vue_svg_mo),
                lag_ratio=0.3,
                run_time=4  # 这句话说完的耗时大概比4s多一点
            )
        )
        self.wait(12)  # 酌情给到NPC吧
        self.play(
            react_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(bg5.label_rect_list[3], RIGHT, buff=self.RANK_LIST_BG_CFG['content_left_buff']),
            run_time=0.25
        )
        self.play(
            tailwind_svg_mo.animate.next_to(react_svg_mo, RIGHT, buff=self.RANK_LIST_BG_CFG['svg_final_gap']),
            run_time=0.25
        )
        self.play(
            ts_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(tailwind_svg_mo, RIGHT, buff=self.RANK_LIST_BG_CFG['svg_final_gap']),
            run_time=0.25
        )
        self.play(
            vite_png_mo.animate.scale_to_fit_height(img_final_height).next_to(ts_svg_mo, RIGHT, buff=self.RANK_LIST_BG_CFG['svg_final_gap']),
            run_time=0.25
        )
        self.play(
            vue_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(vite_png_mo, RIGHT, buff=self.RANK_LIST_BG_CFG['svg_final_gap']),
            run_time=0.25
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
                lag_ratio=0.3,
                run_time=2  # “接着出场的是Angular和Redux”说完的耗时大概比2s多一点
            )
        )
        self.wait(5)  # 比“拉完了”靠前一点点，耗时4s左右
        self.play(
            angular_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(bg5.label_rect_list[4], RIGHT, buff=self.RANK_LIST_BG_CFG['content_left_buff']),
            run_time=0.4
        )
        self.play(
            redux_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(angular_svg_mo, RIGHT, buff=self.RANK_LIST_BG_CFG['svg_final_gap']),
            run_time=0.4
        )
        frontend_svg_la = VGroup(angular_svg_mo, redux_svg_mo)

        bun_svg_mo = SVGMobject(BUN_SVG)
        bun_svg_mo.scale_to_fit_height(img_initial_height)
        self.play(FadeIn(bun_svg_mo))
        self.wait(8)  # 给到人上人
        self.play(
            bun_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(bg5.label_rect_list[2], RIGHT, buff=self.RANK_LIST_BG_CFG['content_left_buff']),
            run_time=0.8
        )
        self.wait(2)  # 等待“接下来我们迎来了”说完

        wasm_svg_mo = SVGMobject(WASM_SVG)
        wasm_svg_mo.scale_to_fit_height(img_initial_height)
        self.play(FadeIn(wasm_svg_mo))
        self.wait(16)  # 从“前端大祭司”那句到“综合下给到顶级”之前
        self.play(
            wasm_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(bg5.label_rect_list[1], RIGHT, buff=self.RANK_LIST_BG_CFG['content_left_buff']),
        )
        self.wait(2)

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
                lag_ratio=0.3,
                run_time=3  # 这句话耗时比3s多一点点
            )
        )
        self.wait(8)  # 必须给到夯！
        self.play(
            postgresql_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(bg5.label_rect_list[0], RIGHT, buff=self.RANK_LIST_BG_CFG['content_left_buff']),
            run_time=0.5
        )
        self.play(
            redis_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(postgresql_svg_mo, RIGHT, buff=self.RANK_LIST_BG_CFG['svg_final_gap']),
            run_time=0.5
        )
        self.wait()
        backend_svg_hang = VGroup(postgresql_svg_mo, redis_svg_mo)

        pandas_svg_mo = SVGMobject(PANDAS_SVG)
        pandas_svg_mo.scale_to_fit_height(img_initial_height)
        self.play(FadeIn(pandas_svg_mo))
        self.wait(7)  # 跟前端坐一桌，拉完了
        self.play(
            pandas_svg_mo.animate.scale_to_fit_height(img_final_height).next_to(redux_svg_mo, RIGHT, buff=self.RANK_LIST_BG_CFG['svg_final_gap']),
        )
        self.wait(2)

        # TODO: 对顺序有依赖，这可能不是一个好做法。 bg5 必须放最前面
        to_shrink5 = Group(bg5.rank_list_rows, frontend_svg_npc, frontend_svg_la, bun_svg_mo, wasm_svg_mo, backend_svg_hang, pandas_svg_mo)
        self.bg_insert_into_rank(to_shrink5, bg4, 0, img_final_height, pre_wait=2)
        self.wait(3)

        to_shrink4 = Group(bg4.rank_list_rows, to_shrink5)
        self.bg_insert_into_rank(to_shrink4, bg3, 4, img_final_height, pre_wait=12)
        self.wait(3)

        to_shrink3 = Group(bg3.rank_list_rows, to_shrink4)
        self.bg_insert_into_rank(to_shrink3, bg2, 3, img_final_height, pre_wait=8)
        self.wait(3)

        npc_hang_video = self.draw_label_rect_list(['NPC', '夯', '原视频'])
        self.play(
            FadeIn(npc_hang_video),
            run_time=2
        )
        self.wait(13)  # 给给视频评夯评NPC必须给到夯！
        self.play(
            npc_hang_video.animate.scale_to_fit_height(img_final_height).next_to(bg2.label_rect_list[0], RIGHT, buff=self.RANK_LIST_BG_CFG['content_left_buff']),
            run_time=3
        )
        self.wait(2)

        to_shrink2 = Group(bg2.rank_list_rows, npc_hang_video, to_shrink3)
        self.bg_insert_into_rank(to_shrink2, bg1, 0, img_final_height, pre_wait=3, move_run_time=1.5)
        self.wait(3)
