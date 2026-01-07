from manim import *


class OpeningAnimation(Scene):
    def show_bg(self):
        background = ImageMobject(r"D:\视频制作素材\视频背景\BV1DY411T7TQ的风景壁纸2.jpg")
        background.set_opacity(0.4)
        background.stretch_to_fit_width(config.frame_width)
        background.stretch_to_fit_height(config.frame_height)
        self.add(background)
        return background

    def construct(self):
        self.show_bg()

        avatar = ImageMobject(r"assets\opening_animation\兔斯基头像-圆形.png")
        avatar.scale(2)
        avatar.shift(UP * 1.5)

        # 昵称“Hans码数理哲”分段着色
        colors = [BLUE, GREEN, ORANGE, PINK, PURPLE]
        nickname_parts = VGroup(
            Text("Hans", color=colors[0], font_size=60),
            Text("码", color=colors[1], font_size=60),
            Text("数", color=colors[2], font_size=60),
            Text("理", color=colors[3], font_size=60),
            Text("哲", color=colors[4], font_size=60),
        )
        nickname_parts.arrange(RIGHT, buff=0)
        nickname_parts.next_to(avatar, DOWN, buff=0.8)

        self.play(FadeIn(avatar), Write(nickname_parts), run_time=0.8)
        self.wait(0.5)

        # ========== 第二阶段：头像与“Hans”消失；其余四字分行排布 ==========
        # 保存“码数理哲”以供后续使用
        char_code = nickname_parts[1].copy().scale(2 / 3)
        char_math = nickname_parts[2].copy().scale(2 / 3)
        char_physics = nickname_parts[3].copy().scale(2 / 3)
        char_phil = nickname_parts[4].copy().scale(2 / 3)

        # 将四个字移到各自行中央
        center_y = 1.5
        spacing = 0.65
        spacing_avatar = 0.8
        char_code.move_to(ORIGIN + UP * (center_y - spacing))
        char_math.move_to(ORIGIN + UP * (center_y - 2 * spacing))
        char_physics.move_to(ORIGIN + UP * (center_y - 3 * spacing))
        char_phil.move_to(ORIGIN + UP * (center_y - 4 * spacing))

        self.play(
            FadeOut(nickname_parts[0]),
            avatar.animate.move_to(ORIGIN + UP * (center_y + spacing_avatar)).scale(0.7),
            Transform(nickname_parts[1], char_code),
            Transform(nickname_parts[2], char_math),
            Transform(nickname_parts[3], char_physics),
            Transform(nickname_parts[4], char_phil),
            run_time=0.5
        )

        # ========== 第三阶段：同时显示对应文字与底部引言 ==========
        missing_texts = VGroup(
            Text("代", color=colors[1], font_size=40).next_to(char_code, LEFT, buff=0),
            Text("学", color=colors[2], font_size=40).next_to(char_math, RIGHT, buff=0),
            Text("物", color=colors[3], font_size=40).next_to(char_physics, LEFT, buff=0),
            Text("学", color=colors[4], font_size=40).next_to(char_phil, RIGHT, buff=0),
        )

        quote_line1 = MarkupText(f"我们必须想象，<span foreground=\"{BLUE}\">做题人</span>是<span foreground=\"{RED}\">幸福</span>的", font_size=28)
        quote_line2 = MarkupText(f"——爱<span foreground=\"{GREEN}\">生命</span>的我们", font_size=24)
        quote_line1.to_edge(DOWN, buff=2)
        quote_line2.next_to(quote_line1, DOWN, aligned_edge=RIGHT)

        self.play(
            Write(missing_texts[0], reverse=True, remover=False),
            Write(missing_texts[1]),
            Write(missing_texts[2], reverse=True, remover=False),
            Write(missing_texts[3]),
            Write(quote_line1),
            Write(quote_line2),
            run_time=0.8
        )

        self.wait(0.5)

        self.play(
            FadeOut(avatar),
            FadeOut(nickname_parts[1:]),
            FadeOut(missing_texts),
            FadeOut(quote_line1),
            FadeOut(quote_line2),
            run_time=0.8
        )
