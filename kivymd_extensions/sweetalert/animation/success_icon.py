# Written by shashi278
#
# Refer:
#    https://github.com/shashi278/AndroidView/blob/master/demo/success_anim.gif
#    https://github.com/shashi278/AndroidView/blob/master/demo/success_anim.py

from kivy.lang import Builder
from kivy.animation import Animation
from kivy.metrics import dp

from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_string(
    """
<SuccessAnimation>:
    md_bg_color: 1, 1, 1, 0
    angle_start: 0
    angle_end: 0
    tick_x1: 0
    tick_y1: 0
    tick_x2: 0
    tick_y2: 0
    tick_x3: 0
    tick_y3: 0

    MDBoxLayout:
        id: box_layout
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: None, None
        height: 100
        width: 100
        md_bg_color: 1, 1, 1, 0

        canvas:
            Color:
                rgba: 0, 1, 0, .2
            SmoothLine:
                circle: self.center_x, self.center_y, self.width / 2 - dp(5), 0,360
                width: dp(2.25)
            Color:
                rgba: 0, 1, 0, 1
            SmoothLine:
                circle: self.center_x, self.center_y, self.width / 2 - dp(5), root.angle_start, root.angle_end
                width: dp(2.25)
                cap: "square"
            SmoothLine:
                points: root.tick_x1, root.tick_y1, root.tick_x2, root.tick_y2
                width: dp(2.25)
                cap: "square"
            SmoothLine:
                points: root.tick_x2, root.tick_y2, root.tick_x3, root.tick_y3
                width: dp(2.25)
                cap: "square"
"""
)


class SuccessAnimation(MDFloatLayout):
    def play(self):
        self._initalize_circ()
        self._initialize_tick()

        anim = Animation(
            angle_start=self.angle_start, angle_end=-51, t="in_quad", d=0.2
        )
        anim.bind(on_complete=self._intermediate)
        anim.stop_all(self)
        anim.start(self)

    def _intermediate(self, wid, ins):
        anim = Animation(angle_start=-51, angle_end=-51, t="out_quad", d=0.15)
        anim &= self._tick_animation()
        anim.stop_all(self)
        anim.start(self)

    def _tick_animation(self):
        x = self.ids.box_layout.center_x
        y = self.ids.box_layout.center_y

        tick_props = ["tick_x2", "tick_y2", "tick_x3", "tick_y3"]
        tick_vals = [x - dp(7), y - dp(10), x - dp(7), y - dp(10)]
        anim = Animation(**dict(zip(tick_props, tick_vals)), d=0.15)

        tick_props = ["tick_x1", "tick_y1", "tick_x3", "tick_y3"]
        tick_vals = [x - dp(20), y + dp(8), x + dp(30), y + dp(15)]
        anim += Animation(**dict(zip(tick_props, tick_vals)), d=0.2 / 10)

        tick_vals = [x - dp(7), y - dp(10), x + dp(30) + 12, y + dp(15) + 12]
        anim += Animation(**dict(zip(tick_props, tick_vals)), d=0.2 / 6)

        tick_vals = [x - dp(20), y + dp(8), x + dp(30), y + dp(15)]
        anim += Animation(**dict(zip(tick_props, tick_vals)), d=0.2 / 6)

        return anim

    def _initalize_circ(self):
        self.angle_start = 140
        self.angle_end = 140

    def _initialize_tick(self):
        x = self.ids.box_layout.center_x
        y = self.ids.box_layout.center_y

        self.tick_x1 = x - dp(33)
        self.tick_y1 = y + dp(28)

        self.tick_x2 = self.tick_x1
        self.tick_y2 = self.tick_y1

        self.tick_x3 = self.tick_x2
        self.tick_y3 = self.tick_y2
