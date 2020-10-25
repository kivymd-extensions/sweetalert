# Written by shashi278
#
# Refer:
#    https://github.com/shashi278/AndroidView/blob/master/demo/failure_anim.gif
#    https://github.com/shashi278/AndroidView/blob/master/demo/failure_anim.py

from kivy.lang import Builder
from kivy.animation import Animation
from kivy.metrics import dp

from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_string(
    """
<FailureAnimation>:
    ma_bg_color: 1, 1, 1, 0
    angle_start_l: 0
    angle_end_l: 0
    angle_start_r: 0
    angle_end_r: 0
    cross_x1_l: 0 # box_layout.center_x - dp(33)
    cross_y1_l: 0 # box_layout.center_y + dp(30)
    cross_x2_l: 0 # box_layout.center_x + dp(24)
    cross_y2_l: 0 # box_layout.center_y - dp(23)
    cross_x1_r: 0 # box_layout.center_x + dp(24)
    cross_y1_r: 0 # box_layout.center_y + dp(23)
    cross_x2_r: 0 # box_layout.center_x - dp(24)
    cross_y2_r: 0 # box_layout.center_y - dp(23)

    MDBoxLayout:
        id: box_layout
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: None, None
        height: 100
        width: 100
        ma_bg_color: 1, 1, 1, 0

        canvas:
            Color:
                rgba: 1, 0, 0, .2
            SmoothLine:
                circle: self.center_x, self.center_y, self.width / 2 - dp(5), 0,360
                width: dp(2.25)
            Color:
                rgba: 1, 0, 0, 1
            SmoothLine:
                circle: self.center_x, self.center_y, self.width / 2 - dp(5), root.angle_start_l, root.angle_end_l
                width: dp(2.25)
                cap: "square"
            SmoothLine:
                circle: self.center_x, self.center_y, self.width / 2 - dp(5), root.angle_start_r, root.angle_end_r
                width: dp(2.25)
                cap: "square"
            SmoothLine:
                points: root.cross_x1_l, root.cross_y1_l, root.cross_x2_l, root.cross_y2_l
                width: dp(2.25)
                cap: "square"
            SmoothLine:
                points: root.cross_x1_r, root.cross_y1_r, root.cross_x2_r, root.cross_y2_r
                width: dp(2.25)
                cap: "square"
"""
)


class FailureAnimation(MDFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def play(self):
        self._initalize_circ()
        self._initialize_cross()

        anim = Animation(
            angle_start_l=self.angle_start_l,
            angle_end_l=315,
            angle_start_r=self.angle_start_r,
            angle_end_r=45,
            # t='in_quad',
            d=0.2,
        )
        anim.bind(on_complete=self._intermediate)
        anim.stop_all(self)
        anim.start(self)

    def _intermediate(self, wid, ins):
        anim = Animation(
            angle_start_l=315,
            angle_end_l=315,
            angle_start_r=45,
            angle_end_r=45,
            # t='out_quad',
            d=0.15,
        )
        anim &= self._cross_animation()
        anim.stop_all(self)
        anim.start(self)

    def _cross_animation(self):
        x = self.ids.box_layout.center_x
        y = self.ids.box_layout.center_y

        cross_props = ["cross_x2_r", "cross_y2_r", "cross_x2_l", "cross_y2_l"]
        cross_vals = [x - dp(24), y - dp(23), x + dp(24), y - dp(23)]
        anim = Animation(**dict(zip(cross_props, cross_vals)), d=0.15)

        cross_props = [
            "cross_x1_l",
            "cross_y1_l",
            "cross_x2_l",
            "cross_y2_l",
            "cross_x1_r",
            "cross_y1_r",
            "cross_x2_r",
            "cross_y2_r",
        ]

        cross_vals = [
            x - dp(24) + 13,
            y + dp(23) - 13,
            x + dp(24) + 17,
            y - dp(23) - 17,
            x + dp(24) - 13,
            y + dp(23) - 13,
            x - dp(24) - 17,
            y - dp(23) - 17,
        ]
        anim += Animation(**dict(zip(cross_props, cross_vals)), d=0.2 / 6)

        cross_vals = [
            x - dp(24),
            y + dp(23),
            x + dp(24),
            y - dp(23),
            x + dp(24),
            y + dp(23),
            x - dp(24),
            y - dp(23),
        ]
        anim += Animation(**dict(zip(cross_props, cross_vals)), d=0.2 / 6)

        return anim

    def _initalize_circ(self):
        self.angle_start_l = 180
        self.angle_end_l = 180

        self.angle_start_r = 180
        self.angle_end_r = 180

    def _initialize_cross(self):
        x = self.ids.box_layout.center_x
        y = self.ids.box_layout.center_y

        self.cross_x1_l = x - dp(33)
        self.cross_y1_l = y + dp(30)
        self.cross_x2_l = self.cross_x1_l
        self.cross_y2_l = self.cross_y1_l

        self.cross_x1_r = x + dp(33)
        self.cross_y1_r = y + dp(30)
        self.cross_x2_r = self.cross_x1_r
        self.cross_y2_r = self.cross_y1_r
