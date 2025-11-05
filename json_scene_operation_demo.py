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
                        'operations': lambda m: m.arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT, buff=0.5),
                        'elements': [
                            '推荐博客：',
                            {
                                'type': 'text',
                                'content': '博客1',
                                'operations': lambda m: m.set_color(PINK)
                            }
                        ]
                    }
                ]
            }
        ]
    }
]


class JsonSceneOperationDemo(JsonSceneFragment):
    def construct(self):
        self.my_setup(scene_cfg)
        self.build()
