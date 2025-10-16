## 提示词

```markdown
大佬，你是一名数学科研工作者，精通manim。请叫我hans7。我有一道题：三角形中有 $\sin A+2\sin B=2\sin C$ ，求 $\frac{1}{\sin A}+\frac{1}{\sin B}-\frac{1}{\sin C}$ 最小值。我为这题写好了一篇正确的推理过程的文章，markdown格式。文章介绍了这道题的3种解法，我希望每种解法生成一个视频，第一种解法需要在开头展示题干，后两种解法直接开始展示解法即可。请完成以下需求：

1. 写manim代码展示这篇文章
2. 根据文章内容输出一篇旁白文章，作为视频的旁白。在保证视频旁白流畅的前提下，旁白内容应尽量忠于原文

要求：

1. 传入`MathTex`的字符串不能有中文，否则代码会报错
2. 讲解视频和旁白都使用中文
3. 旁白请以纯文本格式而非markdown格式输出，不要出现公式。可以用“这个公式”之类的词代替，观众看到视频画面能够明白旁白在说哪个公式

现在我先给你文章的引言和解法1的全文：
```

试了4次，每次效果都好差！我决定不让它自己创作旁白，而是只让它把我的博客里的公式翻译成中文，然后我手动修改

```markdown
大佬，你是一名数学科研工作者，精通manim。请叫我hans7。我有一道题：三角形中有 $\sin A+2\sin B=2\sin C$ ，求 $\frac{1}{\sin A}+\frac{1}{\sin B}-\frac{1}{\sin C}$ 最小值。我为这题写好了一篇正确的推理过程的文章，markdown格式。文章介绍了这道题的3种解法，我希望每种解法生成一个视频，第一种解法需要在开头展示题干，后两种解法直接开始展示解法即可。请完成以下需求：

1. 写manim代码展示这篇文章
2. 请把我文章的所有公式改写为中文读法。比如 a >= 1 改写为 a 大于等于1

要求：

1. 传入manim`MathTex`类的字符串不能有中文，否则代码会报错
2. 讲解视频和旁白都使用中文
3. 旁白请以纯文本格式而非markdown格式输出，不要出现公式。只需要将公式改写为中文读法，严禁修改我文章原文！

现在我先给你文章的引言和解法1的全文：
```

还是没遵循我的要求。可能是模型降智了。我丢进GLM里试试。额…GLM生成的也很烂。不过GLM生成了几何意义法的单位圆图像，还是有点参考价值的。

## 生成文字稿、BGM

```bash
edge-tts --voice zh-CN-XiaoxiaoNeural --file docs\视频文字稿：tri_sina_add_2sinb_eq_2sinc-主视频.md --write-media media\bili\tri_sina_add_2sinb_eq_2sinc\tri_sina_add_2sinb_eq_2sinc.mp3 --write-subtitles media\bili\tri_sina_add_2sinb_eq_2sinc\tri_sina_add_2sinb_eq_2sinc.srt

edge-tts --voice zh-CN-XiaoxiaoNeural --file docs\视频文字稿：tri_sina_add_2sinb_eq_2sinc-纯三角变换.md --write-media media\bili\tri_sina_add_2sinb_eq_2sinc\tri_2sinc_sol2.mp3 --write-subtitles media\bili\tri_sina_add_2sinb_eq_2sinc\tri_2sinc_sol2.srt

edge-tts --voice zh-CN-XiaoxiaoNeural --file docs\视频文字稿：tri_sina_add_2sinb_eq_2sinc-正弦定理+余弦定理.md --write-media media\bili\tri_sina_add_2sinb_eq_2sinc\tri_2sinc_sol1.mp3 --write-subtitles media\bili\tri_sina_add_2sinb_eq_2sinc\tri_2sinc_sol1.srt
```

顺便做个音频：

```bash
edge-tts --voice zh-CN-XiaoxiaoNeural --text "谢谢大佬们的三连加关注" --write-media D:\视频制作素材\三连+关注.mp3 --write-subtitles D:\视频制作素材\三连+关注.srt
```

BGM仍然用《羽根》

想要在“强注意力 → 打咩 ×”下面插入一个gif，但manim不支持。那就用kdenlive做了

## B站发布：标题、标签、简介…

标题：《一道颇难的解三角形题： sinA+2sinB=2sinC，求 min(1/sinA + 1/sinB - 1/sinC)》

标签：新学期多点新知识, 高中数学, 学渣逆袭, 高中生必看, 双曲线, manim, 解三角形, 三角恒等变换, 三角函数

```
今天我们来看这道颇难的解三角形题： sinA+2sinB=2sinC，求 min(1/sinA + 1/sinB - 1/sinC) 。这题至少有3种解法。个人体感，计算量：双曲线法 < 解三角形法 < 纯三角变换。对注意力的要求：双曲线法 < 解三角形法 < 纯三角变换。
题目来源： https://www.bilibili.com/video/BV12DJXzoEgK
那道更简单的题： https://zhidao.baidu.com/question/744659451359792932.html
manim 源码传送门：
- P1: https://github.com/Hans774882968/manim-hw/blob/main/tri_sina_add_2sinb_eq_2sinc/tri_sina_add_2sinb_eq_2sinc.py
- P2: https://github.com/Hans774882968/manim-hw/blob/main/tri_sina_add_2sinb_eq_2sinc/tri_2sinc_sol1.py
- P3: https://github.com/Hans774882968/manim-hw/blob/main/tri_sina_add_2sinb_eq_2sinc/tri_2sinc_sol2.py
文字稿： https://hans774882968.github.io/teaching-plan-analytic-geometry/blog/%E4%B8%89%E8%A7%92%E5%BD%A2%E4%B8%AD%E6%9C%89%20%24%5Csin%20A%2B2%5Csin%20B%3D2%5Csin%20C%24%20%EF%BC%8C%E6%B1%82%20%24%5Cfrac%7B1%7D%7B%5Csin%20A%7D%2B%5Cfrac%7B1%7D%7B%5Csin%20B%7D-%5Cfrac%7B1%7D%7B%5Csin%20C%7D%24%20%E6%9C%80%E5%B0%8F%E5%80%BC
旁白模型：edge-tts 的 zh-CN-XiaoxiaoNeural
字体：站酷快乐体 https://ziti.xxriji.cn/
```

章节（仅P1有，P2、P3无）：

```
00:00 片头
00:13 题干
00:42 思想
01:08 法3：双曲线
02:06 后记
```

3个P的互动引导都加在末尾

投票弹幕仅加在P1：00:18

你觉得这题难度如何

- 太水了
- 一般般
- 踮踮脚能够到
- 踮脚也够不着
