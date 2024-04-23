# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#

###################################################
#    ____                                __       #
#   /  _/____ ___   ____   ____   _____ / /_ _____#
#   / / / __ `__ \ / __ \ / __ \ / ___// __// ___/#
# _/ / / / / / / // /_/ // /_/ // /   / /_ (__  ) #
#/___//_/ /_/ /_// .___/ \____//_/    \__//____/  #
#               /_/                               #
###################################################
import os 
import subprocess
from libqtile import bar, layout, qtile, hook
from qtile_extras import widget
from libqtile.widget import backlight
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras.widget.decorations import RectDecoration
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal, send_notification





@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("/home/nizar/.config/qtile/autostart.sh")
    subprocess.Popen([home])

mod = "mod4"
terminal = "alacritty"
home= os.path.expanduser("~")
##########################################################
# _  __            ____  _           _ _                 #
#| |/ /           |  _ \(_)         | (_)                #
#| ' / ___ _   _  | |_) |_ _ __   __| |_ _ __   __ _ ___ #
#|  < / _ | | | | |  _ <| | '_ \ / _` | | '_ \ / _` / __|#
#| . |  __| |_| | | |_) | | | | | (_| | | | | | (_| \__ \#
#|_|\_\___|\__, | |____/|_|_| |_|\__,_|_|_| |_|\__, |___/#
#           __/ |                               __/ |    #
#          |___/                               |___/     #
##########################################################
keys = [
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),

    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),

    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),

    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 3- unmute")),

    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 3+ unmute")),

    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),

    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),

    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),

    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),

    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),

    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),

    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),

    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "Right",
        lazy.layout.grow_right(), desc="Grow window to the right"),
    Key(
        [mod, "control"],
        "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key(
        [mod, "control"], "Up",
        lazy.layout.grow_up(), desc="Grow window up"),
    Key(
        [mod], "n",
        lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],"Return",
        lazy.layout.toggle_split(),desc="Toggle between split and unsplit sides of stack",),
    Key(
        [mod], "Return",
        lazy.spawn("alacritty"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key(
        [mod], "Tab",
        lazy.next_layout(), desc="Toggle between layouts"),
    Key(
        [mod],"w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],"f",
        lazy.window.toggle_fullscreen(),desc="Toggle fullscreen",),
    Key(
        [mod], "t",
        lazy.window.toggle_floating(), desc="Toggle floating"),
    Key(
        [mod, "control"], "r",
        lazy.reload_config(), desc="Reload the config"),
    Key(
        [mod, "control"], "q",
        lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [mod], "r",
        lazy.spawn("rofi -show drun"), desc="Spawn rofi app laucher"),
    Key(
        [mod], "b",
        lazy.spawn("brave"), desc="spawn brave browser"),

]
###########################################
#   ______                                #
#  / ____/_____ ____   __  __ ____   _____#
# / / __ / ___// __ \ / / / // __ \ / ___/#
#/ /_/ // /   / /_/ // /_/ // /_/ /(__  ) #
#\____//_/    \____/ \__,_// .___//____/  #
#                         /_/             #
###########################################
#groups = [Group(i) for i in "12345"]

groups = [
        Group("1",label= "-"),
        Group("2",label= "="),
        Group("3",label= "≡"),
        Group("4",label= "△"),
        Group("5",label= "□"),
        ]

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
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
               desc="Switch to & move focused window to group ".format(i.name),
           ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
            ]
    )
###################################################
#      __                                __       #
#     / /   ____ _ __  __ ____   __  __ / /_ _____#
#    / /   / __ `// / / // __ \ / / / // __// ___/#
#   / /___/ /_/ // /_/ // /_/ // /_/ // /_ (__  ) #
#  /_____/\__,_/ \__, / \____/ \__,_/ \__//____/  #
#               /____/                            #
###################################################
layouts = [
      #Try more layouts by unleashing below layouts.
     #layout.Stack(num_stacks=2),
     #layout.Bsp(),
     #layout.Matrix(),
     #layout.MonadTall(margin=9, border_focus="cce6ff", border_normal="0059b3", border_on_single=True,border_width= 5),
     #layout.MonadWide(),
     #layout.RatioTile(),
     #layout.Tile(),
     #layout.TreeTab(border_width=3, margin= 6, border_focus="ffffff", border_normal="ffff44", active_bg="99ccff", active_fg="000000",sections=[""]),
     #layout.VerticalTile(),
     #layout.Zoomy( margin=9,border_focus="cce6ff",border_normal="0059b3",border_on_single=True,border_width= 5),
     layout.Columns(
         margin=9,
         border_focus="cce6ff",
         border_normal="0059b3",
         border_on_single=True,
         border_width= 5
         ),
     layout.Max(
         margin=9,
         border_focus="cce6ff",
         border_normal="ffff44",
         border_width=5
         ),
    # layout.Floating( border_focus="#ffffff", border_normal="#0059b3",border_width=5),

]
#########################################
#__        ___     _            _       #
#\ \      / (_) __| | __ _  ___| |_ ___ #
# \ \ /\ / /| |/ _` |/ _` |/ _ | __/ __|#
#  \ V  V / | | (_| | (_| |  __| |_\__ \#
#   \_/\_/  |_|\__,_|\__, |\___|\__|___/#
#  __| | ___ / _| __ |___/ _| | |_ ___  #
# / _` |/ _ | |_ / _` | | | | | __/ __| #
#| (_| |  __|  _| (_| | |_| | | |_\__ \ #
# \__,_|\___|_|  \__,_|\__,_|_|\__|___/ #
#########################################
widget_defaults = dict(
    font="Source Code Pro",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()
powerlineA = {
    "decorations": [
        PowerLineDecoration(path="forward_slash")
    ]
}
powerlineB = {
    "decorations": [
        PowerLineDecoration(path="back_slash")
    ]
}
roundshape = {
    "decorations": [
        RectDecoration(colour="#800000",
                       radius=10,
                       filled=True,
                       padding_y=1,
                       group=True)
    ],
    "padding": 10,
}
##################################################
#         _____                                  #
#        / ___/ _____ _____ ___   ___   ____     #
#        \__ \ / ___// ___// _ \ / _ \ / __ \    #
#       ___/ // /__ / /   /  __//  __// / / /    #
#      /____/ \___//_/    \___/ \___//_/ /_/     #
##################################################
screens = [
    Screen(
        wallpaper=".config/qtile/wallpaper.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                #widget.CurrentLayout(),
                widget.Spacer(
                    width=7,
                    length=7,
                    background="0080ff",
                    ),

 
                              
                widget.Image(
                    filename=".config/qtile/logo.png",
                    scale=True,
                    margin_x=-3,
                    background="0080ff",
                    ),
                
                widget.Clock(
                        format=" %I:%M%p ", 
                        background="0080ff", 
                        foreground="#000000",
                        spacing="2"
                        ),


               widget.Spacer(
                    width=7,
                    length=7,
                    background="0080ff",
                    **powerlineA,
                    ),
 

                widget.GroupBox(
                    fontsize=21,
                    active="000000",
                    background="0073e6",
                    highlight_method="line",
                    highlight_color=["0080ff","0059b3"],
                    this_current_screen_border="004080",
                    margin_x=-1,
                    **powerlineA,
                    ),


                widget.WindowName(
                    background="00000000",
                    **powerlineB,
                    empty_group_string="What a great wallpaper...",
                    ),
                

            
                widget.Memory(
                    background="#0062b3",
                    foreground="#000000",
                    format="RAM:{MemPercent}%",
                    #**powerlineB
                    ),

                widget.CPU(
                    background="0062b3",
                    foreground="000000",
                    format= "| CPU:{load_percent}%",
                    **powerlineB
                    ),

                 widget.UPowerWidget(
                    background = "#0070cc",
                    border_colour = "#000000",
                    border_critical_colour = "#cc0000",
                    border_charge_colour = "#000000",
                    fill_low = "#ff6600",
                    fill_charge = "#00cc66",
                    fill_critical = "#cc0000",
                    fill_normal = "#3d3d29",
                    percentage_low = 0.4,
                    percentage_critical = 0.2,
                    foreground="#000000",
                    text_charging="({percentage:.0f}%)",
                    text_discharging="{percentage:.0f}%",
                    text_displaytime=3666,
                    battery_height=13,
                    battery_width=27,
                    **powerlineB,
                    ),

                 widget.WiFiIcon(
                    **powerlineB,
                    background="#0070cc",
                    active_colour="#1e1e1e",
                    foreground="#000000",
                    
                    ),

                
                widget.CheckUpdates(
                    distro="Arch_checkupdates",
                    no_update_string="No updates",
                    background="#0073e6", 
                    foreground="000000",
                    colour_have_updates="000000",
                    colour_no_updates="000000",
                    display_format="Updates:{updates}",
                    **powerlineB,
                    ),


                 widget.OpenWeather(
                    app_key = "4cf3731a25d1d1f4e4a00207afd451a2",
                    cityid = "250441",
                    format = '{main_temp}° {icon}',
                    metric = True,
                    
                    background = "#0080ff",
                    foreground = "#000000",
                     
                        ),

                widget.Clock(
                        format=" %d/%m ", 
                        background="0080ff", 
                        foreground="#000000",
                        spacing="2"
                        ),

                widget.QuickExit(
                        countdown_format="[ {}  ]",
                        default_text="LOGOUT",
                        background="0080ff",
                        padding_x="3",
                        **roundshape
                        ),
                 widget.Spacer(
                    width=7,
                    length=5,
                    background="0080ff",
                    ),


            ],

            24,
      #this ^^ is the bar hight 
             border_width=[3, 0, 0, 0],#Draw top and bottom borders
              border_color=["0080ff",
                            "0060cc",
                            "00000000", 
                            "0060cc"
                            ],

              # Borders are magenta (UP,SIDE,DOWN,SIDE)
                opacity=1,
                background="ffffff00",
              ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
         x11_drag_polling_rate = 60,
    ),
]
####################################################
#          __  ___                                 #
#         /  |/  /____   __  __ _____ ___          #
#        / /|_/ // __ \ / / / // ___// _ \         #
#       / /  / // /_/ // /_/ /(__  )/  __/         #
#      /_/  /_/ \____/ \__,_//____/ \___/          #
####################################################
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
#####################################################################################
#         ____   __   __                  ______ __     _                           #
#        / __ \ / /_ / /_   ___   _____  /_  __// /_   (_)____   ____ _ _____       #
#       / / / // __// __ \ / _ \ / ___/   / /  / __ \ / // __ \ / __ `// ___/       #
#      / /_/ // /_ / / / //  __// /      / /  / / / // // / / // /_/ /(__  )        #
#      \____/ \__//_/ /_/ \___//_/      /_/  /_/ /_//_//_/ /_/ \__, //____/         #
#                                                             /____/                #
#####################################################################################
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
main = None
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
        margin=9,
        border_focus="cce6ff",
        border_normal="0059b3",
        border_on_single=True,
        border_width= 5,



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





# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java"s whitelist.
wmname = "LG3D"
