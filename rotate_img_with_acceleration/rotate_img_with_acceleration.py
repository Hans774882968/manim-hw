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


class RotateImgWithAcceleration(Scene):
    def add_watermark(self):
        MUTED_FOREGROUND = '#c04283'
        watermark = MovingWatermark("Hans码数理哲", font_size=20, color=MUTED_FOREGROUND, z_index=114)
        watermark.add_updater(watermark.update_position)
        self.add(watermark)

    def construct(self):
        BG_COLOR = '#fff0f8'
        TEXT_PRIMARY = '#e6067a'
        self.camera.background_color = BG_COLOR

        self.add_watermark()

        img1 = ImageMobject('D:\\视频制作素材\\够赞头像.jpg')
        img2 = ImageMobject('D:\\视频制作素材\\够赞头像AI扩图后.jpg')
        img3 = ImageMobject('D:\\视频制作素材\\够赞头像.jpg')

        img1.scale_to_fit_width(3)
        img2.scale_to_fit_width(3)
        img3.scale_to_fit_width(3)

        img2.next_to(img1, RIGHT, buff=1.6)
        img3.next_to(img1, DOWN, buff=0.8)

        time_text = Text('00:00', font="Consolas", color=TEXT_PRIMARY)
        TIME_TEXT_POSITION = 2.4 * RIGHT + 1.9 * DOWN
        time_text.shift(TIME_TEXT_POSITION)

        all_mobs = Group(img1, img2, img3, time_text)
        all_mobs.center()

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

        clock_time = ValueTracker(0)

        def update_clock(mob: Mobject, dt):
            current_time = clock_time.get_value()
            clock_time.increment_value(dt)
            new_time_text = Text(format_time(current_time), font="Consolas", color=TEXT_PRIMARY)
            new_time_text.shift(TIME_TEXT_POSITION)
            mob.become(new_time_text)

        img1.add_updater(update_rotation_2d)
        img2.add_updater(update_rotation_2d)
        img3.add_updater(update_rotation_3d)
        time_text.add_updater(update_clock)

        self.add(all_mobs)
        self.wait(60)
