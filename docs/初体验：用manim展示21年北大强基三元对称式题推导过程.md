代码传送门：`pku_2021_sf_abc_problem.py`

初版代码提示词：

```
大佬，你是一名数学科研工作者，精通manim。请叫我hans7。我有一道题《2021北大强基： $a=ab+c$ ， $b=bc+a$ ， $c=ca+b$ ，求 $a+b+c$》。我为这题写好了一个正确的推理过程的文章，markdown格式。请写一段manim代码展示这篇文章。文章全文如下：
```

个人感觉，即使用通义千问帮忙写代码，这也还是个脏活累活，而且展示的效果也一般，感觉还不如写好PPT/博客+录屏演示。以后考虑只用manim展示需要画图像的题目

心得：

1. 通义千问似乎不太删除manim编程，我们需要给通义千问定规范，让它把说明文字和公式一组一组地展示。未整合的提示词如下：

```
大佬，希望你把我博客的一段话文字说明用Text包起来，和公式构成一个VGroup一起展示。比如，为了展示：

为了弄出 $abc$ ，我们分别乘c、a、b：

$$
ac = abc+c^2,\ ab = abc+a^2,\ bc = abc+b^2
$$

这段话，我写了如下代码：

step2_arr = [
    Text("为了弄出 abc ，我们分别乘c、a、b："),
    MathTex(r"ac = abc + c^2"),
    MathTex(r"ab = abc + a^2"),
    MathTex(r"bc = abc + b^2")
]
step2_group = VGroup(step2_arr).arrange(DOWN, buff=0.3)
self.play(Transform(sum_eq, step2_group))
self.wait(1)

请模仿这种风格进一步修改我下面给出的，我基于你给的代码调整过后的代码，把必要的文字说明和公式放在一个VGroup里展示。
```
