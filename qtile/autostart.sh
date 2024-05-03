#!/usr/bin/env bash 

COLORSCHEME=DoomOne

### AUTOSTART PROGRAMS ###
lxsession &
picom --daemon &
/usr/bin/emacs --daemon &
nm-applet &
"$HOME"/.screenlayout/layout.sh &
picom -b --config $HOME/.config/qtile/scripts/picom.conf  &

sleep 1
# conky -c "$HOME"/.config/conky/qtile/01/"$COLORSCHEME".conf || echo "Couldn't start conky."
setxkbmap -option ctrl:nocaps
systemctl --user start dunst.service

### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
# xargs xwallpaper --stretch < ~/.cache/wall &
# 2. Uncomment to set a random wallpaper on login
feh --bg-fill --randomize "$HOME"/wallpapers
# find /home/j/Downloads/wallpapers/ -type f | shuf -n 1 | xargs xwallpaper --stretch &
# 3. Uncomment to set wallpaper with nitrogen
# nitrogen --restore &
