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
