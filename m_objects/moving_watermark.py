from manim import *
import random


class MovingWatermark(Text):
    def __init__(self, text: str, rand_mode=False, **kwargs):
        super().__init__(text, **kwargs)
        self.move_to(config.frame_width / 2 * RIGHT + config.frame_height / 2 * DOWN)
        self.velocity = np.array([
            random.uniform(-0.6, -0.3),
            random.uniform(0.3, 0.6),
            0.0
        ]) if rand_mode else np.array([-0.4114, 0.514, 0.0])

    def update_position(self, mob, dt):
        """
        更新位置的方法，用于 add_updater
        mob 是被更新的对象（即 self），dt 是时间增量
        """
        mob.shift(mob.velocity * dt)

        pos = mob.get_center()
        half_width = mob.width / 2
        half_height = mob.height / 2

        left_edge = pos[0] - half_width
        right_edge = pos[0] + half_width
        if left_edge <= -config.frame_width / 2:
            mob.velocity[0] = abs(mob.velocity[0])
            mob.shift(((-config.frame_width / 2) - left_edge + 1e-3) * RIGHT)
        elif right_edge >= config.frame_width / 2:
            mob.velocity[0] = -abs(mob.velocity[0])
            mob.shift(((config.frame_width / 2) - right_edge - 1e-3) * RIGHT)

        bottom_edge = pos[1] - half_height
        top_edge = pos[1] + half_height
        if bottom_edge <= -config.frame_height / 2:
            mob.velocity[1] = abs(mob.velocity[1])
            mob.shift(((-config.frame_height / 2) - bottom_edge + 1e-3) * UP)
        elif top_edge >= config.frame_height / 2:
            mob.velocity[1] = -abs(mob.velocity[1])
            mob.shift(((config.frame_height / 2) - top_edge - 1e-3) * UP)
