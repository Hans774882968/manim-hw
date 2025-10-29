import os
import sys

sys.path.append(os.getcwd())  # 解决 import 报错 ModuleNotFoundError: No module named 'manim_schema'

from manim_schema.json_driven_scene import main

scene_cfg = {
    'output_file': 'henan_2610_t14',
    'title': [
        '2026河南新未来高三',
        '10月联合测评T14'
    ],
    'sections': [
        {
            'title': '题干',
            'wait': 10,
            'blocks': [
                {
                    'vgroups': [
                        {
                            'elements': [
                                {
                                    'arrange': {'aligned_edge': 'left'},
                                    'elements': [
                                        '三角形ABC中有 ',
                                        {
                                            'type': 'math_tex',
                                            'content': r'\frac{\cos B}{\cos A}=\frac{1+\sin B}{1+\sin A}',
                                            'color': 'BLUE'
                                        }
                                    ]
                                },
                                {
                                    'arrange': {'direction': 'right'},
                                    'elements': [
                                        '求',
                                        {
                                            'type': 'math_tex',
                                            'content': r'\sin A+\cos B+\sin C'
                                        },
                                        '的取值范围'
                                    ]
                                }
                            ]
                        }
                    ]
                },
            ]
        },
        {
            'title': '碎碎念',
            'wait': 10,
            'blocks': [
                {
                    'vgroups': [
                        {
                            'elements': [
                                {
                                    'type': 'text',
                                    'content': '强注意力 → 打咩 ×',
                                    'color': 'RED',
                                    'font_size': 48
                                },
                                {
                                    'type': 'text',
                                    'content': '水到渠成 → 我要 √',
                                    'color': 'GREEN',
                                    'font_size': 48
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            'title': [
                '如何化简约束方程',
                '法1：万能公式（不需要注意力）'
            ],
            'subtitle_mode': True,
            'wait': 10,
            'blocks': [
                {
                    'wait': 5,
                    'vgroups': [
                        {
                            'arrange': {'aligned_edge': 'left'},
                            'elements': [
                                {
                                    'arrange': {'direction': 'right'},
                                    'elements': [
                                        '设',
                                        {
                                            'type': 'math_tex',
                                            'content': r'u=\tan \frac{B}{2} > 0,\ v=\tan \frac{A}{2} > 0'
                                        }
                                    ]
                                },
                                {
                                    'arrange': {'direction': 'right'},
                                    'elements': [
                                        '则',
                                        {
                                            'type': 'math_tex',
                                            'content': r'\cos B = \frac{1-u^2}{1+u^2},\ \cos A = \frac{1-v^2}{1+v^2}'
                                        }
                                    ]
                                },
                                {
                                    'arrange': {'aligned_edge': 'left'},
                                    'elements': [
                                        {
                                            'type': 'markup_text',
                                            'content': '则<span foreground=\"#58C4DD\">约束方程</span>',
                                        },
                                        {
                                            'type': 'math_tex',
                                            'content': r'\frac{1-u^2}{1-v^2}=\frac{u^2-1}{v^2-1}=\frac{u^2+1+2u}{v^2+1+2v}=\frac{(u+1)^2}{(v+1)^2}'
                                        }
                                    ]
                                },
                            ]
                        },
                    ]
                },
                {
                    'wait': 5,
                    'vgroups': [
                        {
                            'arrange': {'direction': 'right'},
                            'elements': [
                                {
                                    'type': 'math_tex',
                                    'content': r'\Rightarrow (u+1)^2(v^2-1) &= (u+1)^2(v+1)(v-1)\\ &= (v+1)^2(u+1)(u-1)'
                                },
                            ]
                        },
                        {
                            'wait': 5,
                            'arrange': {'direction': 'right'},
                            'elements': [
                                '因为',
                                {
                                    'type': 'math_tex',
                                    'content': r'u+1>1,\ v+1>1'
                                },
                                '所以可以消掉它们'
                            ]
                        },
                        {
                            'elements': [
                                {
                                    'type': 'math_tex',
                                    'content': r'(u+1)(v-1)=(v+1)(u-1)'
                                },
                                {
                                    'type': 'math_tex',
                                    'content': r'\Rightarrow uv-u+v-1=uv-v+u-1=0 \Rightarrow u=v'
                                }
                            ]
                        }
                    ]
                },
                {
                    'vgroups': [
                        {
                            'elements': [
                                '所以',
                                {
                                    'type': 'math_tex',
                                    'content': r'u=\tan \frac{B}{2}=v=\tan \frac{A}{2} \Rightarrow A=B'
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            'title': [
                '如何化简约束方程',
                '法2：纯三角变换（不需要注意力）'
            ],
            'subtitle_mode': True,
            'wait': 10,
            'blocks': [
                {
                    'vgroups': [
                        {
                            'wait': 5,
                            'arrange': {'aligned_edge': 'left'},
                            'elements': [
                                {
                                    'type': 'math_tex',
                                    'content': r'\cos B(1+\sin A)=\cos B+\sin A\cos B'
                                },
                                {
                                    'type': 'math_tex',
                                    'content': r'=\cos A+\sin B\cos A \Rightarrow \sin (A-B)=\cos A-\cos B'
                                }
                            ]
                        },
                        {
                            'wait': 5,
                            'arrange': {'aligned_edge': 'left'},
                            'elements': [
                                '和差化积：',
                                {
                                    'type': 'math_tex',
                                    'content': r'\cos A-\cos B=-2\sin \frac{A+B}{2}\sin \frac{A-B}{2}'
                                }
                            ]
                        },
                    ]
                },
                {
                    'wait': 5,
                    'vgroups': [
                        {
                            'arrange': {'aligned_edge': 'left'},
                            'elements': [
                                '二倍角公式：',
                                {
                                    'type': 'math_tex',
                                    'content': r'-2\sin \frac{A+B}{2}\sin \frac{A-B}{2}=2\sin \frac{A-B}{2}\cos \frac{A-B}{2}'
                                },
                                {
                                    'type': 'math_tex',
                                    'content': r'\sin \frac{A-B}{2}(\sin \frac{A+B}{2}+\cos \frac{A-B}{2})=0',
                                    'substrings_to_isolate': (r'\sin \frac{A-B}{2}',),
                                    'set_color_by_tex': (r'\sin \frac{A-B}{2}', 'BLUE')
                                }
                            ]
                        },
                    ]
                },
                {
                    'wait': 5,
                    'vgroups': [
                        {
                            'arrange': {'aligned_edge': 'left'},
                            'elements': [
                                '把sin化为cos，再用一次和差化积：',
                                {
                                    'type': 'math_tex',
                                    'content': r'\sin \frac{A+B}{2}+\cos \frac{A-B}{2}=\cos \frac{C}{2}+\cos \frac{A-B}{2}'
                                },
                                {
                                    'type': 'math_tex',
                                    'content': r'=2\cos \frac{C+A-B}{2}\cos \frac{C+B-A}{2}=2\sin B\sin A'
                                },
                            ]
                        }
                    ]
                },
                {
                    'vgroups': [
                        {
                            'arrange': {'direction': 'right'},
                            'elements': [
                                '因为',
                                {
                                    'type': 'math_tex',
                                    'content': r'\sin A'
                                },
                                '和',
                                {
                                    'type': 'math_tex',
                                    'content': r'\sin B'
                                },
                                '都不为0，所以只能是',
                            ]
                        },
                        {
                            'elements': [
                                {
                                    'type': 'math_tex',
                                    'content': r'\sin \frac{A-B}{2}=0 \Rightarrow A=B'
                                }
                            ]
                        },
                    ]
                }
            ]
        },
        {
            'title': [
                '如何化简约束方程',
                '法3：数形结合（需要注意力）'
            ],
            'subtitle_mode': True,
            'wait': 10,
            'blocks': [
                {
                    'wait': 5,
                    'vgroups': [
                        {
                            'arrange': {'aligned_edge': 'left'},
                            'elements': [
                                '简单变形：',
                                {
                                    'type': 'math_tex',
                                    'content': r'\frac{\sin A-(-1)}{\cos A}=\frac{\sin B-(-1)}{\cos B}'
                                }
                            ]
                        },
                        {
                            'arrange': {'direction': 'right'},
                            'elements': [
                                '设',
                                {
                                    'type': 'math_tex',
                                    'content': r'B=\frac{\pi}{2}'
                                },
                                '则容易推出',
                                {
                                    'type': 'math_tex',
                                    'content': r'A=\frac{\pi}{2}'
                                },
                            ]
                        },
                        {
                            'arrange': {'direction': 'right'},
                            'elements': [
                                '矛盾，所以可以放心把',
                                {
                                    'type': 'math_tex',
                                    'content': r'\cos B',
                                    'color': 'blue'
                                },
                                '放到分母'
                            ]
                        },
                    ]
                },
                {
                    'vgroups': [
                        {
                            'elements': [
                                '这表示上半圆的两点到',
                                {
                                    'type': 'math_tex',
                                    'content': r'(0,\ -1)'
                                },
                                '连线的斜率相等，所以',
                                {
                                    'type': 'math_tex',
                                    'content': r'A=B'
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            'title': [
                '如何化简约束方程',
                '法4：用二倍角公式拆开（需要注意力）'
            ],
            'subtitle_mode': True,
            'wait': 10,
            'blocks': [
                {
                    'wait': 5,
                    'vgroups': [
                        {
                            'arrange': {'direction': 'right'},
                            'elements': [
                                '左边：',
                                {
                                    'type': 'math_tex',
                                    'content': r'\frac{\cos^2\frac{B}{2}-\sin^2\frac{B}{2}}{\cos^2\frac{A}{2}-\sin^2\frac{A}{2}}'
                                }
                            ]
                        },
                        {
                            'wait': 5,
                            'arrange': {'aligned_edge': 'left'},
                            'elements': [
                                '右边：',
                                {
                                    'type': 'math_tex',
                                    'content': r'\frac{1+\sin B}{1+\sin A}=\frac{\sin^2\frac{B}{2}+\cos^2\frac{B}{2}+2\sin \frac{B}{2}\cos \frac{B}{2}}{1+\sin A}',
                                    'font_size': 28
                                },
                                {
                                    'type': 'math_tex',
                                    'content': r'=\frac{(\sin \frac{B}{2}+\cos \frac{B}{2})^2}{(\sin \frac{A}{2}+\cos \frac{A}{2})^2}',
                                    'font_size': 28
                                }
                            ]
                        }
                    ]
                },
                {
                    'vgroups': [
                        {
                            'arrange': {'direction': 'right'},
                            'elements': [
                                '把两边的加法消掉：',
                                {
                                    'type': 'math_tex',
                                    'content': r'\frac{\cos \frac{B}{2}-\sin \frac{B}{2}}{\cos \frac{A}{2}-\sin \frac{A}{2}}=\frac{\cos \frac{B}{2}+\sin \frac{B}{2}}{\cos \frac{A}{2}+\sin \frac{A}{2}}'
                                }
                            ]
                        },
                        {
                            'elements': [
                                '交叉相乘，然后展开得：',
                                {
                                    'type': 'math_tex',
                                    'content': r'\sin \frac{B}{2}\cos \frac{A}{2}-\cos \frac{B}{2}\sin \frac{A}{2}=\sin \frac{B-A}{2}=0'
                                }
                            ]
                        },
                        {
                            'arrange': {'direction': 'right'},
                            'elements': [
                                '同样得到',
                                {
                                    'type': 'math_tex',
                                    'content': r'A=B'
                                }
                            ]
                        }
                    ]
                },
            ]
        },
        {
            'title': '题解收尾',
            'wait': 10,
            'blocks': [
                {
                    'wait': 5,
                    'vgroups': [
                        {
                            'arrange': {'aligned_edge': 'left'},
                            'elements': [
                                '剩下的就是常规问题了：',
                                {
                                    'type': 'math_tex',
                                    'content': r'f &= \sin A+\cos B+\sin C\\ &= \sin A+\cos A+\sin 2A\\ &= (\sin A+\cos A)+(1+2\sin A\cos A)-1\\ &= (\sin A+\cos A)+(\sin A+\cos A)^2-1',
                                    'substrings_to_isolate': (r'\sin A+\cos A',),
                                    'set_color_by_tex': (r'\sin A+\cos A', 'BLUE'),
                                },
                            ]
                        }
                    ]
                },
                {
                    'vgroups': [
                        {
                            'arrange': {'direction': 'right'},
                            'elements': [
                                '令',
                                {
                                    'type': 'math_tex',
                                    'content': r't=\sin A+\cos A=\sqrt{2}\sin\left(A+\frac{\pi}{4}\right)'
                                }
                            ]
                        },
                        {
                            'arrange': {'direction': 'right'},
                            'elements': [
                                '因为',
                                {
                                    'type': 'math_tex',
                                    'content': r'0 < A=B < \frac{\pi}{2}'
                                },
                                '所以',
                                {
                                    'type': 'math_tex',
                                    'content': r't \in (1,\sqrt{2}]'
                                }
                            ]
                        },
                        {
                            'arrange': {'direction': 'right'},
                            'elements': [
                                '所以',
                                {
                                    'type': 'math_tex',
                                    'content': r'f=t^2+t-1'
                                },
                                '在',
                                {
                                    'type': 'math_tex',
                                    'content': r't=1,\ \sqrt{2}',
                                    'color': 'BLUE'
                                },
                            ]
                        },
                        {
                            'arrange': {'direction': 'right'},
                            'elements': [
                                '处分别取得最小、最大值，所求为',
                                {
                                    'type': 'math_tex',
                                    'content': r'(1,\ \sqrt{2}+1]',
                                    'color': 'BLUE'
                                }
                            ]
                        },
                    ]
                },
            ]
        }
    ]
}
main(scene_cfg)
