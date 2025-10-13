## 提示词

```markdown
大佬，你是一名数学科研工作者，精通manim。请叫我hans7。我有一道证明题：证明对于任意自然数n，都有 $n^2(n^2-1) \mod 12 = 0$ 。我为这题写好了一篇正确的文章，markdown格式。请你帮我写一段manim代码，展示这篇文章。我已经写好了一部分代码，请你帮我在其基础上继续修改。代码的方法1已经完成，方法2还未完成。

文章全文如下：

代码如下：

要求：

1. 传入`MathTex`的字符串不能有中文，否则代码会报错。如果句子里有中文，请使用`Text`
2. 讲解视频使用中文
```

这次是扔给GLM-4.6的，这个模型牛皮吹得震天响，但是生成的效果很烂（`useless\n2_n2_mod_12_eq_0_glm.py`）。我甚至觉得没什么修改的价值。可能现在国内的模型都没有能力输出高质量的manim代码。还是参考AI生成的代码，古法手搓了

生成文字稿：

```bash
edge-tts --voice zh-CN-XiaoxiaoNeural --file docs\视频文字稿：n2_n2_mod_12_eq_0.md --write-media media\bili\n2_n2_mod_12_eq_0\n2_n2_mod_12_eq_0.mp3 --write-subtitles media\bili\n2_n2_mod_12_eq_0\n2_n2_mod_12_eq_0.srt
```
