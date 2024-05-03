from libqtile import qtile
from libqtile.bar import Bar
from libqtile.widget.volume import Volume
from libqtile.widget.sep import Sep
from libqtile.widget.image import Image
from libqtile.widget.currentlayout import CurrentLayoutIcon
from libqtile.widget.battery import Battery
from libqtile.widget.clock import Clock
from libqtile.widget.cpu import CPU
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.spacer import Spacer
from libqtile.widget.systray import Systray
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName
from libqtile.config import Screen
from qtile_extras.widget.decorations import PowerLineDecoration
#from unicodes import left_half_circle, right_arrow, left_arrow, right_half_circle, lower_left_triangle, lower_right_triangle
import colors
from colors import Gruvbox

barHeight = 20
tsBgColor =  Gruvbox['bg'] #'#16161e90'

decor_left = {
    "decorations": [
        PowerLineDecoration(
            path="arrow_left"
            # path="rounded_left"
            # path="forward_slash"
            # path="back_slash"
        )
    ],
}

decor_right = {
    "decorations": [
        PowerLineDecoration(
            #path="arrow_right"
            # path="rounded_right"
            # path="forward_slash"
            path="back_slash"
        )
    ],
}

def init_widgets_list():
    widgets_list = [
        Sep(
            linewidth=0,
            padding=10,
            foreground=Gruvbox['bg'],
            background = Gruvbox['red']
        ),
        Image(
            filename="~/.config/qtile/icons/qtile.png",
            scale="False",
            background=Gruvbox['red'],
            margin_y=-2,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("rofi -show drun -theme ~/.config/rofi/config.rasi")}
        ),
        #lower_right_triangle(Gruvbox['bg'], Gruvbox['red']),
        GroupBox(
            **decor_right,
            font = "FontAwesome Bold", fontsize = 12,
            margin_y = 3, margin_x = 0, padding_y = 5, padding_x = 5,
            borderwidth = 3, rounded = False,
            active = Gruvbox['fg'], inactive = Gruvbox['dark-gray'],
            highlight_color = Gruvbox['bg'], highlight_method = "line",
            this_current_screen_border = Gruvbox['red'], this_screen_border = Gruvbox ['red'],
            other_current_screen_border = Gruvbox['green'], other_screen_border = Gruvbox['red'],
            foreground = Gruvbox['fg'], background = Gruvbox['bg']
        ),
        #lower_right_triangle(Gruvbox['red'], Gruvbox['bg']),
        CurrentLayoutIcon(
            **decor_right,
            background=Gruvbox['red'],
            foreground=Gruvbox['bg'],
            padding = 4,
            scale = 0.6
        ),
        CurrentLayout(
            **decor_right,
            background=Gruvbox['red'],
            foreground=Gruvbox['bg'],
            margin=10,
        ),
        #lower_right_triangle(Gruvbox['fg'], Gruvbox['red']),
        WindowCount(
            **decor_right,
            text_format='缾 {num}',
            background=Gruvbox['fg'],
            foreground=Gruvbox['bg'],
            show_zero=True,
        ),
        #lower_right_triangle(Gruvbox['bg'], Gruvbox['fg']),
        WindowName(
            **decor_right,
            background=Gruvbox['bg'],
            foreground=Gruvbox['fg'],
	        max_chars=25
        ),
        #lower_right_triangle(Gruvbox['dark-purple'], Gruvbox['bg']),
        CPU(
            **decor_left,
            format=' {freq_current}GHz {load_percent}%',
            background=Gruvbox['dark-purple'],
            foreground=Gruvbox['bg']
        ),
        #lower_right_triangle(Gruvbox['dark-blue'], Gruvbox['dark-purple']),
        Memory(
            **decor_left,
            format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
            background=Gruvbox['dark-blue'],
            foreground=Gruvbox['bg']
        ),
        #lower_right_triangle(Gruvbox['dark-yellow'], Gruvbox['dark-blue']),
        Net(
            **decor_left,
	        interface='wlan0',
            format='{interface}: {down:6.2f}{down_suffix:<2}↓↑{up:6.2f}{up_suffix:<2}',
            background=Gruvbox['dark-yellow'],
            foreground=Gruvbox['bg']
        ),
        #lower_right_triangle(Gruvbox['dark-green'], Gruvbox['dark-yellow']),
        Battery(
            **decor_left,
            background=Gruvbox['dark-green'],
	        foreground=Gruvbox['bg'],
            format='{char} {percent:2.0%} {hour:d}:{min:02d}',
	        charge_char='  ',
            not_charging_char='',
	        full_char=' ',
	        discharge_char=' ',
	        update_interval = 5
        ),
        #lower_right_triangle(Gruvbox['dark-red'], Gruvbox['dark-green']),
        Volume(
            **decor_left,
            background = Gruvbox['dark-red'],
            foreground = Gruvbox['bg'],
            fmt = '  {}',
        ),
        #lower_right_triangle(Gruvbox['dark-aqua'], Gruvbox['dark-red']),
        Clock(
            **decor_left,
            background=Gruvbox['dark-aqua'],
            foreground=Gruvbox['bg'],
            format=' %Y-%m-%d %a 󰥔 %I:%M %p'
        ),
        #lower_right_triangle(Gruvbox['bg'], Gruvbox['dark-aqua']),
        Systray(
            **decor_left,
            background=Gruvbox['bg']
        ),
    ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

# All other monitors' bars will display everything but widgets 22 (systray) and 23 (spacer).
def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[22:24]
    return widgets_screen2

# For adding transparency to your bar, add (background="#00000000") to the "Screen" line(s)
# For ex: Screen(top=bar.Bar(widgets=init_widgets_screen2(), background="#00000000", size=24)),

def init_screens():
    return [Screen(top=Bar(widgets=init_widgets_screen1(),background=tsBgColor, size=barHeight)),
            Screen(top=Bar(widgets=init_widgets_screen2(),background=tsBgColor, size=barHeight)),
            Screen(top=Bar(widgets=init_widgets_screen2(),background=tsBgColor, size=barHeight))]

