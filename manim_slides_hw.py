from manim_slides.slide import Slide
from manim import *


class ManimSlidesHw(Slide):
    """WARNING: this example does not seem to work with ManimGL."""

    def construct(self):
        self.wait_time_between_slides = 0.1

        title = VGroup(
            Text("From Manim animations", t2c={"From": BLUE}),
            Text("to slides presentation", t2c={"to": BLUE}),
            Text("with Manim Slides", t2w={"[-12:]": BOLD}, t2c={"[-13:]": YELLOW}),
        ).arrange(DOWN)

        step_1 = Text("1. In your scenes file, import Manim Slides")
        step_2 = Text("2. Replace Scene with Slide")
        step_3 = Text("3. In construct, add pauses where you need")
        step_4 = Text("4. You can also create loops")
        step_5 = Text("5. Render your scene with Manim")
        step_6 = Text("6. Open your presentation with Manim Slides")

        for step in [step_1, step_2, step_3, step_4, step_5, step_6]:
            step.scale(0.5).to_corner(UL)

        step = step_1

        self.play(FadeIn(title))

        self.next_slide()

        code = Code(
            code_string="""from manim import *


class Example(Scene):
    def construct(self):
        dot = Dot()
        self.add(dot)

        self.play(Indicate(dot, scale_factor=2))

        square = Square()
        self.play(Transform(dot, square))

        self.play(Rotate(square, angle=PI/2))
""",
            language="python",
        )

        code_step_1 = Code(
            code_string="""from manim import *
from manim_slides import Slide

class Example(Scene):
    def construct(self):
        dot = Dot()
        self.add(dot)

        self.play(Indicate(dot, scale_factor=2))

        square = Square()
        self.play(Transform(dot, square))

        self.play(Rotate(square, angle=PI/2))
""",
            language="python",
        )

        code_step_2 = Code(
            code_string="""from manim import *
from manim_slides import Slide

class Example(Slide):
    def construct(self):
        dot = Dot()
        self.add(dot)

        self.play(Indicate(dot, scale_factor=2))

        square = Square()
        self.play(Transform(dot, square))

        self.play(Rotate(square, angle=PI/2))
""",
            language="python",
        )

        code_step_3 = Code(
            code_string="""from manim import *
from manim_slides import Slide

class Example(Slide):
    def construct(self):
        dot = Dot()
        self.add(dot)

        self.play(Indicate(dot, scale_factor=2))
        self.next_slide()
        square = Square()
        self.play(Transform(dot, square))
        self.next_slide()
        self.play(Rotate(square, angle=PI/2))
""",
            language="python",
        )

        code_step_4 = Code(
            code_string="""from manim import *
from manim_slides import Slide

class Example(Slide):
    def construct(self):
        dot = Dot()
        self.add(dot)
        self.next_slide(loop=True)
        self.play(Indicate(dot, scale_factor=2))
        self.next_slide()
        square = Square()
        self.play(Transform(dot, square))
        self.next_slide()
        self.play(Rotate(square, angle=PI/2))
""",
            language="python",
        )

        code_step_5 = Code(
            code_string="manim-slide render example.py Example",
            language="console",
        )

        code_step_6 = Code(
            code_string="manim-slides Example",
            language="console",
        )

        or_text = Text("or generate HTML presentation").scale(0.5)

        code_step_7 = Code(
            code_string="manim-slides convert Example slides.html --open",
            language="console",
        ).shift(DOWN)

        self.wipe(title, code)
        self.next_slide()

        self.play(FadeIn(step, shift=RIGHT))
        self.play(Transform(code, code_step_1))
        self.next_slide()

        self.play(Transform(step, step_2))
        self.play(Transform(code, code_step_2))
        self.next_slide()

        self.play(Transform(step, step_3))
        self.play(Transform(code, code_step_3))
        self.next_slide()

        self.play(Transform(step, step_4))
        self.play(Transform(code, code_step_4))
        self.next_slide()

        self.play(Transform(step, step_5))
        self.play(Transform(code, code_step_5))
        self.next_slide(auto_next=True)

        self.play(Transform(step, step_6))
        self.play(Transform(code, code_step_6))
        self.play(code.animate.shift(UP), FadeIn(code_step_7), FadeIn(or_text))

        watch_text = Text("Watch results on next slides!").shift(2 * DOWN).scale(0.5)

        self.next_slide(loop=True)
        self.play(FadeIn(watch_text))
        self.play(FadeOut(watch_text))
        self.next_slide()
        self.clear()

        dot = Dot()
        self.add(dot)
        self.next_slide(loop=True)
        self.play(Indicate(dot, scale_factor=2))
        self.next_slide()
        square = Square()
        self.play(Transform(dot, square))
        self.remove(dot)
        self.add(square)
        self.next_slide()
        self.play(Rotate(square, angle=PI / 4))
        self.next_slide()

        learn_more_text = (
            VGroup(
                Text("Learn more about Manim Slides:"),
                Text("https://github.com/jeertmans/manim-slides", color=YELLOW),
            )
            .arrange(DOWN)
            .scale(0.75)
        )

        self.play(Transform(square, learn_more_text))
        self.wait(3)
