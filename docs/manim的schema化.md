## 初版提示词

```markdown
大佬，你是一名数学科研工作者，精通manim。请叫我hans7。我们不妨考虑用JSON来描述一个manim视频播放的全过程（不考虑展示图像等复杂情况，只考虑标题、文字和公式的展示）。一个视频由若干小节构成。每个小节都有一个标题，黄色、字体大小60，在该小节中标题一直居中展示在屏幕上方。每个的开头是上一个小节剩下的所有内容ReplacementTransform到当前小节的标题。展示完标题后，可以展示一系列公式和文字的组合，组合用VGroup包裹。一般的流程是从上往下堆叠了若干个VGroup，然后这些VGroup ReplacementTransform到下一个需要展示的VGroup，然后继续堆叠过程，直到再次发生多个VGroup ReplacementTransform到下一个需要展示的VGroup。对于一个VGroup，可以规定它其中元素的堆叠方向RIGHT、DOWN、以及靠左对齐aligned_edge=LEFT等。请帮我写出这样的JSON约定，并提供一份Python代码来解析符合这种约定的JSON
```

```markdown
大佬，content_groups应该扩展支持定义：第一组VGroup是从上往下堆叠，然后被第二组的第一个VGroup ReplacementTransform，然后继续堆叠第二组的其他VGroup，然后第二组的所有VGroup被第三组的第一个VGroup ReplacementTransform。循环往复
```

> 大佬，接下来请给我一个JSON字段的类型定义文件

> 大佬，请把这个schema.json文件的description翻译为中文

后来我还是改用TS描述了，因为它对人来说更友好。对LLM来说，我盲猜JSON和TS是差不多友好的，都是结构化数据

> 大佬，请你帮我写一个TypeScript语法的以上代码支持输入的数据结构的类型定义

## 支持Python字典透传诸多参数

```markdown
大佬，请帮我把下面的代码改成：把elem除了type和content外的所有属性透传给Text或MathTex类

很好，大佬。接下来请帮我把下面代码里的arrange方法改成从vg_data的arrange属性（一个字典）透传

for vg_data in block["vgroups"]:
    direction = DIRECTION_MAP[vg_data.get("direction", "DOWN")]
    aligned_edge = ALIGN_EDGE_MAP.get(vg_data.get("aligned_edge", "LEFT"), LEFT)
    # 省略代码
    vgroup = VGroup(*display_elements)
    vgroup.arrange(direction, aligned_edge=aligned_edge, buff=0.4)
    vgroups_in_block.append(vgroup)
```

## 新增递归能力

```markdown
大佬，现在我项目的代码`manim_schema\json_driven_scene.py`如下，它可以正常工作。接下来请你帮我在这份代码的基础上新增功能：支持vg_data的elements数组的每个元素传入现在这种（叶子），也支持继续传入vgroup（支持的属性和现有代码的一样）。这样就形成一个树状结构。

配套的可以工作的调用代码`henan_2610_t14\henan_2610_t14.py`：

代码执行的命令是：`uv run henan_2610_t14\henan_2610_t14.py`
```

## 试水：试着让LLM根据我的博客生成`henan_2610_t14`的代码

```markdown
大佬，你是一名数学科研工作者，精通manim。请叫我hans7。我有一段manim代码`manim_schema\json_driven_scene.py`，支持读取Python配置字典，生成manim视频。配置字典的类型定义文件`manim_schema\manim_json_schema.d.ts`在下面给出。我现在给你一篇博客，请你帮我补全我下面给你的`henan_2610_t14\henan_2610_t14.py`，把博客的“法2”到结尾部分转化为Python配置字典。

要求：

1. 和已有代码的风格保持一致。
2. 务必尊重原文！不要擅自修改原文的内容和公式！

`manim_schema\manim_json_schema.d.ts`：

你需要帮我补全的`henan_2610_t14\henan_2610_t14.py`：

博客“法2”之后的原文：

```

## Code Review

```markdown
大佬，我有一段manim代码，请你帮我进行code review，并给出修改后的代码。要求：
1. 代码符合DRY原则，重复逻辑抽象为函数、类等。
```

## 支持`Indicate, Circumscribe, SurroundingRectangle`等

新开GLM-4.6对话

大佬，你是一名数学科研工作者，精通manim。请叫我hans7。我有一段manim代码`manim_schema\json_driven_scene.py`，支持读取Python配置字典，生成manim视频。配置字典的类型定义文件`manim_schema\manim_json_schema.d.ts`在下面给出。

现在我希望：

1. 新增一个全局变量`vgroup_pool`。如果一个`vg_data`或`build_mobject_from_elem`方法中的`elem`参数提供了`id`属性，就把它加进`vgroup_pool`
2. 新增`Indicate, Circumscribe, SurroundingRectangle`的播放能力。`vg_data`新增`anime`属性，ts类型定义如下：

```ts
interface AnimationDescription {
  type: "indicate" | "circumscribe" | "surrounding_rectangle";
  target: string;
}

interface VGroupData extends NestedVGroupElement {
  wait?: number;
  anime?: AnimationDescription[];
}
```

`target`属性用于`vgroup_pool`的查询。其中`Indicate, Circumscribe`直接调用`self.play()`，`SurroundingRectangle`需要调用`self.play(Create)`以及`self.remove`。所以你需要对原有`play_animation_and_wait`方法的`self.play(Write(vg))`进行分类讨论。对于`SurroundingRectangle`，它需要在`page_wait_time`结束后再调用`self.remove`

要求：

1. 遵循最小改动原则，严禁修改与本次需求无关的代码
2. 动画的播放顺序要严格遵循Python字典中数组定义的顺序

`manim_schema\manim_json_schema.d.ts`：

`manim_schema\json_driven_scene.py`：

反馈：试了3次，输出的代码都有问题。鉴定为LLM没能力做这个需求。古法手作吧
