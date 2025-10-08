[TOC]

## 引言

学一下manim，为做视频做准备

## 安装manim

[manim官方文档](https://docs.manim.community/en/stable/installation/uv.html)强烈推荐用uv把manim安装在项目内。Python和uv的安装都很简单，略。首先用uv建一个项目：`uv init manim-hw`，然后在项目里直接`uv add manim`，最后准备一个`hw.py`：

```python
from manim import Text, Write, Scene


class HelloManim(Scene):
    def construct(self):
        text = Text("你好，Manim！", font="SimHei")
        self.play(Write(text))
        self.wait(2)
```

执行`uv run manim -pqh hw.py`，就能看到`media`文件夹被自动创建，然后一个高品质的视频生成在`media/videos/hw`文件夹。这里的h表示输出高品质视频，为了节省时间，在开发期间可以用参数`-pql`，表示生成低品质视频。

我个人是把`media`文件夹加进了`.gitignore`，我觉得因项目而异吧。

PS：我还尝试了用pip安装，但是遇到了报错：`cl.exe`未找到。懒得搜解决方案了，还是用uv轻松愉悦地安装吧。

### 安装tex编译器

为了在manim动画里渲染公式，我们必须安装一个tex编译器。根据manim官方文档推荐，我们安装[MiKTeX](https://miktex.org/download)。直接参照官方文档安装即可。安装完成后，执行`tex --version`应该能看到tex输出版本信息。

为了进一步验证manim可以渲染公式，我写了`tex_demo.py`（根据官网给的Examples修改），执行命令：`uv run manim -pqh tex_demo.py`。

## shape_transform_demo.py

展示基本图形及过渡动画。在这段代码中，我做了从正方形到圆的过渡、从圆到文字的过渡和从文字到文字的过渡。在做从圆到文字的过渡时，我发现圆并没有消失，文字直接出现在圆的中心位置，问了LLM，发现给的回答都不靠谱。后面发现只要把正方形删掉就OK了。

## 参考资料

1. 用uv安装manim： https://docs.manim.community/en/stable/installation/uv.html
