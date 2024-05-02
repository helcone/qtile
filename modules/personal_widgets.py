from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration, base
from audio_device_widget import AudioDeviceWidget
from poweroff import PowerOffButton

# Power Line decoration
powerline = {
        "decorations": [
            PowerLineDecoration()
            ]
        }

widget_defaults = dict(
        font="FiraCode Nerd Font",
        fontsize=14,
        background="#292d3e"
        )
extension_defaults = widget_defaults.copy()

def init_widget_list():
    # Define color variables
    color_yellow = '#FFFF00'
    color_blue = '#0047AB'
    color_green = '#007F5F'
    color_gray = '#B1B2B8'
    color_cyan = '#00A3CC'
    color_orange = '#fe640b'
    color_darkgray = '#4c4f56'

    # Define widget list
    widgets_list = [
        widget.GroupBox(
            fontsize=16,
            highlight_method='line',
            padding=3
        ),
        widget.Cmus(),
        widget.WindowName(**powerline),
        # Notification form qtile
#        widget.Notify(
#            max_chars=150,
#            default_timeout=20,
#            scroll=True,
#            background=color_orange,
#        ),
        widget.Prompt(
            max_chars=150,
            background=color_orange
        ),
        widget.Pomodoro(
            background=color_yellow,
            color_active='#333333',
            color_break='#1e233f',
            length_long_break=30,
            length_pomodori=30,
            length_short_break=10,
            prefix_active='🍎 ',
            prefix_break='🚰 ',
            prefix_inactive='🍏 Pomodoro',
            prefix_long_break='🚰🚶 ',
            **powerline
        ),
        widget.OpenWeather(
            background=color_cyan,
            app_key='02fd2f5789b72f9992314389e2098196',
            location='Mérida,MX',
            **powerline
            ),
        widget.Wallpaper(
            label='  Wallpaper',
            random_selection=True,
            fontsize=15,
            background=color_blue,
            option='fill',
            **powerline
        ),
        widget.Wlan(
            format=' {essid} {percent:1.0%}',
            disconnected_message='睊',
            background=color_green,
            **powerline
        ),
        widget.TextBox(
            '  ',
            padding=0,
            background=color_gray
        ),
        widget.CurrentLayout(
            padding=2,
            background=color_gray,
            **powerline
        ),
        widget.Clock(
            format='🕑 %I:%M %p',
            background=color_cyan,
            **powerline
        ),
        widget.Systray(
            padding=1,
            background=color_darkgray
        ),
        AudioDeviceWidget(
                background=color_darkgray
                ),
        widget.Volume(
            background=color_darkgray
        ),
        widget.KeyboardLayout(
            background=color_darkgray,
            configured_keyboards=['us', 'latam']
        ),
        PowerOffButton()
    ]

    return widgets_list
