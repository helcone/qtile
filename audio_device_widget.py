import os
from libqtile import bar, hook, qtile
from libqtile.widget import base

import os
from libqtile import qtile

def choose_audio_device():
    # Get a list of all audio devices
    devices = os.popen("pactl list short sinks").read().splitlines()

    # Create a menu with all the audio devices
    menu_items = []
    for device in devices:
        device_name = device.split()[1]
        menu_items.append(device_name)

    # Show the menu and let the user choose an audio device
    menu_str = '\n'.join(menu_items)
    chosen_device = os.popen(f"echo \"{menu_str}\" | dmenu -i -p 'Choose an audio device:'").read().strip()

    # Set the chosen audio device as the default
    os.system(f"pactl set-default-sink {chosen_device}")

class AudioDeviceWidget(base._TextBox):
    def __init__(self, **config):
        base._TextBox.__init__(self, "Audio Device", **config)

    def button_press(self, x, y, button):
        if button == 1:
            choose_audio_device()
