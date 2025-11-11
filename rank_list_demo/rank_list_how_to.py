from manim import *
import os
import sys

sys.path.append(os.getcwd())

from m_objects.moving_watermark import MovingWatermark
from manim_schema.json_driven_scene import JsonSceneFragment

code_common_config = {
    'type': 'code',
    'language': 'python',
    'formatter_style': 'github-dark',
    'background': 'window',
    'background_config': {'stroke_color': 'maroon'},
    'paragraph_config': {'font_size': 20},
}

scene_cfg = [
    {
        'title': '学习材料',
        'wait': 20,
        'blocks': [
            {
                'vgroups': [
                    {
                        'arrange': {'aligned_edge': 'left'},
                        'elements': [
                            {
                                'type': 'paragraph',
                                'line_spacing': 0.7,
                                'content': [
                                    '1. 上期 manim 教学视频： https://www.bilibili.com/video/BV1GY2cBkEUo/',
                                    '2. 推荐入门教程（老）： https://www.bilibili.com/opus/247191680174716386'
                                ],
                                'font_size': 24,
                                'color': 'BLUE',
                                't2c': {
                                    '1. 上期 manim 教学视频：': 'WHITE',
                                    '2. 推荐入门教程（老）：': 'WHITE',
                                }
                            },
                        ],
                    }
                ]
            }
        ]
    },
    {
        'title': '视频制作的主要步骤',
        'wait': 20,
        'blocks': [
            {
                'vgroups': [
                    {
                        'arrange': {'aligned_edge': 'left'},
                        'elements': [
                            {
                                'type': 'paragraph',
                                'line_spacing': 0.7,
                                'content': [
                                    '1. 画出从夯到拉的背景图',
                                    '2. 展示初始素材图片，并设置成合适的大小',
                                    '3. 让素材图片一边缩小到和一行矩形的高度相同，一边移动到正确位置',
                                ],
                                'font_size': 28,
                            },
                        ],
                    }
                ]
            }
        ]
    },
    {
        'title': '画从夯到拉的背景图',
        'blocks': [
            {
                'wait': 20,
                'vgroups': [
                    {
                        'arrange': {'aligned_edge': 'left'},
                        'elements': [
                            {
                                'type': 'text',
                                'content': '背景图参考网站： https://conghangdaola.com/',
                                'font_size': 32,
                                'color': 'BLUE',
                                't2c': {
                                    '背景图参考网站：': 'WHITE',
                                }
                            },
                            {
                                'type': 'paragraph',
                                'line_spacing': 0.7,
                                'content': [
                                    '提示词：',
                                    '大佬，你是一名数学科研工作者，精通manim。请叫我hans7。',
                                    '请帮我写一段manim代码，画出图片里的效果。'
                                ],
                                'font_size': 32,
                            }
                        ],
                    }
                ]
            },
            {
                'wait': 20,
                'vgroups': [
                    {
                        'elements': [
                            {
                                **code_common_config,
                                'paragraph_config': {'font_size': 16},
                                'content': '''
STROKE_WIDTH = 2
STROKE_LOGIC_WIDTH = STROKE_WIDTH / config.pixel_width * config.frame_width
STROKE_LOGIC_HEIGHT = STROKE_WIDTH / config.pixel_height * config.frame_height
label_width = config.frame_width * 0.2 - STROKE_LOGIC_WIDTH
content_rect_width = config.frame_width - label_width - STROKE_LOGIC_WIDTH
row_height = (total_height - STROKE_LOGIC_HEIGHT) / row_count
for i in range(row_count):
    label_rect = Rectangle(
        width=label_width, height=row_height, fill_color=colors[i],
        fill_opacity=1, stroke_color=WHITE, stroke_width=STROKE_WIDTH
    )
    label_text = Text(rank_labels[i], font_size=60, weight=ULTRABOLD, color=BLACK)
    label_text.move_to(label_rect.get_center())
    content_rect = Rectangle(
        width=content_rect_width, height=row_height, fill_color="#1a1a17",
        fill_opacity=1, stroke_color=WHITE, stroke_width=STROKE_WIDTH
    )
    content_rect.next_to(label_rect, RIGHT, buff=0)
    row = VGroup(label_rect, label_text, content_rect)
    rank_list_rows.add(row)
'''
                            },
                        ]
                    }
                ]
            },
        ]
    },
    {
        'title': '从夯到拉背景图 - 边框宽度问题',  # 为了解决报错而拆分 It looks like the scene contains a lot of sub-mobjects
        'blocks': [
            {
                'wait': 20,
                'vgroups': [
                    {
                        'arrange': {'aligned_edge': 'left'},
                        'elements': [
                            {
                                **code_common_config,
                                'paragraph_config': {'font_size': 14},
                                'content': '''
STROKE_WIDTH = 2
STROKE_LOGIC_WIDTH = STROKE_WIDTH / config.pixel_width * config.frame_width
STROKE_LOGIC_HEIGHT = STROKE_WIDTH / config.pixel_height * config.frame_height
label_width = config.frame_width * 0.2 - STROKE_LOGIC_WIDTH
content_rect_width = config.frame_width - label_width - STROKE_LOGIC_WIDTH
row_height = (total_height - STROKE_LOGIC_HEIGHT) / row_count
'''
                            },
                            {
                                'type': 'paragraph',
                                'line_spacing': 0.7,
                                'font_size': 22,
                                'content': [
                                    '1. 60px字体配0.2倍屏幕宽刚好合适，如果太大，一行矩形都会发生错位',
                                    '2. 边框宽度不包含在矩形宽度里，所以如果让左右矩形宽度和等于屏幕宽度',
                                    '   就会导致左矩形左边框和右矩形右边框只能显示一半',
                                    '3. 边框宽度的单位是像素，所以需要转换成逻辑宽度',
                                ]
                            },
                            {
                                'type': 'math_tex',
                                'font_size': 36,
                                'content': r'\frac{STROKE\_LOGIC\_WIDTH}{config.frame\_width} = \frac{STROKE\_WIDTH}{config.pixel\_width}',
                                'color': 'BLUE'
                            }
                        ]
                    }
                ]
            },
        ]
    },
    {
        'title': '素材图片的展示和移动',
        'blocks': [
            {
                'vgroups': [
                    {
                        'arrange': {'aligned_edge': 'left'},
                        'wait': 20,
                        'elements': [
                            {
                                **code_common_config,
                                'content': r'''
img_initial_height = 2 * row_height
img_final_height = row_height - 0.5 * STROKE_LOGIC_HEIGHT
img2 = ImageMobject(r"assets\rank_list_demo\服务员.jpg")
img2.scale_to_fit_height(img_initial_height)
self.play(FadeIn(img2))
'''
                            },
                            {
                                'type': 'paragraph',
                                'line_spacing': 0.7,
                                'font_size': 24,
                                'content': [
                                    '图片路径不踩坑：相对于项目根目录的相对路径',
                                    r'注：假设在项目根目录运行命令 uv run manim -pql foo\rank_list_demo.py',
                                ]
                            },
                            {
                                'type': 'paragraph',
                                'line_spacing': 0.7,
                                'font_size': 24,
                                'content': [
                                    'mobject.scale_to_fit_height(height, **kwargs) ：',
                                    'Scales the Mobject to fit a height while keeping width/depth proportional',
                                ]
                            }
                        ],
                    }
                ]
            },
            {
                'vgroups': [
                    {
                        'arrange': {'aligned_edge': 'left'},
                        'wait': 20,
                        'elements': [
                            {
                                **code_common_config,
                                'paragraph_config': {'font_size': 14},
                                'content': '''
self.wait(11.451)
self.play(
    img2.animate.scale_to_fit_height(img_final_height)
        .next_to(label_rect_list[3], RIGHT, buff=STROKE_LOGIC_WIDTH * 0.5),
    run_time=4.191
)
self.wait(9.810)
'''
                            },
                            {
                                **code_common_config,
                                'paragraph_config': {'font_size': 14},
                                'content': '''
self.play(
    img4.animate.scale_to_fit_height(img_final_height).next_to(img2, RIGHT, buff=0),
    run_time=1.5
)
'''
                            },
                            {
                                'type': 'text',
                                'font_size': 24,
                                'content': '代码优化建议：每行维护一个数组，当前元素要紧挨着数组最后一个元素',
                            }
                        ],
                    }
                ]
            },
        ]
    },
]


class RankListHowTo(JsonSceneFragment):
    def add_watermark(self):
        watermark = MovingWatermark("Hans码数理哲", font_size=20, color="#a1a1a1", z_index=114)
        watermark.add_updater(watermark.update_position)
        self.add(watermark)

    def show_title(self):
        title_group = Text("用manim做从夯到拉锐评视频", font_size=60, color=BLUE)
        subtitle_arr = [
            MarkupText("作者：<span foreground=\"#58C4DD\">hans7</span>", font_size=24),
            Text("我们必须想象，做题人是幸福的", font_size=24, color=BLUE),
            Text("源码传送门：见视频简介", font_size=24, color=YELLOW),
        ]
        subtitle_group = VGroup(*subtitle_arr).arrange(DOWN, buff=0.2)
        subtitle_group.next_to(title_group, DOWN, buff=0.5)

        title_whole = VGroup(title_group, subtitle_group)
        title_whole.move_to(ORIGIN)

        self.play(Write(title_group), run_time=1)
        self.play(FadeIn(subtitle_group, shift=DOWN))
        self.play(Circumscribe(subtitle_arr[1], run_time=4, color=BLUE))
        self.wait(10)
        title_to_remove = VGroup(title_group, subtitle_group)
        return title_to_remove

    def construct(self):
        self.add_watermark()
        title_to_remove = self.show_title()
        self.my_setup(scene_cfg, title_to_remove)
        self.build()
        self.show_ending(self.section_to_remove, 18)
