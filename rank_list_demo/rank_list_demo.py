from manim import *
import os
import sys

sys.path.append(os.getcwd())

from m_objects.moving_watermark import MovingWatermark


class RankListDemo(Scene):
    def add_watermark(self):
        watermark = MovingWatermark("Hans码数理哲", font_size=20, color="#a1a1a1", z_index=114)
        watermark.add_updater(watermark.update_position)
        self.add(watermark)

    def construct(self):
        self.add_watermark()

        total_height = config.frame_height * 0.9
        row_count = 5
        row_height = total_height / row_count

        label_width = config.frame_width * 0.2

        colors = [PURE_RED, "#ffc000", YELLOW, "#fff2cc", WHITE]
        rank_labels = ["夯", "顶级", "人上人", "NPC", "拉"]

        rank_list_rows = VGroup()
        for i in range(row_count):
            label_rect = Rectangle(
                width=label_width,
                height=row_height,
                fill_color=colors[i],
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=2
            )

            label_text = Text(rank_labels[i], font_size=60, weight=ULTRABOLD, color=BLACK)
            label_text.move_to(label_rect.get_center())

            content_rect = Rectangle(
                width=config.frame_width - label_width,
                height=row_height,
                fill_color="#1a1a17",
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=2
            )
            content_rect.next_to(label_rect, RIGHT, buff=0)

            placeholder_text = Text("拖放内容到这里", font_size=24, color=GRAY)
            placeholder_text.move_to(content_rect.get_center())

            row = VGroup(label_rect, label_text, content_rect, placeholder_text)
            rank_list_rows.add(row)
        rank_list_rows.arrange(DOWN, buff=0)
        self.add(rank_list_rows)
        self.wait(25)
