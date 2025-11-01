type Direction = 'UP' | 'DOWN' | 'LEFT' | 'RIGHT';

// 默认 direction = DOWN, aligned_edge = ORIGIN
interface ArrangeConfig {
  direction?: Direction;
  aligned_edge?: Direction;
  buff?: number;
  // 其他 VGroup.arrange 支持的参数
  [key: string]: any;
}

// 默认 font_size = 36, color = WHITE
interface TextElement {
  type: 'text';
  content: string;
  font_size?: number;
  color?: string; // 如 "RED", "#FF0000", "WHITE"
  // 其他 Text 支持的属性
  [key: string]: any;
}

// 默认 font_size = 48, color = WHITE
interface MathTexElement {
  type: 'math_tex';
  content: string | string[];
  font_size?: number;
  color?: string;
  set_color_by_tex?: [string, string];
  set_color_by_tex_to_color_map?: Record<string, string>;
  // 其他 MathTex 支持的属性
  [key: string]: any;
}

// 默认 font_size = 36, color = WHITE
interface MarkupTextElement {
  type: 'markup_text';
  content: string;
  font_size?: number;
  color?: string;
  // 其他 MarkupText 支持的属性
  [key: string]: any;
}

interface NestedVGroupElement {
  elements: VgElement[];
  arrange?: ArrangeConfig;
}

// string 视为 TextElement
type VgElement = 'string' | TextElement | MathTexElement | MarkupTextElement | NestedVGroupElement;

interface AnimationDescription {
  type: "indicate" | "circumscribe" | "surrounding_rectangle";
  target: string;
  // 给 Indicate, Circumscribe 等类透传的属性
  [key: string]: any;
}

interface VGroupData extends NestedVGroupElement {
  wait?: number; // 每个 vgroup 渲染后的等待时间（秒）。默认为 0
  anime?: AnimationDescription[];
}

// 一块占一页
interface Block {
  vgroups: VGroupData[];
  wait?: number; // 页与页之间的等待时间（秒）。默认为 0
}

type Title = string | string[];

// 一小节占多页
interface Section {
  title: Title;
  subtitle_mode: boolean; // True 表示 title[1:] 作为副标题
  blocks: Block[];
  wait?: number; // 小节与小节之间的等待时间（秒）。默认为 0
}

interface ManimJsonSchema {
  output_file: string;
  title: Title;
  problem_source?: string;
  title_wait?: number; // 标题页的等待时间（秒）。默认为 17
  ending_wait?: number; // 后记页的等待时间（秒）。默认为 16
  sections: Section[];
}
