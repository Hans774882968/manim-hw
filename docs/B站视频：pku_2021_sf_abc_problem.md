AI朗读暂定采用`edge-tts`的：`zh-CN-XiaoxiaoNeural, zh-CN-XiaomengNeural`。示例命令：

```powershell
edge-tts --voice zh-CN-XiaomengNeural --text "欢迎回到我的频道，我是汉斯。今天我们来讲一道超机车的数学题。已知 a+b+c=0 ，求abc。我们得到a+b+c的平方等于负3abc。所以a+b+c=3" --write-media hello-xiaomeng.mp3 --write-subtitles hello-xiaomeng.srt
```

[预览`edge-tts`的声音模型](https://speech.microsoft.com/portal/voicegallery)

生成文字稿：

```powershell
edge-tts --voice zh-CN-XiaoxiaoNeural --file docs\视频文字稿：pku_2021_sf_abc_problem.md --write-media media\bili\pku_2021_sf_abc_problem.mp3 --write-subtitles media\bili\pku_2021_sf_abc_problem.srt
```

## BGM

grlymm用的《羽根》，我也跟着用了。问LLM这有没有限流风险：

```
大佬，我用manim做了个21年强基计划的数学题讲解视频，希望发布到b站。请问配乐选什么好？我希望配乐是循环播放的。并且我希望为视频添加一个ai旁白，请问如何添加？我没有视频剪辑基础，请讲解得详细些！

大佬，我初步选定bgm为《菊次郎的夏天》。请问选这首歌可能被b站限流吗？以及我如何获取这首歌的资源文件，并加进视频里？

大佬，那选用bgm为魔法少女小圆的《Sis puella magica》有被b站限流的风险吗？以及我如何获取这首歌的资源文件，并加进视频里？
```

kimi k2说风险很高，但发现它老在推那个什么《万兴喵影AI配乐》。我就又去问通义千问，它没有推这玩意了，但还是说风险很高。所以初步认定这是可信的。我还问了《羽根》的风险，它说中等，但我也懒得管了。

其他可考虑选项：

- https://freepd.com/upbeat.php 的 Ukulele Song

## 文字稿

`docs\视频文字稿：pku_2021_sf_abc_problem.md`

为了让AI读得流畅，会做一些改动，记得手动再改一下`edge-tts`生成的`.srt`文件。这个可以用Python脚本实现，写一个正向的replace和一个逆向的replace就行。

## B站发布：标题、标签、简介…

【manim】2021北大强基：考察三元对称式的题目

都选知识区

标签：新学期多点新知识, 高中数学, 学渣逆袭, 高中生必看, 强基计划, 三元对称式, 代数, manim

```
21年北大强基考察三元对称式的题目讲解~
题目来源： https://www.bilibili.com/video/BV1nh4y1M7h9
manim 源码传送门： https://github.com/Hans774882968/manim-hw/blob/main/pku_2021_sf_abc_problem.py
文字稿： https://hans774882968.github.io/teaching-plan-analytic-geometry/blog/2021%E5%8C%97%E5%A4%A7%E5%BC%BA%E5%9F%BA%EF%BC%9A%20%24a%3Dab%2Bc%24%20%EF%BC%8C%20%24b%3Dbc%2Ba%24%20%EF%BC%8C%20%24c%3Dca%2Bb%24%20%EF%BC%8C%E6%B1%82%20%24a%2Bb%2Bc%24
旁白模型：edge-tts 的 zh-CN-XiaoxiaoNeural
字体：站酷快乐体 https://ziti.xxriji.cn/
不管是文案还是剪辑都还有些不连贯。我会慢慢修改~
```

初版视频章节：

```
00:00 片头
00:09 题干
00:20 思想
00:34 题解
01:49 后记
```

其他两版视频章节：

```
00:00 片头
00:09 题干
00:20 思想
00:34 题解
02:00 后记
```

互动引导都加在“后记”章节

投票弹幕：

时间都是00:13

你觉得这题难度如何

- 太水了
- 一般
- 踮踮脚能够到
- 踮脚也够不着

## 抖音

话题： 知识分享, 高中数学, 强基计划, manim, 代数

## 小红书

标题：《2021北大强基：考察三元对称式的题目》

标签：高考数学, 学渣逆袭, 高中生必看, 强基计划, 三元对称式, 代数, manim
