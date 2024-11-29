# Qtile configuration file
## Screenshots
![image](https://github.com/jkhabra/dotfiles/assets/22749805/a6d13aa5-e213-4160-8583-037edeb0bf2b)
<img src="https://github.com/jkhabra/dotfiles/assets/22749805/bc48d5f3-345b-4da4-986c-adf4462c3a08" alt="image1" width="35%"> | <img src="https://github.com/jkhabra/dotfiles/assets/22749805/1c945d1f-8842-4eb3-80a5-8a9cd7cf886f" alt="image2" width="35%">

## What is Qtile?
Qtile is a window manager written and configured in Python🐍. It is hackable and lightweight, you can install it among other desktop environments and standalone WM's.

## Installation
Install Qtile and other dependencies.

### For Arch Linux
All software, one command:
```bash
  yay -S qtile qtile-extras picom rofi feh alacritty bat playerctl dunst ttf-font-awesome network-manager-applet ranger flameshot htop transmission-gtk zsh starship
```

### Setup
```bash
  git clone https://github.com/jkhabra/dotfiles.git ~/.dotfiles
  cd dotfiles
  chmod +x autostart.sh
  chmod +x ./scripts/autostart.sh
```
Than replace the config file with these
