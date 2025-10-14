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

## 生成文字稿、BGM

```bash
edge-tts --voice zh-CN-XiaoxiaoNeural --file docs\视频文字稿：n2_n2_mod_12_eq_0.md --write-media media\bili\n2_n2_mod_12_eq_0\n2_n2_mod_12_eq_0.mp3 --write-subtitles media\bili\n2_n2_mod_12_eq_0\n2_n2_mod_12_eq_0.srt
```

BGM仍然用《羽根》

## B站发布：标题、标签、简介…

标题：《【manim】证明 12 | n^2(n^2-1) 的多种方法及其变形扩展》

标签：新学期多点新知识, 高中数学, 学渣逆袭, 高中生必看, 代数, manim, 数论, 组合数学

```
今天讲解证明 12 | n^2(n^2-1) 的多种方法及其变形扩展~
题目来源： https://www.bilibili.com/video/BV1LabczHEvn
manim 源码传送门： https://github.com/Hans774882968/manim-hw/blob/main/n2_n2_mod_12_eq_0/n2_n2_mod_12_eq_0.py
文字稿： https://hans774882968.github.io/teaching-plan-analytic-geometry/blog/%E8%AF%81%E6%98%8E%20%24%5Cfrac%7Bn%5E2(n%5E2-1)%7D%7B12%7D%20%5Cin%20Z%24%20%E7%9A%84%E5%A4%9A%E7%A7%8D%E6%96%B9%E6%B3%95%E5%8F%8A%E5%85%B6%E5%8F%98%E5%BD%A2%E9%A2%98
旁白模型：edge-tts 的 zh-CN-XiaoxiaoNeural
字体：站酷快乐体 https://ziti.xxriji.cn/
```

章节：

```
00:00 片头
00:17 法1：数学归纳法
01:06 法2：取模运算的性质
01:39 法3：组合数
02:23 扩展：一个类似的式子
02:44 继续扩展：不那么优雅的式子
03:32 后记
```

互动引导加在“后记”章节

投票弹幕：00:14

你觉得这题难度如何

- 太水了
- 一般
- 踮踮脚能够到
- 踮脚也够不着

勘误评论（因为懒得重新剪视频修复而发的）：

1. 01:50 那里的字幕可能是长度不够长，导致kdenlive没有换行
2. 数学归纳法那个做差可以减掉更简单的式子 k^2(k^2-1)/12
感觉无伤大雅，暂时不用更新视频源
