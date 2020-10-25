import ast

from kivy.lang import Builder
from kivy.loader import Loader
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp

from sweetalert import SweetAlert

KV = """
# Do not delete this imports.
# These imports are needed to execute the command `exec(root.example_text)`
#:import ast ast
#:import requests requests
#:import threading threading
#:import Clock kivy.clock.Clock
#:import MDRectangleFlatIconButton kivymd.uix.button.MDRectangleFlatIconButton
#:import MDRaisedButton kivymd.uix.button.MDRaisedButton

#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import Clipboard kivy.core.clipboard.Clipboard
#:import PythonLexer pygments.lexers.python.PythonLexer
#:import SweetAlert sweetalert.SweetAlert
#:import toast kivymd.toast.toast


<ItemPreview>
    size_hint_y: None

    RelativeLayout:

        CodeInput:
            lexer: PythonLexer()
            style: "monokai"
            background_color: app.theme_cls.bg_darkest
            text: root.example_text
            selection_color: app.selection_color

        MDRectangleFlatButton:
            text: "COPY TO BUFFER"
            on_release:
                Clipboard.copy(root.example_text)
                toast("Copied to clipboard")

    RelativeLayout:

        FitImage:
            source: root.path_to_preview_image

        MDRectangleFlatButton:
            text: "RUN EXAMPLE"
            on_release: exec(root.example_text)


ScrollView:

    MDList:
        id: box
        padding: "4dp"
        spacing: "4dp"
        
        #MDFlatButton:
        #    on_release: app.show_confirmation_dialog2()
"""


class ItemPreview(BoxLayout):
    example_text = StringProperty()
    path_to_preview_image = StringProperty()


class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        selection_color = self.theme_cls.primary_light
        selection_color[-1] = 0.5
        self.selection_color = selection_color
        Loader.loading_image = "data/loader.gif"
        return Builder.load_string(KV)

    def on_start(self):
        data = ast.literal_eval(open(f"{self.directory}/example_data.json").read())
        for i in range(len(data)):
            if i == 8 or i == 9:
                height = "560dp"
            elif i == 13:
                height = "800dp"
            else:
                height = "280dp"
            self.root.ids.box.add_widget(
                ItemPreview(
                    example_text=data[i],
                    path_to_preview_image=f"data/{i}.png",
                    height=height,
                )
            )

    def show_confirmation_dialog2(self):
        SweetAlert(window_control_buttons=["mac-style"]).fire(
            'Submit your Github username',
        )


Example().run()
