from manim import *
import json
import argparse
from typing import List, Dict, Any, Union

DEFAULT_FONT_SIZE = {
    "title": 60,
    "subtitle": 48,
    "text": 36,
    "math_tex": 48,
    "footer": 24,
}
DEFAULT_COLORS = {
    "title": BLUE,
    "section_title": YELLOW,
    "footer_text": YELLOW,
    "footer_author": "#58C4DD",
}
BACKGROUND_IMAGE_PATH = "assets/南澳岛.jpg"
BACKGROUND_OPACITY = 0.4

DIRECTION_MAP = {"UP": UP, "RIGHT": RIGHT, "DOWN": DOWN, "LEFT": LEFT}


def filter_kwargs(elem: Dict[str, Any], exclude_keys: set) -> Dict[str, Any]:
    return {k: v for k, v in elem.items() if k not in exclude_keys}


def get_arrange_args(arrange_config: Dict[str, Any]):
    arrange_kwargs = filter_kwargs(arrange_config, {"direction", "aligned_edge"})
    aligned_edge = DIRECTION_MAP.get(arrange_config.get("aligned_edge", "").upper())
    if aligned_edge is not None:
        arrange_kwargs["aligned_edge"] = aligned_edge
    direction = DIRECTION_MAP[arrange_config.get("direction", "DOWN").upper()]
    return direction, arrange_kwargs


def create_math_tex(math_tex_str: Union[str, List[str]], kwargs: Dict[str, Any]) -> MathTex:
    if isinstance(math_tex_str, str):
        return MathTex(math_tex_str, **kwargs)
    return MathTex(*math_tex_str, **kwargs)


def apply_math_tex_post_processing(math_tex: MathTex, elem: Dict[str, Any]) -> MathTex:
    sub_tex, tex_color = elem.get("set_color_by_tex", (None, None))
    if sub_tex and tex_color:
        math_tex.set_color_by_tex(sub_tex, tex_color)
    tex_color_map = elem.get("set_color_by_tex_to_color_map", {})
    if tex_color_map:
        math_tex.set_color_by_tex_to_color_map(tex_color_map)
    return math_tex


def build_mobject_from_elem(elem: Union[str, Dict[str, Any]], vgroup_pool: Dict[str, Mobject]) -> Mobject:
    # 支持字符串简写，给配置文件瘦身
    if isinstance(elem, str):
        return Text(elem, font_size=DEFAULT_FONT_SIZE["text"])
    # 叶子节点
    if "type" in elem:
        elem_type = elem.get("type", "text")
        elem_content = elem.get("content", "")
        exclude_keys = {"id", "type", "content", "set_color_by_tex", "set_color_by_tex_to_color_map"}
        kwargs = filter_kwargs(elem, exclude_keys)

        if "font_size" not in kwargs:
            kwargs["font_size"] = DEFAULT_FONT_SIZE.get(elem_type, DEFAULT_FONT_SIZE["text"])

        if elem_type == "text":
            return Text(elem_content, **kwargs)
        elif elem_type == "math_tex":
            math_tex = create_math_tex(elem_content, kwargs)
            math_tex = apply_math_tex_post_processing(math_tex, elem)
            return math_tex
        elif elem_type == "markup_text":
            return MarkupText(elem_content, **kwargs)
        raise ValueError(f"Unknown element type: {elem_type}")
    # 嵌套 VGroup
    elif "elements" in elem:
        sub_elements = elem["elements"]
        sub_mobjects = [build_mobject_from_elem(e, vgroup_pool) for e in sub_elements]
        for sm, e in zip(sub_mobjects, sub_elements):
            if "id" in e:
                vgroup_pool[e["id"]] = sm

        arrange_config = elem.get("arrange", {})
        direction, arrange_kwargs = get_arrange_args(arrange_config)

        nested_vgroup = VGroup(*sub_mobjects)
        nested_vgroup.arrange(direction, **arrange_kwargs)
        return nested_vgroup

    raise ValueError(f"Invalid element: must have 'type' (leaf) or 'elements' (nested vgroup). Got: {elem}")


def build_title_group(title_data: Union[str, List[str]], is_subtitle_mode: bool = False, **kwargs) -> Mobject:
    if isinstance(title_data, str):
        return Text(title_data, font_size=DEFAULT_FONT_SIZE["title"], **kwargs)
    if not isinstance(title_data, list):
        raise ValueError("title_data must be str or List[str]")

    if is_subtitle_mode:
        text_list = [
            Text(t, font_size=(DEFAULT_FONT_SIZE["subtitle"] if i else DEFAULT_FONT_SIZE["title"]), **kwargs)
            for i, t in enumerate(title_data)
        ]
    else:
        text_list = [Text(t, font_size=DEFAULT_FONT_SIZE["title"], **kwargs) for t in title_data]
    return VGroup(*text_list).arrange(DOWN, buff=0.2)


class JsonDrivenScene(Scene):
    def my_setup(self, schema_data, last_section_to_remove=None):
        '''
        manim 不推荐覆盖 `__init__` 方法（实测能正常运行），但 setup 不支持传参
        所以引入一个 my_setup 方法，并调用 check_schema_data 确保有 schema 数据
        '''
        self.schema_data = schema_data
        self.last_section_to_remove = last_section_to_remove
        self.vgroup_pool = {}
        self.section_to_remove = None

    def show_bg(self):
        background = ImageMobject(BACKGROUND_IMAGE_PATH)
        background.set_opacity(BACKGROUND_OPACITY)
        background.stretch_to_fit_width(config.frame_width)
        background.stretch_to_fit_height(config.frame_height)
        self.add(background)

    def show_title(self):
        title_data = self.schema_data["title"]
        problem_source = self.schema_data.get("problem_source", "")
        title_group = build_title_group(title_data, color=BLUE)
        subtitle_arr = ([
            Text(f"题源： {problem_source}", font_size=DEFAULT_FONT_SIZE["footer"], color=YELLOW),
        ] if problem_source else []) + [
            MarkupText("作者：<span foreground=\"#58C4DD\">hans7</span>", font_size=DEFAULT_FONT_SIZE["footer"]),
            Text("我们必须想象，做题人是幸福的", font_size=DEFAULT_FONT_SIZE["footer"], color=BLUE),
            Text("文字稿传送门：见视频简介", font_size=DEFAULT_FONT_SIZE["footer"], color=YELLOW),
        ]
        subtitle_group = VGroup(*subtitle_arr).arrange(DOWN, buff=0.2)
        subtitle_group.next_to(title_group, DOWN, buff=0.5)

        title_whole = VGroup(title_group, subtitle_group)
        title_whole.move_to(ORIGIN)

        self.play(Write(title_group), run_time=1)
        self.play(FadeIn(subtitle_group, shift=DOWN))
        self.play(Circumscribe(subtitle_arr[2], run_time=4, color=BLUE))
        title_wait = self.schema_data.get("title_wait", 17)
        self.wait(title_wait)
        self.play(FadeOut(title_group, subtitle_group))

    def show_ending(self, last_section_to_remove):
        postscript_arr = [
            Text("后记", font_size=60, color=YELLOW),
            Text("为做题人的精神自留地添砖加瓦", font_size=28, color=RED),
            Text("喜欢本期视频的话，别忘了一键三连哦", font_size=28, color=PINK),
            Text("谢谢观看~", font_size=28),
        ]
        postscript_group = VGroup(*postscript_arr).arrange(DOWN, buff=0.4)
        self.play(ReplacementTransform(last_section_to_remove, postscript_group))
        self.play(
            Wiggle(postscript_group[-3]),
            Circumscribe(postscript_group[-2], run_time=4, color=PINK)
        )
        self.play(
            Wiggle(postscript_group[-3]),
            Wiggle(postscript_group[-2])
        )
        ending_wait = self.schema_data.get("ending_wait", 16)
        self.wait(ending_wait)

    def play_anime_in_vgroup(self, vg_data):
        anime_descriptions = vg_data.get("anime")
        if not anime_descriptions:
            return
        for anime_desc in anime_descriptions:
            anime_type = anime_desc.get("type")
            target_id = anime_desc.get("target")
            kwargs = filter_kwargs(anime_desc, {"type", "target"})

            if target_id not in self.vgroup_pool:
                continue
            tgt = self.vgroup_pool[target_id]

            if anime_type == "indicate":
                self.play(Indicate(tgt, color=BLUE, **kwargs))
            elif anime_type == "circumscribe":
                self.play(Circumscribe(tgt, color=BLUE, **kwargs))
            elif anime_type == "surrounding_rectangle":
                frame_box = SurroundingRectangle(tgt, color=BLUE, **kwargs)
                self.play(Create(frame_box))
                self.mobjects_to_remove_on_page.append(frame_box)

    def play_vg_animation_and_wait(self, vgroups_in_block, vg_data_list):
        for vg, vg_data in zip(vgroups_in_block, vg_data_list):
            self.play(Write(vg))

            self.play_anime_in_vgroup(vg_data)

            vg_wait_time = vg_data.get("wait", 0)
            if vg_wait_time > 0:
                self.wait(vg_wait_time)

    def show_sections(self, last_section_to_remove=None):
        sections = self.schema_data if isinstance(self, JsonSceneFragment) else self.schema_data["sections"]
        current_mobjects = VGroup()  # 包含标题 + 当前 block 所有 vgroup

        for sec_idx, section in enumerate(sections):
            title_data = section["title"]
            is_subtitle_mode = section.get("subtitle_mode", False)
            title_mob = build_title_group(
                title_data,
                is_subtitle_mode=is_subtitle_mode,
                color=DEFAULT_COLORS["section_title"]
            )
            title_mob.to_edge(UP, buff=0.5)

            if sec_idx == 0:
                if last_section_to_remove is None:
                    self.play(Write(title_mob))
                else:
                    self.play(ReplacementTransform(last_section_to_remove, title_mob))
            else:
                self.play(ReplacementTransform(current_mobjects, title_mob))
            current_mobjects = VGroup(title_mob)

            blocks = section.get("blocks", [])
            prev_page = VGroup()  # 上一页的所有 vgroup（不含标题）

            for blk_idx, block in enumerate(blocks):
                self.mobjects_to_remove_on_page = []
                vgroups_in_block = []
                vg_data_list = block.get("vgroups", [])
                for vg_data in vg_data_list:
                    arrange_config = vg_data.get("arrange", {})
                    direction, arrange_kwargs = get_arrange_args(arrange_config)

                    elements = vg_data.get("elements", [])
                    display_elements = [build_mobject_from_elem(elem, self.vgroup_pool) for elem in elements]
                    for d_elem, elem in zip(display_elements, elements):
                        if "id" in elem:
                            self.vgroup_pool[elem["id"]] = d_elem
                    vgroup = VGroup(*display_elements).arrange(direction, **arrange_kwargs)
                    vgroups_in_block.append(vgroup)

                # 第一个 vgroup 在标题下方，后续 vgroup 依次堆叠在前一个下方
                if vgroups_in_block:
                    vgroups_in_block[0].next_to(title_mob, DOWN, buff=0.8)
                    for i in range(1, len(vgroups_in_block)):
                        vgroups_in_block[i].next_to(vgroups_in_block[i - 1], DOWN, buff=0.5)

                current_page = VGroup(*vgroups_in_block)

                # 第一个 block 逐个 Write
                if blk_idx == 0:
                    self.play_vg_animation_and_wait(vgroups_in_block, vg_data_list)
                else:
                    # 后续 block 先用第一个 vgroup 替换上一个 block 的全部内容
                    self.play(ReplacementTransform(prev_page, vgroups_in_block[0]))
                    self.play_anime_in_vgroup(vg_data_list[0])
                    vg0_wait_time = vg_data_list[0].get("wait", 0)
                    if vg0_wait_time > 0:
                        self.wait(vg0_wait_time)
                    # 然后 Write 剩余的 vgroup（如果有）
                    vgroups_in_block1 = vgroups_in_block[1:]
                    vg_data_list1 = vg_data_list[1:]
                    self.play_vg_animation_and_wait(vgroups_in_block1, vg_data_list1)

                prev_page = current_page
                current_mobjects = VGroup(title_mob, current_page)

                page_wait_time = block.get("wait", 0)
                if page_wait_time > 0:
                    self.wait(page_wait_time)

                if self.mobjects_to_remove_on_page:
                    self.remove(*self.mobjects_to_remove_on_page)
                    self.mobjects_to_remove_on_page.clear()

            section_wait_time = section.get("wait", 0)
            if section_wait_time > 0:
                self.wait(section_wait_time)

        return current_mobjects

    def construct(self):
        self.check_schema_data()
        self.show_bg()
        self.show_title()
        current_mobjects = self.show_sections()
        self.show_ending(current_mobjects)

    def set_schema_data(self, schema_data: Dict[str, Any]):
        self.schema_data = schema_data

    def check_schema_data(self):
        if not self.schema_data:
            raise ValueError("self.schema_data is not set")


class JsonSceneFragment(JsonDrivenScene):
    def build(self):
        self.check_schema_data()
        current_mobjects = self.show_sections(self.last_section_to_remove)
        self.section_to_remove = current_mobjects


def main(scene_cfg: Dict[str, Any] = None):
    parser = argparse.ArgumentParser(description="JSON-driven Manim scene renderer")
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
    else:
        raise ValueError("Either scene_cfg or --config must be provided")

    output_file = schema_data["output_file"]
    config.output_file = output_file
    config.video_dir = '{media_dir}/videos/%s/{quality}' % (output_file)
    config.quality = args.quality
    config.preview = args.preview
    scene = JsonDrivenScene()
    scene.my_setup(schema_data)
    scene.render()


if __name__ == "__main__":
    main()
