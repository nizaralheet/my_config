# pywal-wpgtk dynamic RICE

## Important notes !!!
- all config files that i have customized for every thing im my system are here
- make sure to make the autostart.sh excutable by running this command ```chmod +x .config/qtile/autostart.sh```
- you could disable the blur or the animaton from picom config if you feel your machine is slow , it is disabled by default
- to make dunst sync with pywal you have to make a link like this 🔻 so any change in pywal or wpgtk changes dunst theme
```
ln -s .cache/wal/dunstrc .config/dunst/dunstrc
```
 
## Dependencies 
-Run this command on arch to install the Dependencies 
```
yay -S --needed gdk-pixbuf2  glibc  libnotify  librsvg  pango  python python-cairocffi  python-cffi  python-gobject  python-xcffib wlroots alsa-utils lm_sensors python-dbus-next python-iwlib python-psutil python-pywayland python-pywlroots python-xkbcommon xorg-xwayland qtile-extras imagemagick python-pywal wpgtk feh libxdg-basedir  startup-notification  libxkbcommon-x11 xcb-util-wm  xcb-util-xrm  librsvg  xcb-util-cursor dunst libxinerama  dbus systemd  wayland  libxss  pango  gdk-pixbuf2 libxrandr  glib2 libnotify upower python-attrs python-pulsectl Python-psutil python-pulsectl-asyncio kitty 
```

- I use this [fdev31 picom](https://github.com/fdev31/picom) fork , but you can you use any like FT-laps fork.
- For text editor I use [lunarvim](https://github.com/LunarVim/LunarVim) .
- For the gtk theme and icons i use flatcolor theme and flattrcolor icons they are in  [wpgtk-templates](https://github.com/deviantfero/wpgtk-templates) and i use [tela-cirle](https://github.com/vinceliuice/Tela-circle-icon-theme) for rofi 
- For themeing [chromium based browsers](https://github.com/metafates/ChromiumPywal) and [firefox](https://github.com/Frewacom/pywalfox/) install the extension for every one of them
- the font : ```ttf-sourcecodepro-nerd```

## Key Bindings 



| **Key Combination**                      | **Action**                                     |
|------------------------------------------|------------------------------------------------|
| **System Controls**                      |                                                |
| `Print`                                  | 🖼️ Take a screenshot with Flameshot            |
| `mod + L`                                | 🔒 Lock the screen using Betterlockscreen       |
| `XF86MonBrightnessUp`                    | 🔆 Increase brightness                          |
| `XF86MonBrightnessDown`                  | 🔅 Decrease brightness                          |
| `XF86AudioMute`                          | 🔇 Mute volume                                  |
| `XF86AudioLowerVolume`                   | 🔉 Decrease volume                              |
| `XF86AudioRaiseVolume`                   | 🔊 Increase volume                              |
| `mod + Control + R`                      | 🔄 Reload the Qtile config                      |
| `mod + Control + Q`                      | ❌ Shutdown Qtile                               |
| `mod + N`                                | 🔄 Reset all window sizes                       |
| **Application Launchers & Rofi**         |                                                |
| `mod + [`                                | 🖼️ Run a wallpaper select Rofi script           |
| `mod + E`                                | 📂 Open Thunar file manager                     |
| `alt + Tab`                              | 🔄 Open Rofi window switcher                    |
| `mod + ,`                                | 😀 Open Rofi emojis picker                      |
| `mod + V`                                | 📋 Show CopyQ clipboard manager                 |
| `mod + R`                                | 🚀 Spawn Rofi app launcher                      |
| `mod + B`                                | 🌐 Spawn browser                                |
| **Window Management**                    |                                                |
| `mod + Left`                             | ⬅️ Move focus to the left                       |
| `mod + Right`                            | ➡️ Move focus to the right                      |
| `mod + Down`                             | ⬇️ Move focus downward                          |
| `mod + Up`                               | ⬆️ Move focus upward                            |
| `mod + Space`                            | 🔄 Move window focus to another window          |
| `mod + Shift + Left`                     | ⬅️ Move window to the left                      |
| `mod + Shift + Right`                    | ➡️ Move window to the right                     |
| `mod + Shift + Down`                     | ⬇️ Move window downward                         |
| `mod + Shift + Up`                       | ⬆️ Move window upward                           |
| `mod + Control + Left`                   | ⬅️ Grow window to the left                      |
| `mod + Control + Right`                  | ➡️ Grow window to the right                     |
| `mod + Control + Down`                   | ⬇️ Grow window downward                         |
| `mod + Control + Up`                     | ⬆️ Grow window upward                           |
| `mod + Shift + Return`                   | 🔀 Toggle between split and unsplit sides of stack |
| `mod + Tab`                              | 🔄 Toggle between layouts                       |
| `mod + W`                                | ❌ Kill the focused window                      |
| `mod + F`                                | 🔳 Toggle fullscreen                            |
| `mod + M`                                | 🗜️ Toggle minimize                              |
| `mod + T`                                | 🗂️ Toggle floating                              |
| **Group Management**                     |                                                |
| `mod + PgDn`                             | ⬇️ Jump to the next group                       |
| `mod + PgUp`                             | ⬆️ Jump to the previous group                   |
| `mod + 1-5`                              | 🔢 Switch to group 1-5                          |
| `mod + Shift + 1-5`                      | 🔢 Switch to & move focused window to group 1-5   |

---

