from manim import *
import os
import sys

sys.path.append(os.getcwd())

from m_objects.moving_watermark import MovingWatermark


def format_time(seconds):
    '''将秒数格式化为 MM:SS 字符串'''
    total_seconds = int(seconds)
    mins = total_seconds // 60
    secs = total_seconds % 60
    return f'{mins:02d}:{secs:02d}'


class Rotate3dDemo(ThreeDScene):
    def add_watermark(self):
        watermark = MovingWatermark("Hans码数理哲", font_size=20, color="#a1a1a1", z_index=114)
        watermark.add_updater(watermark.update_position)
        self.add(watermark)

    def construct(self):
        BG_COLOR = '#fff0f8'
        TEXT_PRIMARY = '#e6067a'
        self.set_camera_orientation(theta=-90 * DEGREES)
        self.camera.background_color = BG_COLOR

        self.add_watermark()

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

        time_text = Text('00:00', font="Consolas", color=TEXT_PRIMARY)
        TIME_TEXT_POSITION = 0.75 * UP
        time_text.shift(TIME_TEXT_POSITION)

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

        clock_time = ValueTracker(0)

        def update_clock(mob: Mobject, dt):
            current_time = clock_time.get_value()
            clock_time.increment_value(dt)
            new_time_text = Text(format_time(current_time), font="Consolas", color=TEXT_PRIMARY)
            new_time_text.shift(TIME_TEXT_POSITION)
            mob.become(new_time_text)

        img1.add_updater(make_z_rot_updater(time_tracker_1))
        img2.add_updater(make_z_rot_updater(time_tracker_2))
        img3.add_updater(make_y_rot_updater(time_tracker_3))
        time_text.add_updater(update_clock)

        self.add(img1, img2, img3, time_text)
        self.wait(60)
