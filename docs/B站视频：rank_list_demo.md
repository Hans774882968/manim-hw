## 功能开发提示词

给通义千问网页端的提示词：

大佬，你是一名数学科研工作者，精通manim。请叫我hans7。请帮我写一段manim代码，画出图片里的效果

图片来源：在 https://conghangdaola.com/ 截图

大佬，接下来请帮我修改下面的manim代码，实现：FadeIn一张图片`assets\rank_list_demo\谁会React Fiber.jpg`，它的初始宽度和高度都设置为1.2倍`content_rect`一行的高度，初始位置在屏幕中心。等待20秒后，让它移向“夯”那行的`content_rect`的第一个位置，并且在移动的同时，让动画和宽度、高度缩小为与`content_rect`一行的高度一致。接下来FadeIn第二张图片`assets\rank_list_demo\服务员.jpg`，后续过程都和第一张图片类似，但它最后要移向“夯”那行的`content_rect`的第二个位置

## 旁白

```bash
edge-tts --voice zh-CN-XiaoxiaoNeural --file docs\视频文字稿：rank_list_demo.md --write-media media\bili\rank_list_demo\rank_list_demo.mp3 --write-subtitles media\bili\rank_list_demo\rank_list_demo.srt
edge-tts --voice zh-CN-XiaoxiaoNeural --file docs\视频文字稿：rank_list_how_to.md --write-media media\bili\rank_list_demo\rank_list_how_to.mp3 --write-subtitles media\bili\rank_list_demo\rank_list_how_to.srt
```

## B站发布：标题、标签、简介…

标题：《【manim】从夯到拉锐评程序员失业出路（附制作教程）》

标签：宝藏知识UP跃迁计划, Python, manim, 从夯到拉, 经验分享, 程序员, 找工作, 程序员就业现状, 互联网, 大语言模型

```
今天带来的是用manim最基础的图形、动画能力做《从夯到拉锐评程序员失业出路》的教程。如果能够理解我上期教学视频的所有内容，那么写出这期视频的代码将会很轻松~
成品旁白是大龄做题人Hans不懂事，乱写的
推荐manim自学博客（同上期）：
1. 入门教程（除了比较老没啥缺点，也是这期视频的灵感源）： https://www.bilibili.com/opus/247191680174716386
2. manim 边做边学： https://www.cnblogs.com/wang_yb/p/18674709
3. animate 属性： https://juejin.cn/post/7507564752434806821
我的上期教学视频： https://www.bilibili.com/video/BV1GY2cBkEUo/
manim 源码传送门：
1. 讲解视频： https://github.com/Hans774882968/manim-hw/blob/main/rank_list_demo/rank_list_how_to.py
2. 成品： https://github.com/Hans774882968/manim-hw/blob/main/rank_list_demo/rank_list_demo.py
文字稿： https://github.com/Hans774882968/manim-hw/blob/main/media/bili/rank_list_demo/rank_list_how_to.srt
旁白模型：edge-tts 的 zh-CN-XiaoxiaoNeural
字体：站酷快乐体 https://ziti.xxriji.cn/
```

P2章节：

```
00:00 片头
00:10 学习材料
00:22 视频制作的主要步骤
00:40 画从夯到拉的背景图
01:17 背景图的边框宽度细节问题
02:35 素材图片的展示
03:02 素材图片的移动
04:48 后记
```

互动引导加在末尾

P1加评分弹幕：浅薄与魔怔程度 00:36

P1的互动引导加在02:50

P1加投票弹幕：00:20

喜欢我大前端吗

- 热爱可抵岁长
- 誓要转成后端
- 小前端闹麻了
- 前端是啥

P2加投票弹幕：00:25

你对manim可视化感兴趣吗

- 不关心
- 一般般
- 感兴趣
