from manim import *


class Rotate3dDemo(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(theta=-90 * DEGREES)
        self.camera.background_color = '#fff0f8'

        img1_path = r'D:\视频制作素材\够赞头像.jpg'
        img2_path = r'D:\视频制作素材\够赞头像AI扩图后.jpg'
        img3_path = r'D:\视频制作素材\够赞头像.jpg'

        img1 = ImageMobject(img1_path)
        img2 = ImageMobject(img2_path)
        img3 = ImageMobject(img3_path)

        img1.scale_to_fit_width(3)
        img2.scale_to_fit_width(3)
        img3.scale_to_fit_width(3)

        img1.shift(LEFT * 3 + UP * 1.5)
        img2.shift(RIGHT * 3 + UP * 1.5)
        img3.shift(DOWN * 1.5)

        INITIAL_SPEED = 2
        ACCELERATION = 0.15

        time_tracker_1 = ValueTracker(0)
        time_tracker_2 = ValueTracker(0)
        time_tracker_3 = ValueTracker(0)

        def make_z_rot_updater(tracker):
            def updater(mob, dt):
                tracker.increment_value(dt)
                speed = INITIAL_SPEED + ACCELERATION * tracker.get_value()
                mob.rotate(speed * dt, axis=Z_AXIS, about_point=mob.get_center())
            return updater

        def make_y_rot_updater(tracker):
            def updater(mob, dt):
                tracker.increment_value(dt)
                speed = INITIAL_SPEED + ACCELERATION * tracker.get_value()
                mob.rotate(speed * dt, axis=Y_AXIS, about_point=mob.get_center())
            return updater

        img1.add_updater(make_z_rot_updater(time_tracker_1))
        img2.add_updater(make_z_rot_updater(time_tracker_2))
        img3.add_updater(make_y_rot_updater(time_tracker_3))

        self.add(img1, img2, img3)
        self.wait(60)
