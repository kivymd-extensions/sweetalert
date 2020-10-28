# Sweet Alert

<img align="left" width="128" src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sweetalert-logo.png"/>

### Beautiful, responsive, customizable
### and accessible popup replacement.

See SweetAlert [documentation](https://raw.githack.com/HeaTTheatR/KivyMD-data/master/sweetalert-doc/unincluded/sweetalert/sweetalert/index.html)


### Usage

```python
from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
#:import SweetAlert kivymd.components.sweetalert.SweetAlert


MDScreen:

    MDRaisedButton:
        text: "EXAMPLE"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release:
            SweetAlert(window_control_buttons=["mac-style"]).fire("Any fool can use a computer!")
"""


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()
```

<p align="center">
  <a href="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/preview-sweet-alert-example.png">
    <img width="500" src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/preview-sweet-alert-example.png" title="Preview sweet alert example">
  </a>
</p>

### Installation

```bash
pip install kivymd-components
componemts install sweetalert
```

## Usage with Buildozer

For now we cannot specify dependencies in the `bulldozer.spec` specification file in the `garden_requirements` 
(for example, like `components_requirements`) parameter. Instead, you must navigate to the root directory of your project,
where the bulldozer.spec file is located, and issue the command:

```bash
pip install kivymd-components
components install --app sweetalert
```

The component package will be installed locally in your project. Remember to import a package of components as follows:

```python
from kivymd.components.sweetalert import SweetAlert
```

### Dependencies

- [Kivy](https://github.com/kivy/kivy) >= 1.10.1 ([Installation](https://kivy.org/doc/stable/gettingstarted/installation.html))
- [KivyMD](https://github.com/kivymd/KivyMD) >= 0.104.2 (`pip install https://github.com/kivymd/KivyMD/archive/master.zip
`)
- [Python 3.6+](https://www.python.org/) _(Python 2 not supported)_

### Run demo

```batch
git clone git@github.com:kivymd-components/sweetalert.git
cd sweetalert/demo
python main.py
```

<p align="center">
  <a href="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/preview-sweet-alert.gif">
    <img width="600" src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/preview-sweet-alert.gif" title="Preview sweet alerts">
  </a>
</p>

### Support

If you need assistance or you have a question, you can ask for help on our mailing list:

- **Discord server:** https://discord.gg/fS7yTeq
- _Email:_ kivydevelopment@gmail.com
