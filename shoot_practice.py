from manim import *
import random


class ShootPractice(Scene):
    def draw_aim_scope(self):
        outer_circle = Circle(radius=0.8, color=BLUE)
        inner_circle = Circle(radius=0.1, color=RED, fill_color=RED, fill_opacity=1)
        line_vertical = Line(start=outer_circle.get_bottom(), end=outer_circle.get_top(), color=RED)
        line_horizontal = Line(start=outer_circle.get_left(), end=outer_circle.get_right(), color=RED)
        aim_scope = VGroup(outer_circle, inner_circle, line_vertical, line_horizontal)
        self.play(FadeIn(aim_scope))
        self.wait(0.5)
        self.play(ApplyMethod(aim_scope.shift, LEFT * 5.6 + UP * 2.4))
        return aim_scope

    def draw_targets(self, r=3, c=4):
        target_labels = [
            "悲剧之溃", "群氓道德", "末人庸众", "怨恨之毒",
            "彼岸幻影", "神之尸骸", "真理暴政", "理性偶像",
            "历史滥用", "平等谎言", "怜悯枷锁", "禁欲理想"
        ]
        targets = []
        labels = []
        hit_counts = []
        idx = 0
        for i in range(r):
            tgt_tmp = []
            lbl_tmp = []
            cnt_tmp = []
            for j in range(c):
                target = Circle(radius=0.4, color=GRAY, fill_color=GRAY, fill_opacity=0.4)
                target.shift((-3 + 2 * j) * RIGHT + (-2 + 2 * i) * DOWN)
                label = Text(target_labels[idx], font_size=24, color=GRAY)
                label.next_to(target, DOWN, buff=0.1)
                self.play(FadeIn(target), FadeIn(label))
                tgt_tmp.append(target)
                lbl_tmp.append(label)
                cnt_tmp.append(0)
                idx += 1
            targets.append(tgt_tmp)
            labels.append(lbl_tmp)
            hit_counts.append(cnt_tmp)
        self.hit_counts = hit_counts
        self.labels = labels
        return targets

    def shoot(self, aim_scope, targets, r: int, c: int):
        goal = targets[r][c]
        label = self.labels[r][c]
        self.play(ApplyMethod(aim_scope.next_to, goal, ORIGIN))
        self.hit_counts[r][c] += 1
        if self.hit_counts[r][c] == 1:
            new_color = GREEN
        elif self.hit_counts[r][c] == 2:
            new_color = ORANGE
        else:
            new_color = RED
        self.play(
            ApplyMethod(goal.set_fill, new_color),
            ApplyMethod(goal.set_color, new_color),
            ApplyMethod(label.set_color, new_color),
        )
        self.wait(0.2)

    def construct(self):
        aim_scope = self.draw_aim_scope()
        targets = self.draw_targets()
        nihilism_score_text = Text("虚无刻度：", font_size=36)
        nihilism_score_text.to_edge(UP)
        nihilism_score = Integer(0).next_to(nihilism_score_text, RIGHT)
        self.play(FadeIn(nihilism_score_text), FadeIn(nihilism_score))
        self.play(ApplyMethod(aim_scope.next_to, LEFT * 3.6 + DOWN * 1.2, ORIGIN))
        self.wait(0.4)
        shoot_seq = (
            (1, 2), (2, 2), (0, 0), (2, 0),
            (0, 3), (1, 0), (2, 1), (0, 1),
            (0, 2), (2, 3), (1, 3), (1, 1),
            (1, 2), (2, 2), (0, 0), (1, 0),
            # (0, 3), (2, 0), (2, 1), (0, 1),
            # (0, 2), (2, 3), (1, 3), (1, 1),
        )
        for (r, c) in shoot_seq:
            self.shoot(aim_scope, targets, r, c)
            new_nihilism_score = Integer(nihilism_score.get_value() + 1).next_to(nihilism_score_text, RIGHT)
            self.play(ReplacementTransform(nihilism_score, new_nihilism_score))
            nihilism_score = new_nihilism_score
        self.wait()

        all_targets = VGroup(*[t for row in targets for t in row])
        all_labels = VGroup(*[l for row in self.labels for l in row])
        target_shifts = []
        for target in all_targets:
            random_pos = np.array([random.uniform(-0.4, 0.4), random.uniform(-0.2, 0.2), 0])
            target_shifts.append(ApplyMethod(target.shift, random_pos))
        self.play(*target_shifts, run_time=0.8)
        aim_scope_shift_direction = LEFT * 3 + DOWN * 2
        self.play(
            all_targets.animate.set_color(RED_E).scale(1.2),
            all_labels.animate.set_color(RED).scale(1.2),
            nihilism_score.animate.set_value(999),
            ApplyMethod(aim_scope.shift, aim_scope_shift_direction),
            ApplyMethod(aim_scope[2].shift, aim_scope_shift_direction + UP * 0.3 + 0.1 * RIGHT),  # 十字线错位
            ApplyMethod(aim_scope[3].shift, aim_scope_shift_direction + LEFT * 0.3 + 0.1 * UP),
            run_time=0.8
        )
        self.wait(0.6)

        collapse_group = VGroup(all_targets, all_labels, aim_scope, nihilism_score_text, nihilism_score)
        self.play(collapse_group.animate.scale(0.01).set_color(BLACK), run_time=0.3)
        self.wait(0.2)
        final_quote_line1 = Text("Ich bin kein Mensch, ich bin Dynamit.", font_size=36, color=RED)
        final_quote_line2 = Text("我不是人，我是炸药！", font_size=36, color=RED)
        final_quote_line3 = Text("——尼采", font_size=30)
        quote_group = VGroup(final_quote_line1, final_quote_line2).arrange(DOWN, aligned_edge=ORIGIN)
        final_quote_line3.next_to(quote_group, DOWN, aligned_edge=RIGHT)
        self.play(FadeIn(final_quote_line1), FadeIn(final_quote_line2), FadeIn(final_quote_line3))
        self.wait(2)
