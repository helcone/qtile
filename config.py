import os
import re
import subprocess
from modules.personal_widgets import init_widget_list
from libqtile import bar, layout, extension, hook
from libqtile.lazy import lazy
from libqtile.config import Key, Click, Drag, KeyChord, ScratchPad, DropDown
from libqtile.utils import guess_terminal
from libqtile.config import Group, Match, Screen
from libqtile.dgroups import simple_key_binder
from libqtile import hook, qtile
from modules.keys import keys

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])
    if qtile.core.name == "x11":
        os.environ["GDK_BACKEND"] = "x11" # Set the GDK_BACKEND environment variable to "x11"
    elif qtile.core.name == "wayland":
        os.environ["GDK_BACKEND"] = "wayland"

# Set personal variables
mod = "mod4"
alt = "mod1"
terminal = guess_terminal()
font = "Agave Nerd Font"


#for vt in range(1,8):
#    keys.append(
#            Key(
#                ["control", "mod1"],
#                f"f{vt}",
#                lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
#                desc=f"Switch to VT{vt}",
#                )
#            )
#

groups = [
        Group("🌐",
              layout="treetab",
              ),
        Group("📝",
              layout="treetab"
              ),
        Group("🎮"),
        Group("📚",
              layout="columns"
              ),
        Group("󰆍")
        ]

layout_theme = {
        "border_width": 2,
        "margin": 2,
        }

layouts = [
        layout.Columns(
            border_focus_stack=["#d75f5f", "#8f3d3d"], **layout_theme),
        layout.TreeTab(
            sections = ["General", "Birkman", "Cursos", "Chats"],
            previous_on_rm=True,
            **layout_theme),
        layout.Stack(num_stacks=2, **layout_theme),
        #layout.RatioTile(**layout_theme),
        #layout.Bsp(**layout_theme),
        # layout.Matrix(**layout_theme),
        # layout.MonadTall(**layout_theme),
        # layout.MonadWide(**layout_theme),
        # layout.Tile(**layout_theme),
        # layout.VerticalTile(**layout_theme),
        # layout.Max(),
        # layout.Zoomy(),
]

def init_widget_screen1():
    widgets_screen1 = init_widget_list()
    return widgets_screen1
def init_widget_screen2():
    widgets_screen2 = init_widget_list()
    del widgets_screen2[-5:]
    return widgets_screen2

screens = [
    Screen(top=bar.Bar(widgets=init_widget_screen1(), size=24,)),
    Screen(top=bar.Bar(widgets=init_widget_screen2(), size=24,)),
]

dgroups_key_binder = simple_key_binder("mod4")
dgroups_app_rules = []  # type: list


# Define scratchpads
groups.append(ScratchPad('scratchpad', [
    DropDown("term", "alacritty --class=scratch",
             width=0.4, height=0.8, x=0.3, y=0.1, opacity=0.9),
    DropDown("ranger", "alacritty --class=ranger -e ranger",
             width=0.6, height=0.8, x=0.2, y=0.1, opacity=0.9),
    DropDown("cmus", "alacritty --class=cmus -e cmus",
             width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown("keepass", "keepassxc",
             width=0.4, height=0.8, x=0.3, y=0.1, opacity=0.9),
    DropDown("notes", "flatpak run md.obsidian.Obsidian",
             width=0.8, height=0.8, x=0.1, y=0.1, opacity=1,
             matches=[Match(wm_class=re.compile(r"^(obsidian)$"))]),
    DropDown("firefox", "firefox",
             width=0.8, height=0.8, x=0.1, y=0.1, opacity=1,
             on_focus_lost_hide=False),
    DropDown("chrome", "flatpak run com.google.Chrome",
             width=0.8, height=0.8, x=0.1, y=0.1, opacity=1,
             on_focus_lost_hide=False),
    DropDown("zathura", "zathura",
             width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("whatsapp", "/opt/whatsdesk/whatsdesk",
             width=0.55, height=0.8, x=0.25, y=0.1, opacity=1),
    DropDown("nvim", "alacritty --class=nvim -e nvim",
             width=0.4, height=0.8, x=0.3, y=0.1, opacity=0.9),
    DropDown("bluetuith", "alacritty --class=bluetuith -e bluetuith",
             width=0.4, height=0.8, x=0.3, y=0.1, opacity=0.9),
    DropDown("android", "scrcpy -S",
             width=0.2, height=0.8, x=0.4, y=0.1, opacity=1,
             on_focus_lost_hide=False),
    DropDown("keys", "alacritty --class=keys -e 'qtilekeys | less'",
             width=0.2, height=0.8, x=0.4, y=0.1, opacity=1,
             on_focus_lost_hide=False),
    DropDown("htop", "alacritty -e htop",
             height=0.5, width=0.5, x=0.25, y=0.25),
    DropDown("authy", "authy",
             height=0.4, width=0.8, x=0.3, y=0.1),
    DropDown("radeontop", "alacritty -e radeontop",
             height=0.5, width=0.5, x=0.25, y=0.25)
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
        Match(title="Picture-in-Picture"),
        Match(title="Live Caption")
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
