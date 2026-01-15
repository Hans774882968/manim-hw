from manim import *


class Rotate3dBecomeDemo(Scene):
    def construct(self):
        self.camera.background_color = '#fff0f8'

        img3 = ImageMobject('D:\\视频制作素材\\够赞头像AI扩图后.jpg')
        IMG_WIDTH = 3
        img3.scale_to_fit_width(IMG_WIDTH)

        INITIAL_SPEED = 2
        ACCELERATION = 0.15

        time_tracker_3d = ValueTracker(0)

        def update_rotation_3d(mob: Mobject, dt):
            time_tracker_3d.increment_value(dt)
            new_speed = INITIAL_SPEED + ACCELERATION * time_tracker_3d.get_value()
            rotate_angle = new_speed * dt

            mob.become(
                mob.copy().apply_function(
                    lambda p: np.array([
                        p[0] * np.cos(rotate_angle) + p[2] * np.sin(rotate_angle),
                        p[1],
                        -p[0] * np.sin(rotate_angle) + p[2] * np.cos(rotate_angle)
                    ])
                )
            )

        img3.add_updater(update_rotation_3d)

        self.add(img3)
        self.wait(60)
