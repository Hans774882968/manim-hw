DeepSeek生成第一版能跑的代码：

> 大佬，你是一名专家Python工程师，精通manim。请问manim如何实现加载一张`foo.png`，并让它不断原地旋转，且旋转速度越来越快

```python
from manim import *


class RotateImgWithAcceleration(Scene):
    def construct(self):
        img1 = ImageMobject('D:\\视频制作素材\\够赞头像.jpg')
        img2 = ImageMobject('D:\\视频制作素材\\够赞头像AI扩图后.jpg')

        img1.scale_to_fit_width(3)
        img2.scale_to_fit_width(3)

        img2.next_to(img1, RIGHT, buff=1.6)

        all_imgs = Group(img1, img2, img3)
        all_imgs.center()

        INITIAL_SPEED = 2
        ACCELERATION = 0.15
        time_tracker_2d = ValueTracker(0)

        def update_rotation_2d(mob, dt):
            time_tracker_2d.increment_value(dt)
            new_speed = INITIAL_SPEED + ACCELERATION * time_tracker_2d.get_value()
            mob.rotate(
                new_speed * dt,
                about_point=mob.get_center()
            )

        img1.add_updater(update_rotation_2d)
        img2.add_updater(update_rotation_2d)

        self.add(all_imgs)
        self.wait(60)
```

注：它生成了一个多余的变量`angular_speed = ValueTracker(1); angular_speed.set_value(new_speed)`，我把它删掉，发现还能正常跑

大佬，我现在的代码如下。它已经能正常旋转。现在我想新增一个img3，路径'D:\\视频制作素材\\够赞头像.jpg'，用和现有代码一样的旋转方式，但它是以图片的竖直对称轴为旋转轴，从外向里旋转。

这时发现DeepSeek生成的旋转代码有问题。
