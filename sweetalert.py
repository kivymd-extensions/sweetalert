from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import OptionProperty, NumericProperty, ListProperty, \
    BooleanProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex

from kivymd.font_definitions import theme_font_styles
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.card import MDSeparator
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.utils.fitimage import FitImage

try:
    from .animation.failure_icon import FailureAnimation
    from .animation.others_icon import OthersAnimation
    from .animation.success_icon import SuccessAnimation
except ImportError:
    from animation.failure_icon import FailureAnimation
    from animation.others_icon import OthersAnimation
    from animation.success_icon import SuccessAnimation

Builder.load_string(
    """
<CustomLabel>
    halign: "center"
    size_hint_y: None
    height: self.texture_size[1]
    markup: True
"""
)


class CustomLabel(MDLabel):
    """Base class for dialog labels."""


class SweetAlert(MDDialog):
    animation_type = OptionProperty("pulse", options=("pulse"))
    """
    Dialog title style.

    Available options are: `'pulse'`.

    :attr:`animation_type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'pulse'`.
    """

    font_style_title = OptionProperty("H4", options=theme_font_styles)
    """
    Dialog title style.

    :attr:`font_style_title` is an :class:`~kivy.properties.OptionProperty`
    and defaults to attr:`~kivymd.font_definitions.theme_font_styles`
    """

    font_style_text = OptionProperty("H6", options=theme_font_styles)
    """
    Dialog text style.

    :attr:`font_style_text` is an :class:`~kivy.properties.OptionProperty`
    and defaults to attr:`~kivymd.font_definitions.theme_font_styles`
    """

    font_style_footer = OptionProperty("H6", options=theme_font_styles)
    """
    Dialog footer style.

    :attr:`font_style_footer` is an :class:`~kivy.properties.OptionProperty`
    and defaults to attr:`~kivymd.font_definitions.theme_font_styles`
    """

    font_size_button = NumericProperty("16sp")
    """
    Button font size.

    :attr:`font_size_button` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'16sp'`.
    """

    color_button = ListProperty()
    """
    Button color.

    :attr:`color_button` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `[]`.
    """

    text_color_button = ListProperty()
    """
    Button text color.

    :attr:`text_color_button` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `[]`.
    """

    position = OptionProperty(
        "center",
        options=("center", "top-left", "top-right", "bottom-left", "bottom-right"),
    )
    """
    Dialog position.

    Available options are: `'center'`, `'top-left'`, `'top-right'`,
    `'bottom-left'`, `'bottom-right'`.

    :attr:`position` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'center'`.
    """

    timer = NumericProperty(0)
    """
    Dialog closes automatically by timer.

    :attr:`timer` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    request = BooleanProperty(False)

    window_control_buttons = ListProperty()

    _timer = 0

    def __init__(self, **kwargs):
        self.type = "custom"
        if hasattr(self, "overlay_color"):
            self.overlay_color = (0, 0, 0, 0)
        else:
            self.background_color = (0, 0, 0, 0)
        self.content_cls = MDBoxLayout(
            adaptive_height=True,
            orientation="vertical",
            padding=("24dp", "68dp", "24dp", "24dp"),
            spacing="24dp",
        )
        self.opacity = 0
        self.bind(
            on_open={"pulse": self.anim_open_dialog_pulse}.get(self.animation_type),
            on_dismiss={"pulse": self.anim_close_dialog_pulse}.get(self.animation_type),
        )
        self._scale_x = 0
        self._scale_y = 0
        super().__init__(**kwargs)

        if self.window_control_buttons:
            button_box = RelativeLayout()
            self.content_cls.add_widget(button_box)
        for name_button in self.window_control_buttons:
            if name_button == "close":
                button_box.add_widget(
                    MDIconButton(
                        icon="close",
                        y=dp(-24),
                        x=self.width - (self.content_cls.padding[0] * 3) - dp(32),
                    )
                )
            if name_button == "mac-style":
                button_box.add_widget(
                    MDIconButton(
                        user_font_size="14sp",
                        y=self.content_cls.height - self.content_cls.padding[0] * 2,
                        theme_text_color="Custom",
                        text_color=get_color_from_hex("#eb5b53"),
                        x=-self.content_cls.padding[0] * 2 + dp(4),
                    )
                )
                button_box.add_widget(
                    MDIconButton(
                        user_font_size="14sp",
                        y=self.content_cls.height - self.content_cls.padding[0] * 2,
                        theme_text_color="Custom",
                        text_color=get_color_from_hex("#f5bc48"),
                        x=-self.content_cls.padding[0] * 2 + dp(4) + dp(14) * 1.5,
                    )
                )
                button_box.add_widget(
                    MDIconButton(
                        user_font_size="14sp",
                        y=self.content_cls.height - self.content_cls.padding[0] * 2,
                        theme_text_color="Custom",
                        text_color=get_color_from_hex("#64ca43"),
                        x=-self.content_cls.padding[0] * 2 + dp(4) + dp(14) * 3,
                    )
                )

    def on_request(self, instance, value):
        for widget in self.content_cls.children:
            if isinstance(widget, MDBoxLayout):
                widget.clear_widgets()
                self.content_cls.spacing = "12dp"
                self.content_cls.add_widget(
                    MDSpinner(
                        size_hint=(None, None),
                        size=("48dp", "48dp"),
                        pos_hint={"center_x": 0.5},
                    )
                )
                break

    def _align_center(self, *l):
        if self._window:
            if self.position == "top-left":
                self.pos = (10, Window.height - self.height - 10)
            elif self.position == "top-right":
                self.pos = (
                    Window.width - self.width - 10,
                    Window.height - self.height - 10,
                )
            elif self.position == "bottom-left":
                self.pos = (10, 10)
            elif self.position == "bottom-right":
                self.pos = (Window.width - self.width - 10, 10)
            else:
                self.center = self._window.center

    def fire(
        self,
        title="",
        text="",
        footer="",
        image="",
        height_image="200dp",
        input="",
        buttons=None,
        type="",
    ):
        if not image:
            self.add_icon(type)
        else:
            self.add_image(image, height_image)
        self.add_title(title)
        self.add_text(text)
        self.add_input(input)
        self.add_buttons(buttons)
        self.add_footer(footer)
        if self.timer:
            Clock.schedule_interval(self.check_timer, 1)
        Clock.schedule_once(self._open)

    def add_input(self, input):
        if input:
            self.content_cls.add_widget(
                MDTextFieldRect(
                    size_hint=(None, None),
                    size=(self.width - dp(40), dp(30)),
                    pos_hint={'center_y': .5, 'center_x': .5},
                )
            )

    def check_timer(self, timer, interval=1):
        self._timer += 1
        if self._timer > self.timer:
            Clock.unschedule(self.check_timer)
            self._timer = 0
            self.dismiss()

    def add_image(self, image, height_image):
        self.content_cls.add_widget(
            FitImage(source=image, size_hint_y=None, height=height_image)
        )

    def add_footer(self, footer):
        if footer:
            self.content_cls.add_widget(MDSeparator())
            footer_text = CustomLabel(
                text=footer,
                font_style=self.font_style_footer,
                theme_text_color="Custom",
                text_color=get_color_from_hex("#429cf4"),
            )
            self.content_cls.add_widget(footer_text)

    def add_buttons(self, buttons):
        if not buttons:
            button = MDRaisedButton(
                text="OK", pos_hint={"center_x": 0.5}, font_size=self.font_size_button
            )
            button.md_bg_color = (
                self.color_button if self.color_button else self.theme_cls.primary_color
            )
            button.text_color = (
                self.text_color_button if self.text_color_button else (0, 0, 0, 1)
            )
            self.content_cls.add_widget(button)
        else:
            box = MDBoxLayout(
                adaptive_size=True, spacing="12dp", pos_hint={"center_x": 0.5}
            )
            self.content_cls.add_widget(box)
            for button in buttons:
                box.add_widget(button)

    def add_text(self, text):
        if text:
            label_text = CustomLabel(
                text=text,
                font_style=self.font_style_text,
                theme_text_color="Custom",
                text_color=self.theme_cls.disabled_hint_text_color,
            )
            self.content_cls.add_widget(label_text)

    def add_title(self, title):
        if title:
            label_title = CustomLabel(text=title, font_style=self.font_style_title)
            self.content_cls.add_widget(label_title)

    def add_icon(self, type, char="", color=()):
        if type not in ("success", "failure", "question", "info", "warning"):
            type = ""
        if type == "success":
            self.content_cls.add_widget(SuccessAnimation())
        elif type == "failure":
            self.content_cls.add_widget(FailureAnimation())
        else:
            if type == "question":
                char = "?"
                color = get_color_from_hex("#7ea1af")
            elif type == "info":
                char = "i"
                color = get_color_from_hex("#55bce5")
            elif type == "warning":
                char = "!"
                color = get_color_from_hex("#edb481")
            if char and color:
                self.content_cls.add_widget(OthersAnimation(char=char, color=color))
        if type:
            self.content_cls.add_widget(Widget(size_hint_y=None, height="48dp"))
        else:
            self.content_cls.padding = ("24dp", "36dp", "24dp", "24dp")

    def anim_open_dialog_pulse(self, *args):
        anim = Animation(opacity=1, _scale_x=1, _scale_y=1, t="out_bounce", d=0.6)
        anim.start(self)
        # Starts the animation of the "failure" and "success" icons.
        for widget in self.content_cls.children:
            if isinstance(widget, (SuccessAnimation, FailureAnimation)):
                widget.play()

    def anim_close_dialog_pulse(self, *args):
        Animation(opacity=0, _scale_x=0, _scale_y=0, t="out_quad", d=0.6).start(self)

    def _open(self, interval):
        self.ids.container.height = self.content_cls.height
        self.open()
