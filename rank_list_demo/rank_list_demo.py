from manim import *
import os
import sys

sys.path.append(os.getcwd())

from m_objects.moving_watermark import MovingWatermark


class RankListDemo(Scene):
    '''
    TODO: 增大 STROKE_WIDTH 会发现，第一张图会停在 content_rect 黑色部分稍微靠左的位置
    但实测发现这个位置并不是 0.5 倍线宽。以及现在设置的高度也不完全契合content_rect 黑色部分
    直觉上看会觉得都是 0.5 倍线宽，但实测都不是
    这两个问题都不知道如何解决，但无伤大雅，就不管了
    '''

    def add_watermark(self):
        watermark = MovingWatermark("Hans码数理哲", font_size=20, color="#a1a1a1", z_index=114)
        watermark.add_updater(watermark.update_position)
        self.add(watermark)

    def construct(self):
        self.add_watermark()

        total_height = config.frame_height * 0.9
        colors = [PURE_RED, "#ffc000", YELLOW, "#fff2cc", WHITE]
        rank_labels = ["夯", "顶级", "人上人", "NPC", "拉"]
        row_count = len(rank_labels)
        STROKE_WIDTH = 2
        STROKE_LOGIC_WIDTH = STROKE_WIDTH / config.pixel_width * config.frame_width
        STROKE_LOGIC_HEIGHT = STROKE_WIDTH / config.pixel_height * config.frame_height
        label_width = config.frame_width * 0.2 - STROKE_LOGIC_WIDTH
        content_rect_width = config.frame_width - label_width - STROKE_LOGIC_WIDTH
        row_height = (total_height - STROKE_LOGIC_HEIGHT) / row_count

        rank_list_rows = VGroup()

        label_rect_list = []
        content_rect_list = []

        for i in range(row_count):
            label_rect = Rectangle(
                width=label_width,
                height=row_height,
                fill_color=colors[i],
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=STROKE_WIDTH
            )

            label_text = Text(rank_labels[i], font_size=60, weight=ULTRABOLD, color=BLACK)
            label_text.move_to(label_rect.get_center())

            content_rect = Rectangle(
                width=content_rect_width,
                height=row_height,
                fill_color="#1a1a17",
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=STROKE_WIDTH
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
        self.wait(10)

        img_initial_height = 2 * row_height
        img_final_height = row_height - 0.5 * STROKE_LOGIC_HEIGHT

        img1 = ImageMobject(r"assets\rank_list_demo\谁会React Fiber.jpg")
        img1.scale_to_fit_height(img_initial_height)
        self.play(FadeIn(img1))
        self.wait(10)
        self.play(
            img1.animate.scale_to_fit_height(img_final_height).next_to(label_rect_list[1], RIGHT, buff=STROKE_LOGIC_WIDTH * 0.5),
            run_time=2
        )

        img2 = ImageMobject(r"assets\rank_list_demo\服务员.jpg")
        img2.scale_to_fit_height(img_initial_height)
        self.play(FadeIn(img2))
        self.wait(10)
        self.play(
            img2.animate.scale_to_fit_height(img_final_height).next_to(label_rect_list[3], RIGHT, buff=STROKE_LOGIC_WIDTH * 0.5),
            run_time=2
        )

        img3 = ImageMobject(r"assets\rank_list_demo\爷们要战斗.png")
        img3.scale_to_fit_height(2.5 * row_height)
        self.play(FadeIn(img3))
        self.wait(10)
        self.play(
            img3.animate.scale_to_fit_height(img_final_height).next_to(label_rect_list[2], RIGHT, buff=STROKE_LOGIC_WIDTH * 0.5),
            run_time=2
        )

        img4 = ImageMobject(r"assets\rank_list_demo\进厂.png")
        img4.scale_to_fit_height(img_initial_height)
        self.play(FadeIn(img4))
        self.wait(10)
        self.play(
            img4.animate.scale_to_fit_height(img_final_height).next_to(img2, RIGHT, buff=0),
            run_time=2
        )

        img5 = ImageMobject(r"assets\rank_list_demo\餐饮创业.png")
        img5.scale_to_fit_height(2.5 * row_height)
        self.play(FadeIn(img5))
        self.wait(10)
        self.play(
            img5.animate.scale_to_fit_height(img_final_height).next_to(label_rect_list[4], RIGHT, buff=STROKE_LOGIC_WIDTH * 0.5),
            run_time=2
        )

        img6 = ImageMobject(r"assets\rank_list_demo\葛优躺.jpg")
        img6.scale_to_fit_height(img_initial_height)

        self.play(FadeIn(img6))
        self.wait(10)
        self.play(
            img6.animate.scale_to_fit_height(1.5 * row_height).next_to(label_rect_list[0], RIGHT, buff=STROKE_LOGIC_WIDTH * 0.5),
            run_time=2
        )
        self.play(
            img6.animate.scale_to_fit_height(img_final_height).next_to(img5, RIGHT, buff=0),
            run_time=2
        )

        self.wait(5)
