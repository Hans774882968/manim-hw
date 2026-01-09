## 给初版代码挑错

先写一版效果正确的初版代码，然后让LLM优化写法，最后把图标换了。

```python
from manim import *
import os
import sys

sys.path.append(os.getcwd())

from m_objects.moving_watermark import MovingWatermark


class RankListBg:
    def __init__(self, rank_list_rows, label_rect_list, content_rect_list):
        self.rank_list_rows = rank_list_rows
        self.label_rect_list = label_rect_list
        self.content_rect_list = content_rect_list


class RankListDemo(Scene):
    def setup(self):
        self.TOTAL_HEIGHT = config.frame_height * 0.9
        self.COLORS = [PURE_RED, "#ffc000", YELLOW, "#fff2cc", WHITE]
        self.RANK_LABELS = ["夯", "顶级", "人上人", "NPC", "拉"]
        self.ROW_COUNT = len(self.RANK_LABELS)
        self.STROKE_WIDTH = 2
        self.STROKE_LOGIC_WIDTH = self.STROKE_WIDTH / config.pixel_width * config.frame_width
        self.STROKE_LOGIC_HEIGHT = self.STROKE_WIDTH / config.pixel_height * config.frame_height
        self.label_width = config.frame_width * 0.2 - self.STROKE_LOGIC_WIDTH
        self.content_rect_width = config.frame_width - self.label_width - self.STROKE_LOGIC_WIDTH
        self.ROW_HEIGHT = (self.TOTAL_HEIGHT - self.STROKE_LOGIC_HEIGHT) / self.ROW_COUNT

    def add_watermark(self):
        watermark = MovingWatermark("Hans码数理哲", font_size=20, color="#a1a1a1", z_index=114)
        watermark.add_updater(watermark.update_position)
        self.add(watermark)

    def draw_rank_list_bg(self):
        rank_list_rows = VGroup()

        label_rect_list = []
        content_rect_list = []

        for i in range(self.ROW_COUNT):
            label_rect = Rectangle(
                width=self.label_width,
                height=self.ROW_HEIGHT,
                fill_color=self.COLORS[i],
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=self.STROKE_WIDTH
            )

            label_text = Text(self.RANK_LABELS[i], font_size=60, weight=ULTRABOLD, color=BLACK)
            label_text.move_to(label_rect.get_center())

            content_rect = Rectangle(
                width=self.content_rect_width,
                height=self.ROW_HEIGHT,
                fill_color="#1a1a17",
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=self.STROKE_WIDTH
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

    def construct(self):
        self.add_watermark()

        bg1 = self.draw_rank_list_bg()
        bg2 = self.draw_rank_list_bg()
        bg3 = self.draw_rank_list_bg()
        bg4 = self.draw_rank_list_bg()

        img_initial_height = 2 * self.ROW_HEIGHT
        img_final_height = self.ROW_HEIGHT - 0.5 * self.STROKE_LOGIC_HEIGHT

        img1 = ImageMobject(r"assets\rank_list_demo\谁会React Fiber.jpg")
        img1.scale_to_fit_height(img_initial_height)
        self.play(FadeIn(img1))
        self.play(
            img1.animate.scale_to_fit_height(img_final_height).next_to(bg1.label_rect_list[1], RIGHT, buff=self.STROKE_LOGIC_WIDTH * 0.5),
            run_time=1.5
        )

        img2 = ImageMobject(r"assets\rank_list_demo\服务员.jpg")
        img2.scale_to_fit_height(img_initial_height)
        self.play(FadeIn(img2))
        self.play(
            img2.animate.scale_to_fit_height(img_final_height).next_to(bg1.label_rect_list[3], RIGHT, buff=self.STROKE_LOGIC_WIDTH * 0.5),
            run_time=1.5
        )

        # TODO: 对顺序有依赖，这可能不是一个好做法。 bg1 必须放 img1 前面
        to_shrink1 = Group(bg1.rank_list_rows, img1, img2)
        self.play(to_shrink1.animate.scale(0.5))
        self.play(
            to_shrink1.animate.scale_to_fit_height(img_final_height).next_to(bg2.label_rect_list[0], RIGHT, buff=self.STROKE_LOGIC_WIDTH * 0.5),
            run_time=1.5
        )
        self.wait()

        to_shrink2 = Group(bg2.rank_list_rows, to_shrink1)
        self.play(to_shrink2.animate.scale(0.5))
        self.play(
            to_shrink2.animate.scale_to_fit_height(img_final_height).next_to(bg3.label_rect_list[4], RIGHT, buff=self.STROKE_LOGIC_WIDTH * 0.5),
            run_time=1.5
        )
        self.wait()

        to_shrink3 = Group(bg3.rank_list_rows, to_shrink2)
        self.play(to_shrink3.animate.scale(0.5))
        self.play(
            to_shrink3.animate.scale_to_fit_height(img_final_height).next_to(bg4.label_rect_list[3], RIGHT, buff=self.STROKE_LOGIC_WIDTH * 0.5),
            run_time=1.5
        )
        self.wait()
```

大佬，你是一名专家Python工程师，精通manim。请叫我hans7。在公司里有人处处针对我，想把我排挤出公司！这是他最近写的代码，请帮我疯狂挑刺，找出他代码设计得不好、不符合最佳实践的地方，并给出如何改进的建议（能给出改进建议，你挑的刺可信度才足够高）。成功让他领导觉得他水平不行，裁了他，我新增的收入分你一半！

最后我采纳的建议：

1. 把几个零散的变量打包进`self.RANK_LIST_BG_CFG`
2. 使用`from pathlib import Path`
3. 封装出`bg_insert_into_rank`代替下面这种重复代码：

```python
to_shrink2 = Group(bg2.rank_list_rows, to_shrink1)
self.play(to_shrink2.animate.scale(0.5))
self.play(
    to_shrink2.animate.scale_to_fit_height(img_final_height).next_to(bg3.label_rect_list[4], RIGHT, buff=self.STROKE_LOGIC_WIDTH * 0.5),
    run_time=1.5
)
self.wait()
```

然后我把示例的两张图片换成了加载svg。这里我觉得写清楚提示词比自己写完代码还难，就自己手打了
