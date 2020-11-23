"""
API
===

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    #:import SweetAlert kivymd_extensions.sweetalert.SweetAlert


    MDScreen:

        MDRaisedButton:
            text: "EXAMPLE"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: SweetAlert(window_control_buttons="mac-style").fire("Message!")
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/preview-sweet-alert-example.png
    :align: center
"""

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    OptionProperty,
    NumericProperty,
    ListProperty,
    BooleanProperty, ObjectProperty,
)
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex

from kivymd.font_definitions import theme_font_styles
from kivymd.material_resources import DEVICE_TYPE
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.card import MDSeparator
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.utils.fitimage import FitImage

from kivymd_extensions.sweetalert.animation import FailureAnimation, OthersAnimation, SuccessAnimation

Builder.load_string(
    """
<SweetAlertLabel>
    halign: "center"
    size_hint_y: None
    height: self.texture_size[1]
    markup: True
"""
)


class SweetAlert(MDDialog):
    animation_type = OptionProperty("pulse", options=("pulse"))
    """
    Dialog appearance animation type. Available options are: `'pulse'`.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-anim-pulse.gif
        :align: center

    :attr:`animation_type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'pulse'`.
    """

    font_style_title = OptionProperty("H4", options=theme_font_styles)
    """
    Dialog title style.

    .. code-block:: python

        SweetAlert(
            window_control_buttons="mac-style",
            font_style_title="H4",
        ).fire("Title", "Message!")

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-title-style.png
        :align: center

    :attr:`font_style_title` is an :class:`~kivy.properties.OptionProperty`
    and defaults to attr:`~kivymd.font_definitions.theme_font_styles`
    """

    font_style_text = OptionProperty("H6", options=theme_font_styles)
    """
    Dialog text style.

    .. code-block:: python

        SweetAlert(
            window_control_buttons="mac-style",
            font_style_text="H4",
        ).fire("Title", "Message!")

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-text-style.png
        :align: center

    :attr:`font_style_text` is an :class:`~kivy.properties.OptionProperty`
    and defaults to attr:`~kivymd.font_definitions.theme_font_styles`
    """

    font_style_footer = OptionProperty("H6", options=theme_font_styles)
    """
    Dialog footer style.

    .. code-block:: python

        SweetAlert(
            window_control_buttons="mac-style",
            font_style_footer="H4",
        ).fire("Title", "Message!", "Footer")

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-text-footer.png
        :align: center

    :attr:`font_style_footer` is an :class:`~kivy.properties.OptionProperty`
    and defaults to attr:`~kivymd.font_definitions.theme_font_styles`
    """

    font_size_button = NumericProperty("16sp")
    """
    Button font size.

    .. code-block:: python

        SweetAlert(
            window_control_buttons="mac-style",
            font_size_button="24sp",
        ).fire("Message!")

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-size-button.png
        :align: center

    :attr:`font_size_button` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'16sp'`.
    """

    color_button = ListProperty()
    """
    Button color.

    .. code-block:: python

        SweetAlert(
            window_control_buttons="mac-style",
            color_button=(1, 0, 1, 1),
        ).fire("Message!")

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-color-button.png
        :align: center

    :attr:`color_button` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    text_color_button = ListProperty()
    """
    Button text color.

    .. code-block:: python

        SweetAlert(
            window_control_buttons="mac-style",
            text_color_button=(1, 0, 0, 1),
        ).fire("Message!")

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-text-color-button.png
        :align: center

    :attr:`text_color_button` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    position = OptionProperty(
        "center",
        options=("center", "top-left", "top-right", "bottom-left", "bottom-right"),
    )
    """
    Dialog position. Available options are: `'center'`, `'top-left'`, `'top-right'`,
    `'bottom-left'`, `'bottom-right'`.

    .. code-block:: python

        SweetAlert(
            window_control_buttons="mac-style",
            position="top-right",
        ).fire("Message!")

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-top-right.png
        :align: center

    :attr:`position` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'center'`.
    """

    window_control_buttons = OptionProperty(None, options=["close", "mac-style"], allownone=True)
    """
    Type of buttons of window header.

    .. code-block:: python

        SweetAlert(window_control_buttons="mac-style").fire("Message!")

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-window-control-buttons.png
        :align: center

    .. code-block:: python

        SweetAlert(window_control_buttons="close").fire("Message!")

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-close.png
        :align: center

    :attr:`window_control_buttons` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    window_control_callback = ObjectProperty()
    """
    Callback for buttons of window header.

    .. code-block:: python

        SweetAlert(
            window_control_buttons="close",
            window_control_callback=self.callback,
        ).fire("Message!")

    .. code-block:: python

        def callback(self, instance_button):
            print(instance_button)

    :attr:`window_control_callback` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    timer = NumericProperty(0)
    """
    Dialog closes automatically by timer.

    :attr:`timer` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    request = BooleanProperty(False)

    _timer = 0
    _created = False

    def __init__(self, **kwargs):
        self.type = "custom"
        if hasattr(self, "overlay_color"):
            self.overlay_color = (0, 0, 0, 0)
        else:
            self.background_color = (0, 0, 0, 0)
        # A box in which text, buttons and icons will be placed of window.
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

        # Creating and adding control buttons (close/collapse/expand)
        # in the window header.
        if self.window_control_buttons:
            button_box = RelativeLayout()
            self.add_widget(button_box)
            if self.window_control_buttons == "close":
                button = MDIconButton(
                    icon="close",
                    pos_hint={"top": 1},
                    x=self.width - self.content_cls.padding[0] - dp(32),
                )
                if self.window_control_callback:
                    button.bind(on_release=self.window_control_callback)
                button_box.add_widget(button)
            elif self.window_control_buttons == "mac-style":
                # Color and padding of buttons.
                data = {"#eb5b53": 8, "#f5bc48": 28, "#64ca43": 48}
                for color in data:
                    button = MacOSWindowHeaderButton(
                        text_color=get_color_from_hex(color),
                        x=data[color],
                    )
                    if self.window_control_callback:
                        button.bind(on_release=lambda x=button: self.window_control_callback(x))
                    button_box.add_widget(button)

        Window.bind(on_resize=lambda *args: self.dismiss())

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
        """
        Arguments:
        ----------

        `title`

        .. code-block:: python

            SweetAlert().fire("Title")

        .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-title.png
            :align: center

        `text`

        .. code-block:: python

            SweetAlert().fire("Title", "Text")

        .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-title-text.png
            :align: center

        Or without title:

        .. code-block:: python

            SweetAlert().fire(text="Text")

        .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-text.png
            :align: center

        `footer`

        .. code-block:: python

            SweetAlert().fire(text="Message", footer="Footer text")

        .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-footer.png
            :align: center

        `image`

        .. code-block:: python

            SweetAlert().fire(text="Message", image="https://picsum.photos/600/400/?blur")

        .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-image.png
            :align: center

        `input`

        .. code-block:: python

            SweetAlert().fire(text="Message", input="Input Email")

        .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-input.png
            :align: center

        Or combine parameters:

        .. code-block:: python

            SweetAlert().fire(
                text="Message",
                image="https://picsum.photos/600/400/?blur",
                input="Input Email",
            )

        .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-combine.png
            :align: center

        `buttons`

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.button import MDRaisedButton, MDFlatButton

            from kivymd_extensions.sweetalert import SweetAlert

            KV = '''
            MDScreen:

                MDRaisedButton:
                    text: "EXAMPLE"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release: app.show_dialog()
            '''


            class Test(MDApp):
                def build(self):
                    return Builder.load_string(KV)

                def show_dialog(self):
                    button_ok = MDRaisedButton(
                        text='OK',
                        font_size=16,
                        on_release=self.callback,
                    )
                    button_cancel = MDFlatButton(
                        text='CANCEL',
                        font_size=16,
                        on_release=self.callback,
                    )
                    self.alert = SweetAlert()
                    self.alert.fire(
                        'Your public IP', buttons=[button_ok, button_cancel],
                    )

                def callback(self, instance_button):
                    print(self.alert, instance_button)


            Test().run()

        .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-buttons.png
            :align: center

        `type`:

        ``success``

        .. code-block:: python

            SweetAlert().fire('That thing is still around?', type='success')

        .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-success.png
            :align: center

        ``failure``

        .. code-block:: python

            SweetAlert().fire('That thing is still around?', type='failure')

        .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-failure.png
            :align: center

        ``warning``

        .. code-block:: python

            SweetAlert().fire('That thing is still around?', type='warning')

        .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-warning.png
            :align: center

        ``info``

        .. code-block:: python

            SweetAlert().fire('That thing is still around?', type='info')

        .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-info.png
            :align: center

        ``question``

        .. code-block:: python

            SweetAlert().fire('That thing is still around?', type='question')

        .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweet-alert-question.png
            :align: center
        """

        if self._created:
            self._open(0)
            return

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

    def update_width(self, *args):
        """Updates window width."""

        self.width = max(
            self.height + dp(48),
            min(
                dp(560) if DEVICE_TYPE == "desktop" else dp(280),
                Window.width - dp(48),
            ),
        )

        # Updates button "close" position.
        for widget in self.children:
            if isinstance(widget, RelativeLayout):
                if len(widget.children) == 1 and isinstance(
                    widget.children[0], MDIconButton
                ):
                    if widget.children[0].icon == "close":
                        widget.children[0].x = (
                            self.width - self.content_cls.padding[0] - dp(32)
                        )
                        break

    def on_request(self, instance, value):
        """Adds a ``MDSpinner`` to the dialog."""

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

    def add_input(self, input):
        if input:
            field = MDTextFieldRect(
                size_hint=(None, None),
                size=(self.width - dp(40), dp(30)),
                pos_hint={"center_y": 0.5, "center_x": 0.5},
            )
            if isinstance(input, str):
                field.hint_text = input
            self.content_cls.add_widget(field)

    def check_timer(self, timer, interval=1):
        self._timer += 1
        if self._timer > self.timer:
            Clock.unschedule(self.check_timer)
            self._timer = 0
            self.dismiss()

    def add_image(self, image, height_image):
        self.content_cls.padding[1] = 0
        self.content_cls.add_widget(
            FitImage(source=image, size_hint_y=None, height=height_image)
        )

    def add_footer(self, footer):
        if footer:
            self.content_cls.add_widget(MDSeparator())
            footer_text = SweetAlertLabel(
                text=footer,
                font_style=self.font_style_footer,
                theme_text_color="Custom",
                text_color=get_color_from_hex("#429cf4"),
            )
            self.content_cls.add_widget(footer_text)

    def add_buttons(self, buttons):
        if not buttons:
            button = MDRaisedButton(
                text="OK",
                pos_hint={"center_x": 0.5},
                font_size=self.font_size_button,
                on_release=lambda x: self.dismiss(),
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
            label_text = SweetAlertLabel(
                text=text,
                font_style=self.font_style_text,
                theme_text_color="Custom",
                text_color=self.theme_cls.disabled_hint_text_color,
            )
            self.content_cls.add_widget(label_text)

    def add_title(self, title):
        if title:
            label_title = SweetAlertLabel(text=title, font_style=self.font_style_title)
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
        self._created = True

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


class SweetAlertLabel(MDLabel):
    """Base class for dialog labels."""


class MacOSWindowHeaderButton(MDIconButton):
    """
    The base class of buttons (close/collapse/expand) that will be placed
    in the window header.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_font_size = "14sp"
        self.theme_text_color = "Custom"
        self.pos_hint = {"top": 1}
        self.ripple_scale = 0.7
