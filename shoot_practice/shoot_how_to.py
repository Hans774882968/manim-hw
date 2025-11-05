from manim import *
import os
import sys

sys.path.append(os.getcwd())

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
        'wait': 12,
        'blocks': [
            {
                'vgroups': [
                    {
                        'arrange': {'aligned_edge': 'left'},
                        'elements': [
                            '推荐博客：',
                            {
                                'type': 'paragraph',
                                'line_spacing': 0.7,
                                'content': [
                                    '1. 入门教程（老）： https://www.bilibili.com/opus/247191680174716386',
                                    '2. manim 边做边学： https://www.cnblogs.com/wang_yb/p/18674709',
                                    '3. animate 属性： https://juejin.cn/post/7507564752434806821',
                                ],
                                'font_size': 28,
                                'color': 'BLUE',
                                't2c': {
                                    '1. 入门教程（老）：': 'WHITE',
                                    '2. manim 边做边学：': 'WHITE',
                                    '3. animate 属性：': 'WHITE',
                                }
                            },
                        ],
                    }
                ]
            }
        ]
    },
    {
        'title': '绘制图形',
        'blocks': [
            {
                'vgroups': [
                    {
                        'wait': 5,
                        'elements': [
                            {
                                'arrange': {'aligned_edge': 'left'},
                                'elements': [
                                    {
                                        **code_common_config,
                                        'content': '''
Circle(radius=0.8, color=BLUE) # 绘制空心圆
Circle(radius=0.1, color=RED, fill_color=RED, fill_opacity=1) # 实心圆
'''
                                    },
                                    {
                                        **code_common_config,
                                        'paragraph_config': {'font_size': 16},
                                        'content': '''
Line(start=LEFT, end=RIGHT, color=RED) # 绘制线段
LEFT, RIGHT = np.array((-1, 0.0, 0)), np.array((1, 0, 0.0)) # manim 提供的向量举例
Point3DLike: TypeAlias = Union[Point3D, tuple[float, float, float]]
Point3D: TypeAlias = npt.NDArray[PointDType]
Vector3D: TypeAlias = npt.NDArray[PointDType]
'''
                                    },
                                    {
                                        **code_common_config,
                                        'content': '''
aim_scope = VGroup(outer_circle, inner_circle, ...) # 打包多个图形
self.play(FadeIn(aim_scope)) # VGroup 动画
'''
                                    }
                                ]
                            }
                        ],
                    }
                ]
            }
        ]
    },
    {
        'title': '移动图形',
        'blocks': [
            {
                'vgroups': [
                    {
                        'wait': 5,
                        'elements': [
                            {
                                **code_common_config,
                                'content': '''
aim_scope.shift(LEFT * 1.14 + UP * 5.14) # 向左上角移动

dot_p.move_to(np.array([x, y, 0])) # 移到指定坐标

aim_scope.next_to(target, ORIGIN) # 移到target的中心
aim_scope.next_to(target, LEFT) # 移到target的左边

Text("虚无刻度").to_edge(UP) # 移到屏幕上方中心
'''
                            },
                        ]
                    }
                ]
            }
        ]
    },
    {
        'title': '图形的过渡动画',
        'blocks': [
            {
                'vgroups': [
                    {
                        'arrange': {'aligned_edge': 'left'},
                        'wait': 5,
                        'elements': [
                            {
                                **code_common_config,
                                'content': '''
# 过渡动画的两种创建方式
ApplyMethod(goal.set_fill, new_color)
gp.animate.scale(0.01).set_color(BLACK)
'''
                            },
                            {
                                **code_common_config,
                                'content': '''
# 多个动画同时进行
self.play(
    ApplyMethod(goal.set_fill, new_color),
    ReplacementTransform(score, new_score)
)
'''
                            },
                        ]
                    }
                ]
            }
        ]
    },
    {
        'title': '这两种方法有区别吗？',
        'blocks': [
            {
                'vgroups': [
                    {
                        'arrange': {'aligned_edge': 'left'},
                        'wait': 5,
                        'elements': [
                            {
                                'type': 'paragraph',
                                'line_spacing': 0.7,
                                'content': [
                                    'kimi k2：有区别',
                                    'Qwen3-Max、GLM-4.6：没区别',
                                    '目前个人认为：',
                                    'ApplyMethod 更老， .animate 支持链式调用，更简洁',
                                ],
                                't2c': {
                                    'kimi k2': 'RED',
                                    'Qwen3-Max': 'GREEN',
                                    'GLM-4.6': 'GREEN',
                                }
                            },
                            {
                                **code_common_config,
                                'content': '''
ApplyMethod(target.shift, random_pos)
target.animate.shift(random_pos) # √ 更推荐
'''
                            },
                        ]
                    }
                ]
            }
        ]
    },
    {
        'title': '画瞄准镜、靶子',
        'blocks': [
            {
                'vgroups': [
                    {
                        'arrange': {'aligned_edge': 'left'},
                        'wait': 5,
                        'elements': [
                            {
                                **code_common_config,
                                'paragraph_config': {'font_size': 14},
                                'content': '''
outer_circle = Circle(radius=0.8, color=BLUE)
inner_circle = Circle(radius=0.1, color=RED, fill_color=RED, fill_opacity=1)
line_vertical = Line(start=outer_circle.get_bottom(), end=outer_circle.get_top(), color=RED)
line_horizontal = Line(start=outer_circle.get_left(), end=outer_circle.get_right(), color=RED)
aim_scope = VGroup(outer_circle, inner_circle, line_vertical, line_horizontal)
self.play(FadeIn(aim_scope))
'''
                            },
                            {
                                **code_common_config,
                                'paragraph_config': {'font_size': 16},
                                'content': '''
for i in range(r): for j in range(c): # r=3, c=4, 间距2
    target = Circle(radius=0.4, color=GRAY, fill_color=GRAY, fill_opacity=0.4)
    target.shift((-3 + 2 * j) * RIGHT + (-2 + 2 * i) * DOWN)
    label = Text(target_labels[idx], font_size=24, color=GRAY)
    label.next_to(target, DOWN, buff=0.1)
    self.play(FadeIn(target), FadeIn(label))
'''
                            },
                            {
                                'type': 'math_tex',
                                'content': r'k+2(x-1)=-k \Rightarrow k = 1-x \text{ then let x = r, c}'
                            }
                        ],
                    }
                ]
            }
        ]
    },
    {
        'title': '显示分数、模拟射击',
        'blocks': [
            {
                'vgroups': [
                    {
                        'arrange': {'aligned_edge': 'left'},
                        'wait': 5,
                        'elements': [
                            {
                                **code_common_config,
                                'paragraph_config': {'font_size': 16},
                                'content': '''
nihilism_score_text = Text("虚无刻度：", font_size=36)
nihilism_score_text.to_edge(UP)
nihilism_score = Integer(0).next_to(nihilism_score_text, RIGHT)
self.play(FadeIn(nihilism_score_text), FadeIn(nihilism_score))
'''
                            },
                            {
                                **code_common_config,
                                'paragraph_config': {'font_size': 16},
                                'content': '''
# 移到靶子中心
goal = targets[r][c]
self.play(ApplyMethod(aim_scope.next_to, goal, ORIGIN))
# 靶子、文本颜色变化，分数增加
self.play(
    ApplyMethod(goal.set_fill, new_color),
    ApplyMethod(goal.set_color, new_color),
    ApplyMethod(label.set_color, new_color),
    ReplacementTransform(nihilism_score, new_nihilism_score)
)
'''
                            }
                        ],
                    }
                ]
            }
        ]
    },
    {
        'title': '模拟尼采精神崩溃的效果',
        'blocks': [
            {
                'vgroups': [
                    {
                        'wait': 12,
                        'elements': [
                            {
                                'type': 'paragraph',
                                'line_spacing': 0.7,
                                'content': [
                                    '问LLM要代码 → 手动微调',
                                    '流程：',
                                    '1. 打乱每个靶子的位置',
                                    '2. 弄乱屏幕里所有图形',
                                    '3. 图形向中心消失，展示尼采的名言'
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                'vgroups': [
                    {
                        'wait': 10,
                        'elements': [
                            {
                                **code_common_config,
                                'paragraph_config': {'font_size': 14},
                                'content': '''
aim_scope_shift_direction = LEFT * 3 + DOWN * 2
self.play(
    all_targets.animate.set_color(RED_E).scale(1.2),
    all_labels.animate.set_color(RED).scale(1.2),
    nihilism_score.animate.set_value(114514).set_color(RED),
    ApplyMethod(aim_scope.shift, aim_scope_shift_direction),
    ApplyMethod(aim_scope[2].shift, aim_scope_shift_direction + UP * 0.3 + 0.1 * RIGHT),  # 十字线错位
    ApplyMethod(aim_scope[3].shift, aim_scope_shift_direction + LEFT * 0.3 + 0.1 * UP),
    run_time=0.8
)

self.play(collapse_gp.animate.scale(0.01).set_color(BLACK), run_time=0.3)

final_quote_line1 = Text("Ich bin kein Mensch, ich bin Dynamit.", font_size=36, color=RED)
final_quote_line2 = Text("我不是人，我是炸药！", font_size=36, color=RED)
final_quote_line3 = Text("——尼采", font_size=30)
quote_group = VGroup(final_quote_line1, final_quote_line2).arrange(DOWN, aligned_edge=ORIGIN)
final_quote_line3.next_to(quote_group, DOWN, aligned_edge=RIGHT)
self.play(FadeIn(final_quote_line1), FadeIn(final_quote_line2), FadeIn(final_quote_line3))
'''
                            }
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
        self.show_ending(self.section_to_remove, 16)
