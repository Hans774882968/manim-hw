from manim import *
import os
import sys

sys.path.append(os.getcwd())

from manim_schema.json_driven_scene import JsonSceneFragment

scene_cfg = [
    {
        'title': '学习材料',
        'wait': 12,
        'blocks': [
            {
                'vgroups': [
                    {
                        'elements': [
                            {
                                'type': 'text',
                                'content': 'https://www.bilibili.com/opus/247191680174716386',
                                'font_size': 32
                            }
                        ],
                    }
                ]
            }
        ]
    },
    {
        'title': ['打靶练习怎么改造成那条', '浅薄与魔怔的视频'],
        'wait': 12,
        'blocks': [
            {
                'vgroups': [
                    {
                        'elements': [
                            '各个'
                        ],
                    }
                ]
            }
        ]
    },
]


class ShootHowTo(JsonSceneFragment):
    def show_title(self):
        title_group = Text("如何用manim做打靶视频", font_size=60, color=BLUE)
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
        self.wait(17)
        title_to_remove = VGroup(title_group, subtitle_group)
        return title_to_remove

    def construct(self):
        title_to_remove = self.show_title()
        self.my_setup(scene_cfg, title_to_remove)
        self.build()
