from libqtile import bar, layout, extension, hook
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration, base
from libqtile.lazy import lazy
from libqtile.config import Key, Click, Drag, KeyChord, ScratchPad, DropDown
from libqtile.utils import guess_terminal
from libqtile.config import Click, Drag, Group, Match, Screen
from libqtile.dgroups import simple_key_binder
from libqtile import hook, qtile
from modules.keys import keys
from audio_device_widget import AudioDeviceWidget

@hook.subscribe.startup_once
def autostart():
    # Set the GDK_BACKEND environment variable to "x11"
    os.environ["GDK_BACKEND"] = "x11"


# Set personal variables
mod = "mod4"
alt = "mod1"
terminal = guess_terminal()
font = "Fira Code Nerd Font"
groups = [
        Group("🛡️"),
        Group("📝🔍",
                layout="monadtall"
             ),
        Group("🎮📺"),
        Group("🏋️🏃"),
        Group("🌐🕵️")
        ]

layout_theme = {
        "border_width": 2,
        "margin": 8,
        }

layouts = [
    # Try more layouts by unleashing below layouts.
     layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], **layout_theme),
     layout.TreeTab(
         previous_on_rm=True,
         **layout_theme),
     layout.Stack(num_stacks=2, **layout_theme),
     #layout.RatioTile(**layout_theme),
     #layout.Bsp(**layout_theme),
     #layout.Matrix(**layout_theme),
     #layout.MonadTall(**layout_theme),
     #layout.MonadWide(**layout_theme),
     #layout.Tile(**layout_theme),
     #layout.VerticalTile(**layout_theme),
     layout.Max(),
     #layout.Zoomy(),
]
# Power line decorations
powerline = {
    "decorations": [
        PowerLineDecoration()
    ]
}

widget_defaults = dict(
    font="FiraCode Nerd Font",
    fontsize=14,
    background="#292d3e",
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
        widget.Notify(
            max_chars=14,
            default_timeout=20,
            scroll=True,
            background=color_orange,
        ),
        widget.Prompt(
            max_chars=150,
            background=color_orange
        ),
        widget.Pomodoro(
            background=color_yellow,
            color_active='#333333',
            length_long_break=25,
            length_pomodori=25,
            length_short_break=5,
            prefix_active=' ',
            prefix_break='  ',
            prefix_inactive=' Pomodoro',
            prefix_long_break='  ',
            **powerline
        ),
        widget.Wallpaper(
            label=' Wallpaper',
            random_selection=True,
            fontsize=15,
            background=color_blue,
            option='fill',
            **powerline
        ),
        widget.Battery(
            padding=4,
            full_char='',
            discharge_char='',
            charge_char='',
            update_interval=15,
            background=color_green,
            **powerline
        ),
        widget.Wlan(
            format=' {essid} {percent:1.0%}',
            disconnected_message='睊',
            background=color_blue,
            **powerline
        ),
        widget.TextBox(
            '',
            padding=0,
            background=color_gray
        ),
        widget.CurrentLayout(
            padding=2,
            background=color_gray,
            **powerline
        ),
        widget.Clock(
            format=' %I:%M %p',
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
        )
    ]

    return widgets_list


def init_widget_screen1():
    widgets_screen1 = init_widget_list()
    return widgets_screen1
def init_widget_screen2():
    widgets_screen2 = init_widget_list()
    del widgets_screen2[-3:]
    return widgets_screen2

screens = [
    Screen(top=bar.Bar(widgets=init_widget_screen1(), size=24,)),
    Screen(top=bar.Bar(widgets=init_widget_screen2(), size=24,)),
]

dgroups_key_binder = simple_key_binder("mod4")
dgroups_app_rules = []  # type: list


# Define scratchpads
groups.append(ScratchPad('scratchpad', [
    DropDown("term", "alacritty --class=scratch", width=0.4, height=0.8, x=0.3, y=0.1, opacity=0.9),
    DropDown("ranger", "alacritty --class=ranger -e ranger", width=0.6, height=0.8, x=0.2, y=0.1, opacity=0.9),
    DropDown("cmus", "alacritty --class=cmus -e cmus", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown("keepass", "keepassxc", width=0.4, height=0.8, x=0.3, y=0.1, opacity=0.9),
    DropDown("notes", "flatpak run md.obsidian.Obsidian", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1, matches=[Match(wm_class=["obsidian"])]),
    DropDown("firefox", "firefox", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1, on_focus_lost_hide=False),
    DropDown("chrome", "flatpak run com.google.Chrome", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1, on_focus_lost_hide=False),
    DropDown("zathura", "zathura", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("whatsapp", "/opt/whatsdesk/whatsdesk", width=0.4, height=0.8, x=0.3, y=0.1, opacity=1),
    DropDown("ringcentral", "ringcentral-community-app", width=0.45, height=0.8, x=0.3, y=0.1, opacity=1),
    DropDown("nvim", "alacritty --class=nvim -e nvim", width=0.4, height=0.8, x=0.3, y=0.1, opacity=0.9),
    DropDown("bluetuith", "alacritty --class=bluetuith -e bluetuith", width=0.4, height=0.8, x=0.3, y=0.1, opacity=0.9),
    DropDown("android", "scrcpy -S", width=0.2, height=0.8, x=0.4, y=0.1, opacity=1, on_focus_lost_hide=False),
    DropDown("keys", "alacritty --class=keys -e 'qtilekeys | less'", width=0.2, height=0.8, x=0.4, y=0.1, opacity=1, on_focus_lost_hide=False)
]))

follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="Tor Browser"),  # tor browser to avoid fingerprinting 
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Installation"),
        Match(title="Live Caption"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
