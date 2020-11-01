# Sweet Alert

<img align="left" width="128" src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweetalert-logo.png"/>

Beautiful, responsive, customizable and accessible popup replacement.

## Installation

```bash
pip install kivymd_extensions.sweetalert
```

### Dependencies:

- [KivyMD](https://github.com/kivymd/KivyMD) >= 0.104.2 (currently master branch)
- [Kivy](https://github.com/kivy/kivy) >= 1.10.1 ([Installation](https://kivy.org/doc/stable/gettingstarted/installation.html))
- [Python 3.6+](https://www.python.org/)

## Documentation

See SweetAlert [documentation](https://raw.githack.com/HeaTTheatR/KivyMD-data/master/sweetalert-doc/unincluded/sweetalert/sweetalert/index.html).

### Usage

```python
from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
#:import SweetAlert kivymd_extensions.sweetalert.SweetAlert


MDScreen:

    MDRaisedButton:
        text: "EXAMPLE"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release:
            SweetAlert(window_control_buttons="mac-style").fire("Any fool can use a computer!")
"""


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    MainApp().run()
```

<p align="center">
  <a href="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/preview-sweet-alert-example.png">
    <img width="500" src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/preview-sweet-alert-example.png" title="Preview sweet alert example">
  </a>
</p>

## Examples

```bash
git clone https://github.com/kivymd-extensions/sweetalert.git
cd sweetalert
cd examples/full_example
python main.py
```

<p align="center">
  <a href="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/preview-sweet-alert.gif">
    <img width="600" src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/preview-sweet-alert.gif" title="Preview sweet alerts">
  </a>
</p>

### Support

If you need assistance or you have a question, you can ask for help on our mailing list:

- **Discord server:** https://discord.gg/wu3qBST
- _Email:_ kivydevelopment@gmail.com
