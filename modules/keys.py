from libqtile.lazy import lazy
from libqtile.config import Key, Click, Drag, KeyChord
from libqtile.utils import guess_terminal
from libqtile import extension, hook, qtile

mod = "mod4"
alt = "mod1"
terminal = guess_terminal()
# Sticky window

win_list = []
def stick_win(qtile):
    global win_list
    win_list.append(qtile.current_window)
def unstick_win(qtile):
    global win_list
    if qtile.current_window in win_list:
        win_list.remove(qtile.current_window)
@hook.subscribe.setgroup
def move_win():
    for w in win_list:
        w.togroup(qtile.current_group.name)

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "shift"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Tree tab controls
    Key([mod, "mod1"], "j", lazy.layout.move_up(), desc='Move up a section in treetab'),
    Key([mod, "mod1"], "k", lazy.layout.move_down(), desc='Move up a section in treetab'),
    Key([mod, "mod1"], "l", lazy.layout.move_right(), desc='Move up a section in treetab'),
    Key([mod, "mod1"], "h", lazy.layout.move_left(), desc='Move up a section in treetab'),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ), Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    #Key([mod, "shift"], "i", lazy.layout.crient_to_next()),


    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Volume Keys
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle"), desc="Mute/Unmute"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%- unmute"), desc="Lower volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+ unmute"), desc="Raise Volume"),
    Key([alt, "shift"], "space", lazy.spawn("setxkbmap us"), desc="English Keyboard Layout"),
    Key([alt], "space", lazy.spawn("setxkbmap latam"), desc="Spanish Keyboard Layout"),
    
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5"), desc="More Brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5"), desc="Lower Brightness"),

    # Created commands #########################################################################

    # Runs application Menu
    Key([mod], "p", lazy.run_extension(extension.J4DmenuDesktop(
            dmenu_prompt="",
            dmenu_lines=20,
            dmenu_ignorecase=True,
            j4dmenu_terminal="alacritty")
        ), desc="Run j4Dmenu app search"),

    Key([alt], "Tab", lazy.run_extension(extension.WindowList(
            dmenu_prompt="",
            dmenu_ignorecase=True
        )), desc="Display Windows List"),

    # Takes Screenshots
    Key([], "Print", lazy.spawn("flatpak run --user org.flameshot.Flameshot gui"), desc="Run flameshot screenshot"),
    #Key([mod], "e", lazy.spawn("alacritty -e ranger"),desc="Opens Ranger"),
    # Open either chrome or firefox or librewolf
    KeyChord([mod], "b", [
        #Key([], "c", lazy.spawn("flatpak run com.google.Chrome")),
            Key([], "f", lazy.group['scratchpad'].dropdown_toggle('firefox'), desc="Firefox"),
            Key([], "c", lazy.group['scratchpad'].dropdown_toggle('chrome'), desc="Google Chrome"),
        ]),

    # Toggle floating
    Key([mod, "control"], "space", lazy.window.toggle_floating(), desc="Toggles Floting on windows"), 
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggles fullscreen focus window"), 

    # Moves between groups.
    Key([mod], "Right", lazy.screen.next_group(), desc="Move to right" ),
    Key([mod], "Left", lazy.screen.prev_group(), desc="Move to left" ),
    Key([mod], "Escape", lazy.screen.toggle_group(), desc="Move previous group" ),

    # Scratch pads for chats
    
    Key([mod], "F1", lazy.group['scratchpad'].dropdown_toggle('ringcentral'), desc="Ring Central ScratchPad"),
    Key([mod], "F2", lazy.group['scratchpad'].dropdown_toggle('whatsapp'), desc="WhatsApp ScratchPad"),
    Key([mod], "F3", lazy.group['scratchpad'].dropdown_toggle('keepass'), desc="Keepass Scratch Pad"),

    # Scratchs for tools

    Key([mod], "n", lazy.group['scratchpad'].dropdown_toggle('term'), desc="Floating Terminal"),
    Key([mod], "e", lazy.group['scratchpad'].dropdown_toggle('ranger'), desc="File Manager Ranger Floating"),
    Key([mod], "F12", lazy.group['scratchpad'].dropdown_toggle('keys'), desc="Qtile Keys"),


    
    # S
    KeyChord([mod], "s", [
            Key([], "F1", lazy.group['scratchpad'].dropdown_toggle('cmus'), desc="Cmus"),
            Key([], "F2", lazy.group['scratchpad'].dropdown_toggle('android'), desc="Screen Copy"),
            Key([], "F3", lazy.group['scratchpad'].dropdown_toggle('notes'), desc="Obsidian"),
            Key([], "F4", lazy.group['scratchpad'].dropdown_toggle('zathura'), desc="E-Book Reader"),
            Key([], "F5", lazy.group['scratchpad'].dropdown_toggle('bluetuith'), desc="Bluetooth"),
            Key([], "F6", lazy.group['scratchpad'].dropdown_toggle('nvim'), desc="nvim")
            ]),

    # Sticky window set up

    #Key([mod], "o", lazy.function(stick_win), desc="stick win"),
    #Key([mod, "shift"], "o", lazy.function(unstick_win), desc="unstick win"),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

