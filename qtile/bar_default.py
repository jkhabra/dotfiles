from libqtile import bar, extension, hook, layout, qtile, widget
# Make sure 'qtile-extras' is installed or this config will not work.
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import PowerLineDecoration
from libqtile.config import Screen

import colors

colors = colors.DoomOne
tsBgColor = '#08080c99' #'#0d0d1399'

decor_left = {
    "decorations": [
        PowerLineDecoration(
            #path="arrow_left"
            path="rounded_left"
            # path="forward_slash"
            # path="back_slash"
        )
    ],
}

decor_right = {
    "decorations": [
        PowerLineDecoration(
            #path="arrow_right"
            path="rounded_right"
            # path="forward_slash"
            # path="back_slash"
        )
    ],
}

widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize = 12,
    padding = 0,
    background=colors[0]
)

extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
        widget.Image(
            **decor_left,
            filename = "~/.config/qtile/icons/logo.png",
            scale = "False",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)},
        ),
        # widget.Prompt(
        #          font = "Ubuntu Mono",
        #          fontsize=14,
        #          foreground = colors[1]
        # ),
        widget.GroupBox(
            **decor_left,
            fontsize = 11,
            margin_y = 5,
            margin_x = 5,
            padding_y = 0,
            padding_x = 1,
            borderwidth = 3,
            active = colors[8],
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
        widget.TextBox(
            text = '|',
            font = "Ubuntu Mono",
            foreground = colors[1],
            padding = 2,
            fontsize = 14
        ),
        widget.CurrentLayoutIcon(
            # custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
            foreground = colors[1],
            padding = 4,
            scale = 0.6
        ),
        widget.CurrentLayout(
            foreground = colors[1],
            padding = 5
        ),
        widget.TextBox(
            text = '|',
            font = "Ubuntu Mono",
            foreground = colors[1],
            padding = 2,
            fontsize = 14
        ),
        widget.WindowName(
            background=tsBgColor,
            foreground = colors[6],
            max_chars = 40
        ),
        widget.Spacer(length = 8),
        widget.Net(
            foreground = colors[1],
            format='{down:.0f}{down_suffix} ↓↑',
            decorations=[
                BorderDecoration(
                    colour = colors[1],
                    border_width = [0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length = 5),
        widget.CPU(
            format = ' {load_percent}%',
            foreground = colors[4],
            decorations=[
                BorderDecoration(
                    colour = colors[4],
                    border_width = [0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length = 8),
        widget.Memory(
            foreground = colors[8],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
            measure_mem='M',
            format = '{MemUsed: .0f}{mm}',
            fmt = ' {} used',
            decorations=[
                BorderDecoration(
                    colour = colors[8],
                    border_width = [0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length = 10),
        widget.DoNotDisturb(
            foreground = colors[3],
            disabled_icon = '',
            enabled_icon = '',
            decorations=[
                BorderDecoration(
                    colour = colors[3],
                    border_width = [0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length = 8),
        widget.Volume(
            foreground = colors[7],
            fmt = ' {}',
            decorations=[
                BorderDecoration(
                    colour = colors[7],
                    border_width = [0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length = 8),
        widget.Volume(
            channel='Capture',
            foreground = colors[7],
            fmt = ' {}',
            decorations=[
                BorderDecoration(
                    colour = colors[7],
                    border_width = [0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length = 8),
        widget.Clock(
            foreground = colors[4],
            format = "⏱  %a, %b %d - %I:%M:%S %p",
            decorations=[
                BorderDecoration(
                    colour = colors[4],
                    border_width = [0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length = 8),
        widget.Battery(
            #**decor_left,
            foreground = colors[1],
            # fmt = '🔋: {}',
            format = '{char} {percent:2.0%}',
            # format='{percent:2.0%}',
                 decorations=[
                     PowerLineDecoration(
                        #path="arrow_left"
                        path="rounded_left"
                        # path="forward_slash"
                        # path="back_slash"
                        ),
                     BorderDecoration(
                         colour = colors[1],
                         border_width = [0, 0, 2, 0],
                     )
                 ],
            not_charging_char=' ',
            charge_char='⚡',
            discharge_char='',
            empty_char='',
            full_char='',
        ),
    widget.Spacer(length = 5),
    widget.Systray(padding = 3),
    widget.Spacer(length = 5),
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
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(),background=tsBgColor, size=26)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(),background=tsBgColor, size=26)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(),background=tsBgColor, size=26))]
