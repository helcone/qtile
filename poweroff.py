import subprocess
from libqtile.widget import base

class PowerOffButton(base._TextBox):
    def __init__(self, **config):
        super().__init__(text="⏻", **config)

    def button_press(self, x, y, button):
        if button == 1:
            subprocess.call(["systemctl", "poweroff"])
        elif button == 2:
            subprocess.call(["systemctl", "suspend"])
