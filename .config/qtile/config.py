# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

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
import json
import qtile_extras.hook
from libqtile import bar, layout, qtile, hook
from qtile_extras import widget
#from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupSlider, PopupText, PopupWidget
from qtile_extras.widget.decorations import RectDecoration
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import send_notification
#from libqtile.widget import backlight



# here is the colors that we gonna use from pywal

colors = os.path.expanduser('~/.cache/wal/colors.json')
colordict = json.load(open(colors))
Color0=(colordict['colors']['color0'])
Color1=(colordict['colors']['color1'])
Color2=(colordict['colors']['color2'])
Color3=(colordict['colors']['color3'])
Color4=(colordict['colors']['color4'])
Color5=(colordict['colors']['color5'])
Color6=(colordict['colors']['color6'])
Color7=(colordict['colors']['color7'])
Color8=(colordict['colors']['color8'])
Color9=(colordict['colors']['color9'])
Color10=(colordict['colors']['color10'])
Color11=(colordict['colors']['color11'])
Color12=(colordict['colors']['color12'])
Color13=(colordict['colors']['color13'])
Color14=(colordict['colors']['color14'])
Color15=(colordict['colors']['color15'])

Btop=({"Button1":lazy.spawn("kitty -e btop")})

# this hooks need to work on



#@qtile_extras.hook.subscribe.up_battery_full
# def battery_full(battery_name):
#    send_notification("Power HQ",  "Battery is fully charged.")



@qtile_extras.hook.subscribe.up_battery_low
def battery_low(battery_name):
    send_notification("Power HQ", "Battery is running low.")

@qtile_extras.hook.subscribe.up_battery_critical
def battery_critical(battery_name):
    send_notification(battery_name, "Battery is critically low. Plug in power cable.")

@hook.subscribe.startup
def run_every_startup():
    send_notification("Qtile", "config realoading is done.")

@qtile_extras.hook.subscribe.up_power_connected
def plugged_in():
    send_notification("Power HQ","The power have been pluged in , Charging Up")
    #qtile.spawn("ffplay power_on.wav")

@qtile_extras.hook.subscribe.up_power_disconnected
def unplugged():
    send_notification("Power HQ", "The power cable is disconnected , Discharging")
    qtile.spawn("ffplay power_off.wav")


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("/home/nizar/.config/qtile/autostart.sh")
    subprocess.Popen([home])

mod = "mod4"
alt = "mod1"
terminal = "kitty"
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
    # that is for my clipboard add yours  
    Key([mod],"v",
        lazy.spawn("copyq show"),
    ),
    # this to change the keyboardlayout if you are multi laguage you could change the lang at keyboardlayout widget
    Key([alt], "Shift_L",  
        lazy.widget["keyboardlayout"].next_keyboard()
    ),

    # here is the brightness control
    Key([], "XF86MonBrightnessUp", 
        lazy.spawn("brightnessctl set +5%"),
    ),
    Key([], "XF86MonBrightnessDown", 
        lazy.spawn("brightnessctl set 5%-"),
    ),
    # audion control
    Key([], "XF86AudioMute",
        lazy.spawn("amixer -q set Master toggle")
        ),

    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer -c 0 sset Master 2- unmute")
    ),

    Key([], "XF86AudioRaiseVolume", 
        lazy.spawn("amixer -c 0 sset Master 2+ unmute")
    ),
    # for moving and changing window focus i use arrows if you are comfortable wiht hjkl you could edit it
    Key([mod], "Left", 
        lazy.layout.left(), 
        desc="Move focus to left"
    ),

    Key([mod], "Right",
        lazy.layout.right(), desc="Move focus to right"
    ),

    Key([mod], "Down", 
        lazy.layout.down(), desc="Move focus down"
    ),

    Key([mod], "Up", 
        lazy.layout.up(), desc="Move focus up"
    ),

    Key([mod], "space",
        lazy.layout.next(), desc="Move window focus to other window"
    ),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", 
        lazy.layout.shuffle_left(), desc="Move window to the left"
    ),

    Key([mod, "shift"], "Right", 
        lazy.layout.shuffle_right(), desc="Move window to the right"
    ),

    Key([mod, "shift"], "Down", 
        lazy.layout.shuffle_down(), desc="Move window down"
    ),

    Key([mod, "shift"], "Up", 
        lazy.layout.shuffle_up(), desc="Move window up"
    ),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(), desc="Grow window to the left"
    ),

    Key(
        [mod, "control"], "Right",
        lazy.layout.grow_right(), desc="Grow window to the right"
    ),

    Key(
        [mod, "control"],
        "Down", lazy.layout.grow_down(), desc="Grow window down"
    ),

    Key(
        [mod, "control"], "Up",
        lazy.layout.grow_up(), desc="Grow window up"
    ),

    Key(
        [mod], "n",
        lazy.layout.normalize(), desc="Reset all window sizes"
    ),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],"Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    Key(
        [mod], "Return",
        lazy.spawn("kitty"), desc="Launch terminal"
    ),

    # Toggle between different layouts as defined below
    Key(
        [mod], "Tab",
        lazy.next_layout(), desc="Toggle between layouts"
    ),

    Key(
        [mod],"w", 
        lazy.window.kill(), desc="Kill focused window"
    ),

    Key(
        [mod],"f",
        lazy.window.toggle_fullscreen(),desc="Toggle fullscreen",
    ),

    Key(
        [mod], "t",
        lazy.window.toggle_floating(), desc="Toggle floating"
    ),

    Key(
        [mod, "control"], "r",
        lazy.reload_config(), desc="Reload the config"
    ),

    Key(
        [mod, "control"], "q",
        lazy.shutdown(), desc="Shutdown Qtile"
    ),
    Key(
        [mod], "r",
        lazy.spawn("rofi -show drun"), desc="Spawn rofi app laucher"
    ),
    # edit and add the browser you use
    Key(
        [mod], "b",
        lazy.spawn("flatpak run com.brave.Browser"), desc="spawn brave browser"
    ),

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
    #Group("6",label= "⬠"),
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
     #layout.TreeTab(border_width=3, margin= 6, border_focus="ffffff", border_normal="ffff44", active_bg="99ccff", active_fg="ffffff",sections=[""]),
     #layout.VerticalTile(),
     #layout.Zoomy( margin=9,border_focus="cce6ff",border_normal="0059b3",border_on_single=True,border_width= 5),
    layout.Columns(
         margin=7,
         border_focus=Color7,
         border_normal=Color1,
         border_on_single=True,
         border_width= 2
    ),
    layout.Max(
         margin=7,
         border_focus=Color7,
         border_normal= Color1 ,
         border_width=2
    ),
    layout.Spiral(margin=7,
         border_focus=Color7,
         border_normal=Color1,
         border_on_single=True,
         border_width= 2
    )
    # layout.Floating( border_focus="#ffffff", border_normal= Color1 ,border_width=5),

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
    fontsize=14,
    padding=3,
)

 
extension_defaults = widget_defaults.copy()

circle = {
    "decorations": [
        RectDecoration(colour=Color1,
            radius=9,
            filled=True,
            extrawidth=0,
            group=True
        )
    ]
}
circle1 = {
    "decorations": [
        RectDecoration(colour=Color1,
            radius=9,
            filled=True,
            extrawidth=0,
            group=True
        ),
        RectDecoration(colour="#800000",
            radius=8,
            filled=True,
            padding_y=2,
            group=False
        )


    ]
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
        wallpaper="",#.config/qtile/wallpaper7.jpg",
        wallpaper_mode="fill",
        top=bar.Bar
        (
            [
                
                widget.Spacer(
                    width=7,
                    length=0,
                    background="0000007f",
                ),
                  
                
                
                widget.Clock(
                    format=" %I:%M %p ", 
                    background="0000007f", 
                    foreground="#ffffff",#Color7
                    spacing="2",
                    **circle
                ),
                
                  
                   
                   
                widget.Spacer(
                    width=7,
                    length=7,
                    background="0000007f",
                ),
                  
                   
                widget.Spacer(length=7,**circle,background="0000007f"),
                widget.CurrentLayoutIcon(
                    **circle,
                    scale=0.8,
                ),
                widget.GroupBox(
                    fontsize=21,
                    active="ffffff",
                    background="0000007f",
                    highlight_method="block",
                    inactive = Color8, 
                    block_highlight_text_color=Color0,
                    #highlight=Color4,
                    #highlight_color=[Color1,Color5],
                    this_current_screen_border=Color7,
                    padding_y=-3,
                    padding_x=4,
                    #rounded = True,
                    margin_x=3,
                    **circle,
                ),
                     
                widget.Spacer(length=7,**circle,background="0000007f"),


                widget.WindowName(
                    padding=10,
                    background="0000007f",
                    empty_group_string="What a great wallpaper...",
                ),
                


                widget.Spacer(length=5,**circle,background="0000007f"),
                widget.TextBox(
                    fontsize=14,
                    text=" ",
                    foreground="ffffff",
                    background="0000007f",
                    mouse_callbacks=Btop,
                    **circle
                ),
                
                widget.Memory(
                    mouse_callbacks=Btop,
                    background="0000007f",
                    foreground="#ffffff",
                    format=":{MemPercent}% ",
                    **circle
                ),
                widget.TextBox(
                    mouse_callbacks=Btop,
                    fontsize=19,
                    text=" 󰍛",
                    foreground="ffffff",
                    background="0000007f",
                    **circle
                ),
                widget.CPU(
                    mouse_callbacks=Btop,
                    background="0000007f",
                    foreground="#ffffff",
                    format= ":{load_percent}% ",
                    update_interval=1,
                    **circle
                ),
               
                widget.ThermalSensor(
                    mouse_callbacks=Btop,
                    background="0000007f",
                    foreground="ffffff",
                    format=" 󰔏 {temp:.1f}{unit} ",
                    tag_sensor="Core 0",
                    update_interval=1,
                    threshold=80,
                    foreground_alert="800000",
                    **circle,
                ),
                
                widget.Spacer(length=7,background="0000007f"),
                widget.Spacer(length=15,**circle,background="0000007f"),
                widget.UPowerWidget(
                    background = "0000007f",
                    border_colour = "#ffffff",
                    border_critical_colour = "#cc0000",
                    border_charge_colour = "#ffffff",
                    fill_low = "#ffff00",
                    fill_charge = "#00cc66",
                    fill_critical = "#cc0000",
                    fill_normal = "#ffffff",
                    percentage_low = 0.4,
                    percentage_critical = 0.2,
                    foreground="#ffffff",
                    text_charging="({percentage:.0f}%)",
                    text_discharging="{percentage:.0f}%",
                    text_displaytime=3666,
                    battery_height=13,
                    battery_width=27,
                    spacing=6,
                    **circle,
                ),

               
                widget.Spacer(length=5,**circle,background="0000007f"),
                widget.WiFiIcon(
                    background="0000007f",
                    active_colour="#E1E1E1",
                    foreground="#ffffff",
                    padding_x=7,
                    padding_y=3,
                    **circle
                ),
                #here you could add your language
                widget.KeyboardLayout(
                    configured_keyboards=['us'],
                    background="0000007f",
                    foreground="ffffff",
                    padding=7,
                    **circle
                ),

                
                #widget.Spacer(length=6,background="0000007f"),
                widget.PulseVolume(
                    **circle,
                    padding=7,
                    unmute_format=' {volume}%',
                    background="0000007f",
                    emoji=False,
                    volume_app='amixer',
                     
                ),
                #maybe this wouldnot work , check qtile docs and your backlight_name
                widget.Backlight(
                    fontsize=15,
                    backlight_name="intel_backlight",
                    **circle,
                    format='󰃠 {percent:2.0%}',
                    padding=5,
                    update_interval=0.1,
                ),

                widget.Spacer(length=7,**circle),
                widget.CheckUpdates(
                    distro="Arch_checkupdates",
                    no_update_string="No updates",
                    background="0000007f", 
                    foreground="ffffff",
                    colour_have_updates="ffffff",
                    colour_no_updates="ffffff",
                    display_format="Updates:{updates}",
                    mouse_callbacks={"Button1":lazy.spawn("kitty ./.config/qtile/update.sh")},
                    **circle,
                ),

                widget.Spacer(length=7,**circle,background="0000007f"),

                widget.Spacer(length=7,background="0000007f"),
                
                #widget.Spacer(length=5,background="0000007f",**circle),
                widget.OpenWeather(
                    app_key = "4cf3731a25d1d1f4e4a00207afd451a2",
                    cityid = "2643743",#serch your city here https://openweathermap.org/find and you gonna find the id at the link like this for london https://openweathermap.org/city/2643743
                    format = "{main_temp}°{icon}",
                    metric = True,
                    padding=5,
                    fontsize = 14,
                    background = "0000007f",
                    foreground = "#ffffff",
                    **circle
                ),

                widget.Clock(
                    format=" %d/%m ", 
                    background="0000007f", 
                    foreground="#ffffff",
                    spacing="2",
                    **circle
                ),


                widget.QuickExit(
                    countdown_format="[ {}  ]",
                    default_text="LOGOUT",
                    background="0000007f",
                    padding_x=3,
                    **circle1
                ),

                widget.Spacer(length=4,**circle,background="0000007f"),

                

            ],

            23,
        #this ^^ is the bar hight 
            border_width=[0, 0,0,0],#Draw top and bottom borders
            border_color=[
                "0000007f",
                "0060cc",
                "0000007f", 
                "0060cc"
            ],
            margin = [7,10,0,10],
              # Borders are magenta (UP,SIDE,DOWN,SIDE)
            opacity=1,
            background="0000007f",
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
         #x11_drag_polling_rate = 400,
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
        margin=7,
         border_focus="cce6ff",
         border_normal=Color1,
         border_on_single=True,
         border_width= 2,



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
