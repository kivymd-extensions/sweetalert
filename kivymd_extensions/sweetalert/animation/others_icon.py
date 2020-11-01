from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel

Builder.load_string(
    """
<OthersAnimation>:
    md_bg_color: 1, 1, 1, 0
    angle_start: 0
    angle_end: 0

    MDBoxLayout:
        id: box_layout
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: None, None
        height: 100
        width: 100
        md_bg_color: 1, 1, 1, 0

        canvas:
            Color:
                rgba: root.color
            Line:
                circle: self.center_x, self.center_y, self.width / 2 - dp(5), 0,360
                width: dp(2.25)
            Rectangle:
                texture: root.char_texture.texture
                size: root.char_texture.texture_size
                pos:
                    self.center_x - root.char_texture.texture_size[0] / 2, \
                    self.center_y - root.char_texture.texture_size[1] / 2, 
"""
)


class OthersAnimation(MDFloatLayout):
    char = StringProperty("!")
    color = ListProperty((0, 1, 0, 1))

    def __init__(self, **kwargs):
        self.char_texture = MDLabel(
            font_style="H2",
            halign="center",
            text=self.char,
            theme_text_color="Custom",
            text_color=self.color,
        )
        super().__init__(**kwargs)

    def on_color(self, instance, value):
        self.char_texture.text_color = value

    def on_char(self, instance, value):
        self.char_texture.text = value
