## 让LLM生成开发规范的提示词

注：直接写这段提示词的效果也OK。

```markdown
大佬，你是一名数学科研工作者，精通manim。请叫我hans7。这段代码的编写遵循一些固定的范式

（需要把多种解法都放在同一个视频时用`tri_sina_add_2sinb_eq_2sinc\tri_sina_add_2sinb_eq_2sinc.py`，只需要生成解法，不需要头尾时用`tri_sina_add_2sinb_eq_2sinc\tri_2sinc_sol2.py`）

请参照这段代码来编写一段manim程序，来把以下博客文段视频化。

（法2：纯三角变换）
```

让LLM生成开发规范的提示词：

```markdown
大佬，你是一名数学科研工作者，精通manim。请叫我hans7。以下代码遵循某种固定的模式编写，请阅读代码，并输出一份manim代码规范

（`tri_sina_add_2sinb_eq_2sinc\tri_sina_add_2sinb_eq_2sinc.py`的代码）
```

## manim代码规范

### 总体结构

- 将场景划分为多个逻辑段落，每个段落封装为一个 **方法**（以 `show_` 开头）
- 每个方法完成一个**完整叙事单元**（如：标题、题干、思想、解法、结尾）
- 方法之间通过 **返回需移除的 VGroup** 实现动画过渡，避免全局变量污染

> ✅ 示例：
> ```python
> def show_problem_stmt(self) -> VGroup:
>     ...
>     return VGroup(title, stmt)
> ```

### 字体与颜色约定

| 元素类型        | 字体大小 | 颜色       | 说明 |
|-|--|--||
| 主标题          | 60     | `BLUE`    | 场景核心主题 |
| 小节标题（如“题干”“法3”） | 60     | `YELLOW`  | 结构标识 |
| 数学公式        | 默认   | 无（或 `BLUE` 强调） | `MathTex` 默认即可 |
| 作者/来源信息   | 24     | `YELLOW` / `#58C4DD` | 使用 `MarkupText` 支持颜色 |
| 最终答案        | 默认   | `BLUE` + `SurroundingRectangle` | 高亮关键结果 |

### 动画与节奏控制

#### 动画动词选择

- **出现**：一律使用`ReplacementTransform`切换之前已经出现的元素。如果是第一次出现，则使用`Write`
- **强调**：`Circumscribe()`、`Wiggle()`、`SurroundingRectangle()`

#### 等待时间（`self.wait()`）
- 所有 `wait()` 时间应**对应视频配音或思考时间**。
- 在代码注释中标注语音内容，便于后期对齐：
  ```python
  self.wait(16)  # “今天我带来了3种解法”
  ```

### 数学表达规范

#### 公式排版

- 使用 `MathTex` 而非 `Text` 表达数学式
- 一行推导里同时出现文本和数学公式时，不要在`MathTex`中使用`\text{}`，而是采用以下写法：

```python
VGroup(
  Text("由"),
  MathTex("a^2 = b^2 + c^2 - 2bc\cos A"),
  Text("得")
).arrange(RIGHT, buff=0.3)
```

- 多行推导使用 `VGroup` + `arrange(DOWN, aligned_edge=LEFT)` 对齐。
- 长公式可适当缩小字号（`font_size=36`）。

#### 推导链设计

- 关键等式用 `SurroundingRectangle` 高亮
- 避免在动画中“跳步”，保持逻辑连贯

```python
res_exprs = VGroup(
    MathTex(r"f = \frac{1}{\sin A} + \cdots"),
    MathTex(r"= \frac{bc}{2y(c-b)} + \cdots"),
    ...
).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
```

### 输入输出约定

- 每个 `show_xxx` 方法：
  - **输入**：上一阶段需移除的 `VGroup`（可选）
  - **输出**：本阶段创建的 `VGroup`（供下一阶段移除）
- 保持 **链式调用**，`construct()` 中无复杂逻辑

```python
def construct(self):
    self.show_bg()
    self.show_title()
    p = self.show_problem_stmt()
    t = self.show_thought(p)
    m = self.show_method3(t)
    self.show_ending(m)
```

### 结尾与互动设计

- 结尾包含：
  - “后记”标题
  - 制作说明（如“分P是因为电脑性能差”）
  - 价值主张（如“为做题人的精神自留地添砖加瓦”）
  - 互动呼吁（“一键三连”）
  - 致谢
- 使用 `Wiggle` + `Circumscribe` 强调互动按钮

### 附：推荐模板骨架

```python
from manim import *

class YourSceneName(Scene):
    def show_bg(self): ...
    def show_title(self): ...
    def show_problem_stmt(self) -> VGroup: ...
    def show_thought(self, problem_stmt_to_remove: VGroup) -> VGroup: ...
    def show_methodX(self, prev_to_remove: VGroup) -> VGroup: ...
    def show_ending(self, method_x_to_remove: VGroup): ...

    def construct(self):
        self.show_bg()
        self.show_title()
        p = self.show_problem_stmt()
        t = self.show_thought(p)
        m = self.show_methodX(t)
        self.show_ending(m)
```
