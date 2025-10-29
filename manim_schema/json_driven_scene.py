from manim import *
import json
import argparse
from typing import List

schema_data = None
DIRECTION_MAP = {"UP": UP, "RIGHT": RIGHT, "DOWN": DOWN, "LEFT": LEFT}


def get_arrange_args(arrange_config):
    arrange_kwargs = {
        k: v for k, v in arrange_config.items()
        if k != "direction" and k != "aligned_edge"
    }
    aligned_edge = DIRECTION_MAP.get(arrange_config.get("aligned_edge", "").upper(), None)
    if aligned_edge is not None:
        arrange_kwargs["aligned_edge"] = aligned_edge
    direction = DIRECTION_MAP[arrange_config.get("direction", "DOWN").upper()]
    return direction, arrange_kwargs


def create_math_tex(math_tex_str: str | List[str], kwargs):
    if isinstance(math_tex_str, str):
        return MathTex(math_tex_str, **kwargs)
    return MathTex(*math_tex_str, **kwargs)


def math_tex_post_creation(math_tex: MathTex, elem):
    sub_tex, tex_color = elem.get("set_color_by_tex", (None, None))
    if sub_tex and tex_color:
        math_tex.set_color_by_tex(sub_tex, tex_color)
    tex_color_map = elem.get("set_color_by_tex_to_color_map", {})
    if tex_color_map:
        math_tex.set_color_by_tex_to_color_map(tex_color_map)
    return math_tex


def build_mobject_from_elem(elem: str | dict):
    # 支持字符串简写，给配置文件瘦身
    if isinstance(elem, str):
        return Text(elem, font_size=36)
    # 叶子节点
    if "type" in elem:
        elem_type = elem.get("type", "text")
        elem_content = elem.get("content", "")

        kwargs = {
            k: v for k, v in elem.items()
            if k not in ("type", "content", "set_color_by_tex", "set_color_by_tex_to_color_map")
        }

        if "font_size" not in kwargs:
            kwargs["font_size"] = 48 if elem_type == "math_tex" else 36

        if elem_type == "text":
            return Text(elem_content, **kwargs)
        elif elem_type == "math_tex":
            math_tex = create_math_tex(elem_content, kwargs)
            math_tex_post_creation(math_tex, elem)
            return math_tex
        elif elem_type == "markup_text":
            return MarkupText(elem_content, **kwargs)
        raise ValueError(f"Unknown element type: {elem_type}")
    # 嵌套 VGroup
    elif "elements" in elem:
        sub_elements = elem["elements"]
        sub_mobjects = [build_mobject_from_elem(e) for e in sub_elements]

        # 处理 arrange 配置
        arrange_config = elem.get("arrange", {})
        direction, arrange_kwargs = get_arrange_args(arrange_config)

        nested_vgroup = VGroup(*sub_mobjects)
        nested_vgroup.arrange(direction, **arrange_kwargs)
        return nested_vgroup

    raise ValueError(f"Invalid element: must have 'type' (leaf) or 'elements' (nested vgroup). Got: {elem}")


def get_title_group(title_data, is_subtitle_mode=False, **kwargs):
    if isinstance(title_data, str):
        return Text(title_data, font_size=60, **kwargs)
    if not isinstance(title_data, list):
        raise ValueError("title_data must be a string or string[]")
    text_list = [
        Text(t, font_size=48 if i else 60, **kwargs) for i, t in enumerate(title_data)
    ] if is_subtitle_mode else [Text(t, font_size=60, **kwargs) for t in title_data]
    return VGroup(*text_list).arrange(DOWN, buff=0.2)


class JsonDrivenScene(Scene):
    def show_bg(self):
        background = ImageMobject("assets/南澳岛.jpg")
        background.set_opacity(0.4)
        background.stretch_to_fit_width(config.frame_width)
        background.stretch_to_fit_height(config.frame_height)
        self.add(background)

    def show_title(self):
        title_data = schema_data["title"]
        title_group = get_title_group(title_data, color=BLUE)
        subtitle_arr = [
            Text("题源： https://www.bilibili.com/video/BV12DJXzoEgK", font_size=24, color=YELLOW),
            MarkupText("作者：<span foreground=\"#58C4DD\">hans7</span>", font_size=24),
            Text("我们必须想象，做题人是幸福的", font_size=24, color=BLUE),
            Text("文字稿传送门：见视频简介", font_size=24, color=YELLOW),
        ]
        subtitle_group = VGroup(*subtitle_arr).arrange(DOWN, buff=0.2)
        subtitle_group.next_to(title_group, DOWN, buff=0.5)

        title_whole = VGroup(title_group, subtitle_group)
        title_whole.move_to(ORIGIN)

        self.play(Write(title_group), run_time=1)
        self.play(FadeIn(subtitle_group, shift=DOWN))
        self.play(Circumscribe(subtitle_arr[2], run_time=4, color=BLUE))
        self.wait(17)
        self.play(FadeOut(title_group, subtitle_group))

    def construct(self):
        self.show_bg()
        self.show_title()

        sections = schema_data["sections"]
        current_mobjects = VGroup()  # 包含标题 + 当前 block 所有 vgroup

        for sec_idx, section in enumerate(sections):
            title_data = section["title"]
            is_subtitle_mode = section.get("subtitle_mode", False)
            title_mob = get_title_group(title_data, is_subtitle_mode=is_subtitle_mode, color=YELLOW)
            title_mob.to_edge(UP, buff=0.5)

            if sec_idx == 0:
                self.play(Write(title_mob))
            else:
                self.play(ReplacementTransform(current_mobjects, title_mob))
            current_mobjects = VGroup(title_mob)

            blocks = section.get("blocks", [])
            prev_page = VGroup()  # 上一页的所有 vgroup（不含标题）

            for blk_idx, block in enumerate(blocks):
                vgroups_in_block = []

                # 构建当前 block 的所有 VGroup
                vg_data_list = block.get("vgroups", [])
                for vg_data in vg_data_list:
                    arrange_config = vg_data.get("arrange", {})
                    direction, arrange_kwargs = get_arrange_args(arrange_config)

                    elements = vg_data.get("elements", [])
                    display_elements = []
                    for elem in elements:
                        m_obj = build_mobject_from_elem(elem)
                        display_elements.append(m_obj)

                    vgroup = VGroup(*display_elements)
                    vgroup.arrange(direction, **arrange_kwargs)
                    vgroups_in_block.append(vgroup)

                # 第一个 vgroup 在标题下方，后续 vgroup 依次堆叠在前一个下方
                if vgroups_in_block:
                    vgroups_in_block[0].next_to(title_mob, DOWN, buff=0.8)
                    for i in range(1, len(vgroups_in_block)):
                        vgroups_in_block[i].next_to(vgroups_in_block[i - 1], DOWN, buff=0.5)

                current_page = VGroup(*vgroups_in_block)

                # 第一个 block 逐个 Write
                if blk_idx == 0:
                    for vg, vg_data in zip(vgroups_in_block, vg_data_list):
                        self.play(Write(vg))
                        vg_wait_time = vg_data.get("wait", 0)
                        if vg_wait_time > 0:
                            self.wait(vg_wait_time)
                else:
                    # 后续 block 先用第一个 vgroup 替换上一个 block 的全部内容
                    self.play(ReplacementTransform(prev_page, vgroups_in_block[0]))
                    vg0_wait_time = vg_data_list[0].get("wait", 0)
                    if vg0_wait_time > 0:
                        self.wait(vg0_wait_time)
                    # 然后 Write 剩余的 vgroup（如果有）
                    vgroups_in_block1 = vgroups_in_block[1:]
                    vg_data_list1 = vg_data_list[1:]
                    for vg1, vg_data1 in zip(vgroups_in_block1, vg_data_list1):
                        self.play(Write(vg1))
                        vg_wait_time = vg_data1.get("wait", 0)
                        if vg_wait_time > 0:
                            self.wait(vg_wait_time)

                prev_page = current_page
                current_mobjects = VGroup(title_mob, current_page)

                page_wait_time = block.get("wait", 0)
                if page_wait_time > 0:
                    self.wait(page_wait_time)

            section_wait_time = section.get("wait", 0)
            if section_wait_time > 0:
                self.wait(section_wait_time)


def main(scene_cfg=None):
    global schema_data

    parser = argparse.ArgumentParser(description="批量替换字幕文件中的文本")
    parser.add_argument(
        "--config",
        "-c",
        type=str,
        help="JSON 配置文件路径"
    )
    parser.add_argument(
        "--quality",
        "-q",
        type=str,
        default="low_quality",
        help="输出视频的质量"
    )
    parser.add_argument(
        "--preview",
        "-p",
        default=True,
        help="是否预览视频"
    )
    args = parser.parse_args()
    if scene_cfg:
        schema_data = scene_cfg
    elif args.config:
        json_file_path = args.config
        with open(json_file_path, 'r', encoding='utf-8') as f:
            schema_data = json.load(f)

    output_file = schema_data["output_file"]
    config.output_file = output_file
    config.video_dir = '{media_dir}/videos/%s/{quality}' % (output_file)
    config.quality = args.quality
    config.preview = args.preview
    scene = JsonDrivenScene()
    scene.render()


if __name__ == "__main__":
    main()
