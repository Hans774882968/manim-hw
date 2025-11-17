from manim import *
import pandas as pd
from typing import Tuple


'''
代码能跑，但完全没有 race chart 的效果。不过我查到 bar-chart-race 这个 Python 包可以做
'''
CSV = """year,province,gdp
2019,广东,107671
2019,江苏,99631
2019,山东,71067
2019,浙江,62352
2019,河南,54259
2019,四川,46615
2019,湖北,45828
2019,福建,43903
2019,湖南,41781
2019,安徽,37114
2020,广东,110761
2020,江苏,102719
2020,山东,73129
2020,浙江,64613
2020,河南,54997
2020,四川,48598
2020,湖北,43443
2020,福建,45055
2020,湖南,41781
2020,安徽,38680
2021,广东,124369
2021,江苏,116364
2021,山东,83095
2021,浙江,73516
2021,河南,58887
2021,四川,53850
2021,湖北,50012
2021,福建,48810
2021,湖南,46063
2021,安徽,42959
2022,广东,129118
2022,江苏,122202
2022,山东,87435
2022,浙江,77715
2022,河南,61345
2022,四川,56749
2022,湖北,53734
2022,福建,53109
2022,湖南,48670
2022,安徽,45045
2023,广东,135673
2023,江苏,128222
2023,山东,92068
2023,浙江,82553
2023,河南,65041
2023,四川,60132
2023,湖北,56352
2023,福建,56758
2023,湖南,51752
2023,安徽,48118"""

df = pd.read_csv(pd.io.common.StringIO(CSV))
grouped = {y: d.sort_values("gdp", ascending=False) for y, d in df.groupby("year")}

BAR_HEIGHT = 0.45
BAR_GAP = 0.52
MAX_BAR_WIDTH = 10
LEFT_OFFSET = -6
TOP_ANCHOR = 2.5
FONT_SIZE = 26
COLOR_MAP = [BLUE_B, GREEN_B, TEAL_B, PURPLE_B, MAROON_B,
             YELLOW_B, ORANGE, PINK, RED_B, GRAY_B]


class GdpRaceChart(Scene):
    def construct(self):
        year_txt = Text("2019", font_size=48).to_edge(UP, buff=0.3)
        title = Text("中国各省GDP TOP10（2019-2023）", font_size=36, color=YELLOW)
        title.next_to(year_txt, DOWN, buff=0.2)
        self.add(year_txt, title)

        year = 2019
        bars, labels, values = self.bars_for_year(year)
        self.add(bars, labels, values)
        self.wait(0.5)

        for year in range(2020, 2024):
            new_bars, new_labels, new_values = self.bars_for_year(year)
            self.play(
                year_txt.animate.become(Text(str(year), font_size=48).to_edge(UP, buff=0.3)),
                *[Transform(*pair) for pair in zip(bars, new_bars)],
                *[Transform(*pair) for pair in zip(labels, new_labels)],
                *[Transform(*pair) for pair in zip(values, new_values)],
                run_time=1.2
            )
            self.wait(0.4)

        self.wait(2)

    def bars_for_year(self, year: int) -> Tuple[VGroup, VGroup, VGroup]:
        sub = grouped[year].reset_index(drop=True)
        max_gdp = sub["gdp"].max()
        bars, labels, values = VGroup(), VGroup(), VGroup()

        for rank, row in sub.iterrows():
            province, gdp = row["province"], row["gdp"]
            width = (gdp / max_gdp) * MAX_BAR_WIDTH
            bar = Rectangle(
                height=BAR_HEIGHT,
                width=width,
                color=COLOR_MAP[rank],
                fill_opacity=0.9,
                stroke_width=1.5
            )
            bar.move_to(LEFT_OFFSET * RIGHT + (TOP_ANCHOR - rank * BAR_GAP) * UP,
                        aligned_edge=LEFT)
            label = Text(province, font_size=FONT_SIZE).next_to(bar, LEFT, buff=0.15)
            value = Text(f"{gdp:,}", font_size=FONT_SIZE - 4).next_to(bar, RIGHT, buff=0.15)
            bars.add(bar)
            labels.add(label)
            values.add(value)
        return bars, labels, values
