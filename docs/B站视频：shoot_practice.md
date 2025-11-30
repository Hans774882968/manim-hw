## 旁白

```bash
edge-tts --voice zh-CN-XiaoxiaoNeural --file docs\视频文字稿：shoot_practice.md --write-media media\bili\shoot_practice\shoot_practice.mp3 --write-subtitles media\bili\shoot_practice\shoot_practice.srt
edge-tts --voice zh-CN-XiaoxiaoNeural --file docs\视频文字稿：shoot_how_to.md --write-media media\bili\shoot_practice\shoot_how_to.mp3 --write-subtitles media\bili\shoot_practice\shoot_how_to.srt
```

## B站发布：标题、标签、简介…

标题：《一起学习如何用manim做一条打靶视频（内含哲学meme）》

标签：宝藏知识UP跃迁计划, Python, manim, 经验分享, 3Blue1Brown, 尼采, 哲学, meme

```
今天带来的是用manim最基础的图形、动画能力做一条打靶视频的教程。成品融了点尼采哲学meme，如果造成精神污染，在此提前道个歉~
推荐manim自学博客：
1. 入门教程（除了比较老没啥缺点，也是这期视频的灵感源）： https://www.bilibili.com/opus/247191680174716386
2. manim 边做边学： https://www.cnblogs.com/wang_yb/p/18674709
3. animate 属性： https://juejin.cn/post/7507564752434806821
manim 源码传送门：
1. 讲解视频： https://github.com/Hans774882968/manim-hw/blob/main/shoot_practice/shoot_how_to.py
2. 成品： https://github.com/Hans774882968/manim-hw/blob/main/shoot_practice/shoot_practice.py
文字稿： https://github.com/Hans774882968/manim-hw/blob/main/media/bili/shoot_practice/shoot_how_to.srt
旁白模型：edge-tts 的 zh-CN-XiaoxiaoNeural
字体：站酷快乐体 https://ziti.xxriji.cn/
```

章节：

```
00:00 片头
00:10 学习材料
01:04 绘制图形
01:57 移动图形
02:30 图形的过渡动画
02:58 过渡动画的两种方法有区别吗
03:20 画瞄准镜、靶子
03:53 显示分数、模拟射击
04:17 模拟尼采精神崩溃的效果
05:24 后记
```

互动引导加在末尾

P1加投票弹幕：00:15

你对manim可视化感兴趣吗

- 不关心
- 一般般
- 感兴趣

P2加评分弹幕：浅薄与魔怔程度 00:05

P2的互动引导加在00:48

封面：

```powershell
magick shoot_practice-封面.png -resize 1920x2560! shoot_practice-封面-4x3.png
magick shoot_practice-封面.png -resize 1080x1080! shoot_practice-封面-1x1.png
magick shoot_merged_mosaic-封面.png -resize 1920x2560! shoot_merged_mosaic-封面-4x3.png
```

## 抖音

标题：《一起学习如何用manim做一条打靶视频（内含哲学meme）》

标签： Python, manim, 经验分享, 3Blue1Brown, 尼采

挑战：python（1294跟拍）

简介diff：只保留第一句话，其他的都扔掉，因为莫名其妙没有推流，好恶心！同时自我回复里的“通义千问”改成“tyqw”

注：第二次投抖音，使用以上简介diff，发现还是没有推流。所以第三次投抖音，我打算给原视频和自我回复的图做好马赛克，然后简介什么的不变

### kdenlive 马赛克

X坐标：449 729 996 1266
Y坐标：336 607 874
马赛克矩形大小：200 50

### gimp 马赛克

暂时不知道原因，但操作前要给png图像加一个alpha通道，否则只有最后一个添加的矩形区域能看到马赛克，前面的矩形区域都是黑色方块。

用“矩形选择工具”选好要马赛克的区域，然后上面菜单，滤镜→模糊→像素化，在弹出的设置窗口里选择方块

章节diff：

- 02:58 过渡动画的两种方法没区别
- 05:24 教程后记
- 05:40 成品

添加合集：manim开发教程 这里收录manim动画的开发教程~

## 小红书

标题：《来学习如何用manim做打靶视频（含哲学meme》

标签： Python, manim, 经验分享, 3Blue1Brown, 3blue1brown, 尼采, 哲学, meme

章节diff：

- 05:24 教程后记
- 05:40 成品
