from manim import *
from typing import List


class RankListBg:
    def __init__(self, rank_list_rows, label_rect_list, content_rect_list):
        self.rank_list_rows = rank_list_rows
        self.label_rect_list = label_rect_list
        self.content_rect_list = content_rect_list


class RankListBgOverlapCorrect(Scene):
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
        LABEL_WIDTH = config.frame_width * 0.25 - STROKE_LOGIC_WIDTH
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

    def draw_rank_list_bg(self, bg_index: int):
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

            label = f"{self.RANK_LIST_BG_CFG['rank_labels'][i]}{bg_index + 1}"
            label_text = Text(label, font_size=60, weight=ULTRABOLD, color=BLACK)
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
        bg_list: List[RankListBg] = []
        for i in range(5):
            bg_list.append(self.draw_rank_list_bg(i))
        bg1, bg2, bg3, bg4, bg5 = bg_list
        self.wait(2)

        img_final_height = self.RANK_LIST_BG_CFG['row_height'] - 0.5 * self.RANK_LIST_BG_CFG['stroke_logic_height']

        npc_hang_video = self.draw_label_rect_list(['NPC', '夯', '原视频'])
        self.play(
            FadeIn(npc_hang_video),
            run_time=2
        )

        to_shrink5 = Group(bg5.rank_list_rows, npc_hang_video)
        self.bg_insert_into_rank(to_shrink5, bg4, 0, img_final_height, pre_wait=2)
        self.wait(3)

        to_shrink4 = Group(bg4.rank_list_rows, to_shrink5)
        self.bg_insert_into_rank(to_shrink4, bg3, 4, img_final_height, pre_wait=2)
        self.wait(3)
