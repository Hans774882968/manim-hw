from manim import *


class RotateImgWithAcceleration(Scene):
    def construct(self):
        self.camera.background_color = '#fff0f8'

        img1 = ImageMobject('D:\\视频制作素材\\够赞头像.jpg')
        img2 = ImageMobject('D:\\视频制作素材\\够赞头像AI扩图后.jpg')
        img3 = ImageMobject('D:\\视频制作素材\\够赞头像.jpg')

        img1.scale_to_fit_width(3)
        img2.scale_to_fit_width(3)
        img3.scale_to_fit_width(3)

        img2.next_to(img1, RIGHT, buff=1.6)
        img3.next_to(img1, DOWN, buff=0.8)

        all_imgs = Group(img1, img2, img3)
        all_imgs.center()

        INITIAL_SPEED = 2
        ACCELERATION = 0.15

        time_tracker_2d = ValueTracker(0)

        def update_rotation_2d(mob: Mobject, dt):
            time_tracker_2d.increment_value(dt)
            new_speed = INITIAL_SPEED + ACCELERATION * time_tracker_2d.get_value()

            mob.rotate(
                new_speed * dt,
                about_point=mob.get_center()
            )

        time_tracker_3d = ValueTracker(0)

        def update_rotation_3d(mob: Mobject, dt):
            time_tracker_3d.increment_value(dt)
            new_speed = INITIAL_SPEED + ACCELERATION * time_tracker_3d.get_value()

            mob.rotate(
                new_speed * dt,
                axis=Y_AXIS,
            )

        img1.add_updater(update_rotation_2d)
        img2.add_updater(update_rotation_2d)
        img3.add_updater(update_rotation_3d)

        self.add(all_imgs)
        self.wait(60)
