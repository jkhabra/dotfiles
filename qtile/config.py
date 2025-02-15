import os
import subprocess
from libqtile import bar, extension, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
# Make sure 'qtile-extras' is installed or this config will not work.
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
#from qtile_extras.widget import StatusNotifier
import colors
#from bar_default2 import init_widgets_list, init_screens, init_widgets_screen1, init_widgets_screen2
from bar_default import init_widgets_list, init_screens, init_widgets_screen1, init_widgets_screen2
#from bar_gruvbox import init_widgets_list, init_screens, init_widgets_screen1, init_widgets_screen2
#from bar_nordic import init_widgets_list, init_screens, init_widgets_screen1, init_widgets_screen2
#from bar_oxide import init_widgets_list, init_screens, init_widgets_screen1, init_widgets_screen2

mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"      # My terminal of choice
myBrowser = "zen-browser"       # My browser of choice
myEmacs = "emacs" # The space at the end is IMPORTANT!
bgchange = "feh --bg-fill --randomize /home/j/wallpapers/"
screenshot = "flameshot"

# Allows you to input a name when adding treetab section.
@lazy.layout.function
def add_treetab_section(layout):
    prompt = qtile.widgets_map["prompt"]
    prompt.start_input("Section name: ", layout.cmd_add_section)

# A function for hide/show all the windows in a group
@lazy.function
def minimize_all(qtile):
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()

# A function for toggling between MAX and MONADTALL layouts
@lazy.function
def maximize_by_switching_layout(qtile):
    current_layout_name = qtile.current_group.layout.name
    if current_layout_name == 'monadtall':
        qtile.current_group.layout = 'max'
    elif current_layout_name == 'max':
        qtile.current_group.layout = 'monadtall'


keys = [
    # The essentials
    Key([mod], "Return", lazy.spawn(myTerm), desc="Terminal"),
    Key([mod], "d", lazy.spawn("rofi -show drun"), desc='Run Launcher'),
    Key([mod, "shift"], "d", lazy.spawn("rofi -show window"), desc='Run window'), #show all ruing windows
    Key([mod], "b", lazy.spawn(myBrowser), desc='firefox'),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "c", lazy.spawn("dm-logout -r"), desc="Logout menu"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # change to spasific layout
    Key([mod], "e", lazy.group.setlayout("monadtall"), desc="go to monadtall layout"),
    Key([mod], "w", lazy.group.setlayout("max"), desc="go to max layout"),
    #Key([mod], "z", lazy.group.setlayout("treetab"), desc="go to max layout"),

    #ScratchPad keybindings
    Key([mod], "c", lazy.group['scratchpad'].dropdown_toggle('ranger'), "Toogle ranger scratchpad"),
    Key([mod], "x", lazy.group['scratchpad'].dropdown_toggle('term'), "Toogle terminal scratchpad"),

    # change wallpaper randomize
    #Key([mod], "v", lazy.spawn(home + ".config/qtile/scripts/wallpaper.sh"), desc="Update Theme and Wallpaper"),
    Key([mod], "v", lazy.spawn(bgchange),desc='random wallpaper'),

    Key([mod, "shift"], "s",
        lazy.spawn(screenshot),
        desc='Screenshot'
        ),
    # Switch between windows
    # Some layouts like 'monadtall' only need to use j/k to move
    # through the stack, but other layouts like 'columns' will
    # require all four directions h/j/k/l to move around.
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        lazy.layout.move_left().when(layout=["treetab"]),
        desc="Move window to the left/move tab left in treetab"),

    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        lazy.layout.move_right().when(layout=["treetab"]),
        desc="Move window to the right/move tab right in treetab"),

    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down().when(layout=["treetab"]),
        desc="Move window down/move down a section in treetab"
    ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up().when(layout=["treetab"]),
        desc="Move window downup/move up a section in treetab"
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "space", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # Treetab prompt
    Key([mod, "shift"], "a", add_treetab_section, desc='Prompt to add new section in treetab'),

    # Grow/shrink windows left/right. 
    # This is mainly for the 'monadtall' and 'monadwide' layouts
    # although it does also work in the 'bsp' and 'columns' layouts.
    Key([mod], "equal",
        lazy.layout.grow_left().when(layout=["bsp", "columns"]),
        lazy.layout.grow().when(layout=["monadtall", "monadwide"]),
        desc="Grow window to the left"
    ),
    Key([mod], "minus",
        lazy.layout.grow_right().when(layout=["bsp", "columns"]),
        lazy.layout.shrink().when(layout=["monadtall", "monadwide"]),
        desc="Grow window to the left"
    ),

    # Grow windows up, down, left, right.  Only works in certain layouts.
    # Works in 'bsp' and 'columns' layout.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "m", lazy.layout.maximize(), desc='Toggle between min and max sizes'),
    Key([mod], "t", lazy.window.toggle_floating(), desc='toggle floating'),
    Key([mod], "f", maximize_by_switching_layout(), lazy.window.toggle_fullscreen(), desc='toggle fullscreen'),
    Key([mod, "shift"], "m", minimize_all(), desc="Toggle hide/show all windows on current group"),

    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen(), desc='Move focus to next monitor'),
    Key([mod], "comma", lazy.prev_screen(), desc='Move focus to prev monitor'),
    
    # # Emacs programs launched using the key chord CTRL+e followed by 'key'
    # KeyChord([mod],"e", [
    #     Key([], "e", lazy.spawn(myEmacs), desc='Emacs Dashboard'),
    #     Key([], "a", lazy.spawn(myEmacs + "--eval '(emms-play-directory-tree \"~/Music/\")'"), desc='Emacs EMMS'),
    #     Key([], "b", lazy.spawn(myEmacs + "--eval '(ibuffer)'"), desc='Emacs Ibuffer'),
    #     Key([], "d", lazy.spawn(myEmacs + "--eval '(dired nil)'"), desc='Emacs Dired'),
    #     Key([], "i", lazy.spawn(myEmacs + "--eval '(erc)'"), desc='Emacs ERC'),
    #     Key([], "s", lazy.spawn(myEmacs + "--eval '(eshell)'"), desc='Emacs Eshell'),
    #     Key([], "v", lazy.spawn(myEmacs + "--eval '(vterm)'"), desc='Emacs Vterm'),
    #     # Key([], "w", lazy.spawn(myEmacs + "--eval '(eww \"distro.tube\")'"), desc='Emacs EWW'),
    #     Key([], "F4", lazy.spawn("killall emacs"),
    #                   lazy.spawn("/usr/bin/emacs --daemon"),
    #                   desc='Kill/restart the Emacs daemon')
    # ]),
    # Dmenu/rofi scripts launched using the key chord SUPER+p followed by 'key'
    KeyChord([mod], "p", [
        Key([], "h", lazy.spawn("dm-hub -r"), desc='List all dmscripts'),
        Key([], "a", lazy.spawn("dm-sounds -r"), desc='Choose ambient sound'),
        Key([], "b", lazy.spawn("dm-setbg -r"), desc='Set background'),
        Key([], "c", lazy.spawn("dtos-colorscheme -r"), desc='Choose color scheme'),
        Key([], "e", lazy.spawn("dm-confedit -r"), desc='Choose a config file to edit'),
        Key([], "i", lazy.spawn("dm-maim -r"), desc='Take a screenshot'),
        Key([], "k", lazy.spawn("dm-kill -r"), desc='Kill processes '),
        Key([], "m", lazy.spawn("dm-man -r"), desc='View manpages'),
        Key([], "n", lazy.spawn("dm-note -r"), desc='Store and copy notes'),
        Key([], "o", lazy.spawn("dm-bookman -r"), desc='Browser bookmarks'),
        Key([], "p", lazy.spawn("rofi-pass"), desc='Logout menu'),
        Key([], "q", lazy.spawn("dm-logout -r"), desc='Logout menu'),
        Key([], "r", lazy.spawn("dm-radio -r"), desc='Listen to online radio'),
        Key([], "s", lazy.spawn("dm-websearch -r"), desc='Search various engines'),
        Key([], "t", lazy.spawn("dm-translate -r"), desc='Translate text')
    ])

]

groups = []
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]

group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
group_labels = ["DEV", "CODE", "TER", "CHAT", "SYS", "DOC", "VBOX", "MUS", "VID",]
#group_labels = ["", "",  "", "", "", "", "", "", "",]
#group_labels = ["", "", "", "",  "", "", "", "", "", ""]
group_layouts = ["monadtall", "treetab", "monadtall", "treetab", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Move focused window to group {}".format(i.name),
            ),
        ]
    )

colors = colors.DoomOne

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": colors[8],
                "border_normal": colors[0]
                }

layouts = [
    #layout.Bsp(**layout_theme),
    #layout.Floating(**layout_theme)
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    #layout.MonadWide(**layout_theme),
    # layout.Tile(
    #      shift_windows=True,
    #      border_width = 0,
    #      margin = 0,
    #      ratio = 0.335,
    #      ),
    layout.Max(
         border_width = 0,
         margin = 0,
         ),
    #layout.Stack(**layout_theme, num_stacks=2),
    #layout.Columns(**layout_theme),
    layout.TreeTab(
         font = "Ubuntu Bold",
         fontsize = 11,
         border_width = 0,
         bg_color = '#1751B457',
         active_bg = colors[8],
         active_fg = colors[2],
         inactive_bg = colors[1],
         inactive_fg = colors[0],
         padding_left = 3,
         padding_x = 2,
         padding_y = 5,
         sections = ["ONE", "TWO"],
         # sections = ["ONE", "TWO", "THREE"],
         place_right = 'true',
         section_fontsize = 8,
         section_fg = colors[7],
         section_top = 15,
         section_bottom = 15,
         level_shift = 10,
         vspace = 10,
         panel_width = 45
         ),
    #layout.Zoomy(**layout_theme), 
]

#Define scratchpads
groups.append(ScratchPad("scratchpad", [
    DropDown('ranger', 'alacritty --class=ranger -e ranger', width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('term', 'alacritty --class=scratch', width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
]))


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

# Define the function to change the wallpaper
def change_wallpaper():
    wallpaper_dir = os.path.expanduser('~/wallpapers/')
    subprocess.run(['feh', '--bg-fill', '--randomize', wallpaper_dir])
    #subprocess.run(['feh', '--bg-fill', '--randomize', os.path.expanduser('~') + '/wallpapers/'])
    #os.system('feh --bg-fill --randomize /home/j/wallpapers/')

# This function sets up the timer to change wallpaper every 60 seconds
def setup_timer():
    hook.add_timer(60, change_wallpaper)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=colors[8],
    border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),   # gitk
        Match(wm_class="dialog"),         # dialog boxes
        Match(wm_class="download"),       # downloads
        Match(wm_class="error"),          # error msgs
        Match(wm_class="file_progress"),  # file progress boxes
        Match(wm_class='kdenlive'),       # kdenlive
        Match(wm_class="makebranch"),     # gitk
        Match(wm_class="maketag"),        # gitk
        Match(wm_class="notification"),   # notifications
        Match(wm_class='pinentry-gtk-2'), # GPG key password entry
        Match(wm_class="ssh-askpass"),    # ssh-askpass
        Match(wm_class="toolbar"),        # toolbars
        Match(wm_class="Yad"),            # yad boxes
        Match(title="branchdialog"),      # gitk
        Match(title='Confirmation'),      # tastyworks exit box
        Match(title='Qalculate!'),        # qalculate-gtk
        Match(title="pinentry"),          # GPG key password entry
        Match(title="tastycharts"),       # tastytrade pop-out charts
        Match(title="tastytrade"),        # tastytrade pop-out side gutter
        Match(title="tastytrade - Portfolio Report"), # tastytrade pop-out allocation
        Match(wm_class="tasty.javafx.launcher.LauncherFxApp"), # tastytrade settings
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

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
    # Call the function initially to set a wallpaper when Qtile starts
    change_wallpaper()
    # Setup the timer for periodic wallpaper changes
    #setup_timer()

    # Open applications and assign to specific workspaces with delays
    qtile.groups["1"].cmd_toscreen()
    subprocess.Popen([myBrowser])  # Launch browser on workspace 1
    time.sleep(1)  # Add a delay to ensure the app opens fully

    qtile.groups["2"].cmd_toscreen()
    subprocess.Popen([myEmacs])    # Launch Emacs on workspace 2
    time.sleep(3)

    qtile.groups["3"].cmd_toscreen()
    subprocess.Popen([myTerm])     # Launch terminal on workspace 3

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
