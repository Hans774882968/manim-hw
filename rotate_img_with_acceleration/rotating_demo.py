from manim import *


class RotatingDemo(Scene):
    '''
    这种做法不好，既不省编译时间，跑出来效果也有突然的停顿，不对头
    '''

    def construct(self):
        img1 = ImageMobject('D:\\视频制作素材\\够赞头像.jpg')
        img2 = ImageMobject('D:\\视频制作素材\\够赞头像AI扩图后.jpg')
        img1.scale_to_fit_width(3)
        img2.scale_to_fit_width(3)
        img2.next_to(img1, RIGHT, buff=1.6)
        img_gp = Group(img1, img2)
        img_gp.center()

        INITIAL_SPEED = 1.5
        ACCELERATION = 0.15
        time_used = 0
        current_speed = INITIAL_SPEED
        while time_used < 60:
            run_time = TAU / current_speed
            r_anim1 = Rotating(
                img1,
                axis=OUT,
                radians=TAU,
                about_point=img1.get_center(),
                run_time=run_time,
            )
            r_anim2 = Rotating(
                img2,
                axis=OUT,
                radians=TAU,
                about_point=img2.get_center(),
                run_time=run_time,
            )
            self.play(r_anim1, r_anim2)

            time_used += run_time
            current_speed += ACCELERATION
