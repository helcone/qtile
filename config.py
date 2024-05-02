from libqtile import bar, layout, qtile 
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
 
# Testing qtile_extras
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration, base

#Personal Modules
from modules.keys import keys
from modules.personal_widgets import init_widget_list

mod = "mod4"
alt = "mod1"
terminal = guess_terminal()
font = "Fira Code Nerd Font"


# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

## Power Line decoration
#powerline = {
#        "decorations": [
#            PowerLineDecoration()
#            ]
#        }
#
#
#widget_defaults = dict(
#    font="FiraCode Nerd Font",
#    fontsize=12,
#    padding=3,
#)
#extension_defaults = widget_defaults.copy()
#
#def init_widget_list():
#    # Color Variables
#    color_yellow = '#FFFF00'
#    color_blue = '#0047AB'
#    color_green = '#007F5F'
#    color_gray = '#B1B2B8'
#    color_cyan = '#00A3CC'
#    color_orange = '#fe640b'
#    color_darkgray = '#4c4f56'
#
#    widgets_list = [
#            widget.CurrentLayout(),
#            widget.GroupBox(),
#            widget.Prompt(),
#            widget.WindowName(),
#            widget.Chord(
#                chords_colors={
#                    "launch": ("#ff0000", "#ffffff"),
#                    },
#                name_transform=lambda name: name.upper(),
#                ),
#            widget.Clock(
#                format=" %I:%M %p",
#                background=color_cyan,
#                **powerline
#                ),
#            widget.StatusNotifier(),
#            widget.QuickExit(),
#            ]
#    return widgets_list

def init_widget_screen1():
    widgets_screen1 = init_widget_list()
    return widgets_screen1
def init_widget_screen2():
    widgets_screen2 = init_widget_list()
#    del widgets_screen2[-5:]
    return widgets_screen2

screens = [
    Screen(top=bar.Bar(widgets=init_widget_screen1(), size=24,)),
    Screen(top=bar.Bar(widgets=init_widget_screen2(), size=24,)),
]
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

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
