from libqtile import bar, extension, hook, layout, qtile, widget
# Make sure 'qtile-extras' is installed or this config will not work.
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import PowerLineDecoration
from libqtile.config import Screen
from colors import Gruvbox
import colors

colors = colors.DoomOne

# --------------------------------------------------------
# Decorations
# https://qtile-extras.readthedocs.io/en/stable/manual/how_to/decorations.html
# --------------------------------------------------------

decor_left = {
    "decorations": [
        PowerLineDecoration(
            #path="arrow_left"
            path="rounded_left"
            #path="forward_slash"
            #path="back_slash"
        )
    ],
}

decor_right = {
    "decorations": [
        PowerLineDecoration(
            #path="arrow_right"
            path="rounded_right"
            #path="forward_slash"
            #path="back_slash"
        )
    ],
}

c = "#282c34"
def init_widgets_list():
    widgets_list = [
        widget.Spacer(
            **decor_right,
            background=Gruvbox['shade3'],
            length= 3
        ),
        widget.GroupBox(
            **decor_left,
            fontsize = 11,
            margin_y = 5,
            margin_x = 5,
            padding_y = 0,
            padding_x = 1,
            borderwidth = 3,
            active = colors[1],
            inactive = colors[1],
            rounded = False,
            hide_unused = True,
            highlight_color = colors[2],
            highlight_method = "line",
            this_current_screen_border = colors[7],
            this_screen_border = colors [4],
            other_current_screen_border = colors[7],
            other_screen_border = colors[4],
        ),
          widget.CurrentLayoutIcon(
            **decor_left,
            #background='#FF5E5E'+'.7',
            #foreground="000000.8",
            background=Gruvbox['shade5'],
            padding = 4,
            scale = 0.6,
            foreground = colors[1],
        ),
        widget.CurrentLayout(
            **decor_left,
            background=Gruvbox['shade5'],
            #background='#FF5E5E'+'.7',
            foreground="000000.8",
            #foreground = colors[1],
            padding = 5
        ),
        widget.CheckUpdates(
            **decor_left,
            fmt=" {}",
            foreground="000000.8",
            distro="Arch_yay",
            update_interval=900,
            colour_have_updates=colors[4],
            colour_no_updates=colors[4],
        ),
        widget.WindowName(
            **decor_left,
            max_chars=50,
            #background=Gruvbox['blue']+'.2',
            #background=Color2+".4",
            foreground = colors[6],
            padding=5,
            background="#08080c99",
        ),
        widget.Spacer(
            **decor_right,
            foreground="#08080c99",
        ),
        widget.Clock(
            **decor_left,
            padding=10,
            background=Gruvbox['shade5'],
            #foreground = colors[4],
            format = "⏱  %a, %b %d - %I:%M:%S %p",
        ),
        widget.Spacer(
            **decor_right,
            foreground="#08080c99",
        ),
        widget.Net(
            **decor_right,
            #background='#303F9F'+'.8',
            background=Gruvbox['shade1'],
            #foreground = colors[1],
            format='{down:.0f}{down_suffix} ↓↑',
            padding=10
        ),
        widget.CPU(
            **decor_right,
            format = ' {load_percent}%',
            #foreground = colors[4],
            background=Gruvbox['shade2'],
            padding=10,
        ),
         widget.Memory(
            **decor_right,
            padding=10,
            background=Gruvbox['shade3'],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
            measure_mem='M',
            format = '{MemUsed: .0f}{mm}',
            fmt = ' {} used',
        ),
        widget.DoNotDisturb(
            **decor_right,
            padding=10,
            background=Gruvbox['shade4'],
            #foreground = colors[3],
            disabled_icon = '',
            enabled_icon = '',
        ),
        widget.Volume(
            **decor_right,
            padding=10,
            background=Gruvbox['shade5'],
            fmt = ' {}',
        ),
        widget.Volume(
            **decor_right,
            padding=10,
            background=Gruvbox['shade6'],
            channel='Capture',
            #foreground = colors[7],
            fmt = ' {}',
        ),
        # widget.Clock(
        #     **decor_right,
        #     padding=10,
        #     background=Gruvbox['shade7'],
        #     #foreground = colors[4],
        #     format = "⏱  %a, %b %d - %I:%M:%S %p",
        # ),
        widget.Battery(
            #**decor_right,
            **decor_left,
            padding=10,
            background=Gruvbox['shade7'],
            #background=Gruvbox['shade8']+".3",
            #foreground = colors[1],
            # fmt = '🔋: {}',
            format = '{char} {percent:2.0%}',
            ging_char=' ',
            charge_char='⚡',
            discharge_char='',
            empty_char='',
            full_char='',
        ),
        widget.Systray(
            **decor_left,
            background=Gruvbox['shade8'],
            padding = 3
            ),
        widget.Spacer(
            background=Gruvbox['shade3'],
            length= 5
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
background = '#08080c99'
size = 28
padding = 15
opacity = 0.9
border_width = [0, 0, 0, 0]
margin = [0,0,0,0]


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(),background=background, size=size, padding=padding, opacity=opacity, border_width=border_width, margin=margin)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(),background=background, size=size, padding=padding, opacity=opacity, border_width=border_width, margin=margin)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(),background=background, size=size, padding=padding, opacity=opacity, border_width=border_width, margin=margin))]
