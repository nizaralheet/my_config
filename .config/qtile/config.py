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
#import copy
import subprocess
import json
import qtile_extras.hook
from libqtile import bar, qtile, extension ,hook
from qtile_extras import widget ,layout 
from qtile_extras.widget import decorations
from qtile_extras.widget.decorations import RectDecoration
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import send_notification
from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupSlider, PopupText, PopupImage ,PopupWidget ,PopupAbsoluteLayout
from functions import keylay ,show_power_menu , qtile_menu
#from qtile_extras.widget import decorations


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


mod = "mod4"
alt = "mod1"
terminal = "kitty"
home= os.path.expanduser("~")

##############################
# _                 _        #
#| |__   ___   ___ | | _____ #
#| '_ \ / _ \ / _ \| |/ / __|#
#| | | | (_) | (_) |   <\__ \#
#|_| |_|\___/ \___/|_|\_\___/#
##############################p
# this hook is wierd af

#@qtile_extras.hook.subscribe.up_battery_full
# def battery_full(battery_name):
#    send_notification("Power HQ",  "Battery is fully charged.")


@qtile_extras.hook.subscribe.up_battery_low
def battery_low():
    send_notification("Power HQ", "Battery is running low.")

@qtile_extras.hook.subscribe.up_battery_critical
def battery_critical():
    send_notification("Power HQ","Battery is critically low. Plug in power cable.")

@hook.subscribe.startup_complete
def run_every_startup():
    send_notification("Qtile", "config realoading is done.")

@qtile_extras.hook.subscribe.up_power_connected
def plugged_in():
    send_notification("Power HQ","The power have been pluged in , Charging Up")
    qtile.spawn("ffplay -nodisp -autoexit /usr/share/sounds/ocean/stereo/power-plug.oga")
@qtile_extras.hook.subscribe.up_power_disconnected
def unplugged():
    send_notification("Power HQ", "The power cable is disconnected , Discharging")
    qtile.spawn("ffplay -nodisp -autoexit /usr/share/sounds/ocean/stereo/power-unplug.oga")


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("/home/nizar/.config/qtile/autostart.sh")
    subprocess.Popen([home])
    send_notification("Welcome","What are you gonna do today?")
    lazy.spawn("sleep 2 ; ffplay -nodisp -autoexit /usr/share/sounds/ocean/stereo/desktop-login.oga")
@hook.subscribe.resume
def wakeup():
    send_notification("Welcome Back !","The system successfully awaken form sleep")


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
   # i have the keys binded to the keycode so isntall xorg-xev to see all keys , thats becasuse i use more than one keyboard layout
    Key([mod],26,
        lazy.spawn("nemo"),desc="mod+e open nemo"
    ),
    Key([alt],"Tab",lazy.run_extension(
        extension.WindowList(dmenu_command="rofi -show window")),desc="alt+tab opens rofi window"
    ),
    Key([mod],59,
         lazy.spawn("rofi -show emoji -modi emoji"),desc="mod+comma opens rofi emojis"
    ),
    # that is for my clipboard add yours
    Key([mod],55,
        lazy.spawn("copyq show"),desc="mod+v shows copyq clipboard"
    ),
    # this to change the keyboardlayout if you are multi laguage you could change the lang at keyboardlayout widget
    Key([alt], "Shift_L",
        lazy.widget["keyboardlayout"].next_keyboard(),
        lazy.function(keylay),desc="this is the function that make the languag layout pop up"
    ),

    # here is the brightness control
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +5%"),desc="raise the brighteness level"

    ),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 5%-"),desc="lower the brighteness level"
    ),
    # audion control
    Key([], "XF86AudioMute",
        lazy.spawn("pamixer -t"),desc="mute the volume"

    ),

    Key([], "XF86AudioLowerVolume",
        lazy.spawn("pamixer -d 5"),
        lazy.spawn(" ffplay -nodisp -autoexit /usr/share/sounds/ocean/stereo/audio-volume-change.oga"),desc="lower the volume"
    ),

    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("pamixer -i 5"),
        lazy.spawn(" ffplay -nodisp -autoexit /usr/share/sounds/ocean/stereo/audio-volume-change.oga"),desc="raising the volume"
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
        [mod], 57,
        lazy.layout.normalize(), desc="mod + n Reset all window sizes"
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
        [mod],25,
        lazy.window.kill(), desc="mod+w Kill focused window"
    ),

    Key(
        [mod],41,
        lazy.window.toggle_fullscreen(),desc="mod+f Toggle fullscreen",
    ),

    Key(
        [mod], 28,
        lazy.window.toggle_floating(), desc="mod +t Toggle floating"
    ),

    Key(
        [mod, "control"], 27,
        lazy.reload_config(), desc="mod +ctrl + r Reload the config"
    ),

    Key(
        [mod, "control"], 24,
        lazy.shutdown(), desc="mod + ctrl +q Shutdown Qtile"
    ),
    Key(
        [mod], 27,
        lazy.spawn("rofi -show drun"), desc="mod +r Spawn rofi app laucher"
    ),
    # edit and add the browser you use
    Key(
        [mod], 56,
        lazy.spawn("firefox"), desc="mod +b spawn brave browser"
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
                desc="Switch to & move focused window to group ",
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
    layout.MonadTall(
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
    ),
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
    font="Iosevka NF SemiBold",
    foreground="#fff",
    fontsize=15,
    padding=3,
)

 
extension_defaults = widget_defaults.copy()

circle = {
    "decorations": [
        RectDecoration(colour=Color1,
            radius=10,#[0,11,0,11],
            filled=True,
            extrawidth=0,
            group=True
        )
    ]
}
circle1 = {
    "decorations": [
        RectDecoration(colour=Color1,
            radius=10,#[0,11,0,11],
            filled=True,
            extrawidth=0,
            group=True
        ),
        RectDecoration(colour="#800000",
            radius=8,
            filled=True,
            padding_y=3,
            group=False
        )


    ]
}
circle2={
    "decorations":[
            RectDecoration(colour=Color1,
                radius=10,#[0,11,0,11],
                filled=True,
                extrawidth=0,
                group=True
            ),
            RectDecoration(colour=Color7,
                radius=8,#[0,11,0,11],
                filled=True,
                padding_y=3,
                extrawidth=0,
                group=False,
            ),
        ]
    }

VOLUME_POPUP = PopupRelativeLayout(

    width=200,
    height=50,
    background=Color1,
    border=Color7,
    border_width=2,
    controls=[
        PopupText(
            text="Volume:",
            name="text",
            font="SourceCodePro",
            pos_x=0.1,
            pos_y=0,
            height=0.4,
            width=0.8,
            v_align="middle",
            h_align="center",
        ),
        PopupSlider(
            name="volume",
            pos_x=0.1,
            pos_y=0.3,
            width=0.8,
            height=0.5,
            colour_below=Color7,
            bar_border_colour=Color7,
            bar_border_size=2,
            bar_border_margin=-2,
            bar_size=7,
            marker_size=0,
            end_margin=0,
        ),
    ],
)



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
                widget.PulseVolumeExtra(step=5,mode="popup",popup_layout=VOLUME_POPUP,limit_max_volume=True,),

                widget.Spacer(
                    width=10,
                    length=0,
                    background="#00000070",
                ),
                
                widget.Spacer(length=7,**circle,background="#00000070"),
                widget.TextBox(

                    "     ",
                    foreground=Color0,
                    **circle2,
                    fontsize=15,
                    mouse_callbacks={"Button1":lazy.function(qtile_menu)}
                    ),
                
                widget.Spacer(length=9,**circle,background="#00000070"),
                widget.CurrentLayoutIcon(
                    **circle,
                    scale=0.8,
                ),
                widget.GroupBox(
                    font="SauceCodePro NFM Medium",
                    fontsize=21,
                    active="ffffff",
                    background="#00000070",
                    highlight_method="block",
                    inactive = Color15,
                    block_highlight_text_color=Color0,
                    this_current_screen_border=Color7,
                    padding_y=-3,
                    padding_x=4,
                    margin_x=3,
                    **circle,
                    center_aligned=True,
                    max_chars=50,
                ),
                widget.Spacer(length=7,**circle,background="#00000070"),





                
                widget.WindowName(
                    padding=10,
                    background="#00000070",
                    format="   {state}{name}",
                    empty_group_string="What a great wallpaper...",
                ),
                

                #widget.TaskList(),
                                widget.Spacer(
                    width=7,
                    length=7,
                    background="#00000070",
                ),
                
                widget.Spacer(length=6,**circle,background="#00000070"),
                widget.Clock(
                    fontsize=16,
                    format="󰸗 %a %d %b " ,
                    background="00000070", 
                    #foreground=Color0,
                    spacing="2",

                    **circle
                ),
                widget.Clock(
                    fontsize=16,
                    format=" 󰥔 %I:%M %p " ,
                    background="00000070",
                    foreground=Color0,
                    padding=2,

                    **circle2
                ),
                #widget.Spacer(length=6,**circle,background="#00000070"),
                widget.OpenWeather(
                    app_key = "4cf3731a25d1d1f4e4a00207afd451a2",
                    cityid = "250441",#serch your city here https://openweathermap.org/find and you gonna find the id at the link like this for london https://openweathermap.org/city/2643743
                    format = " {weather} {icon} {main_temp:.0f}°C",
                    metric = True,
                    padding=5,
                    fontsize = 16,
                    weather_symbols={
                        "Unknown": "",
                        "01d": " ",
                        "01n": " ",
                        "02d": "",
                        "02n": " ",
                        "03d": " ",
                        "03n": " ",
                        "04d": " ",
                        "04n": " ",
                        "09d": "⛆ ",
                        "09n": "⛆ ",
                        "10d": "",
                        "10n": " ",
                        "11d": "🌩",
                        "11n": "🌩",
                        "13d": "❄",
                        "13n": "❄",
                        "50d": "🌫",
                        "50n": "🌫",
                    },
                    background = "00000070",
                    **circle
                ),

                widget.Spacer(**circle,length=5,background="00000070"),

                widget.Spacer(length = bar.STRETCH,background="#00000070"),



                widget.TextBox(
                    fontsize=16,
                    text="  ",
                    background="#00000070",
                    mouse_callbacks=Btop,
                    **circle
                ),

                widget.Memory(
                    mouse_callbacks=Btop,
                    background="#00000070",
                    format="{MemPercent:.0f}% ",
                    **circle
                ),
                widget.TextBox(
                    mouse_callbacks=Btop,
                    fontsize=19,
                    text="󰍛 ",
                    background="#00000070",
                    **circle
                ),
                widget.Spacer(length=-6,**circle),
                widget.CPU(
                    mouse_callbacks=Btop,
                    background="#00000070",
                    format= "{load_percent:.0f}%",
                    update_interval=1,
                    **circle
                ),
               
                widget.ThermalSensor(
                    mouse_callbacks=Btop,
                    background="#00000070",
                    format=" 󰔏 {temp:.0f}{unit} ",
                    tag_sensor="Core 0",
                    update_interval=1,
                    threshold=80,
                    foreground_alert="800000",
                    **circle,
                ),
                widget.Spacer(length=7,background="#00000070"), 

                widget.Spacer(length=7,**circle),
                widget.WidgetBox(

                widgets=[
                    widget.TextBox(
                        text="󱅫 ",
                        **circle,
                        mouse_callbacks={"Button1":lazy.spawn("dunstctl history-pop")}
                    ),
                    widget.CheckUpdates(
                        distro="Arch_checkupdates",
                        no_update_string="",
                        background="#00000070", 
                        colour_have_updates="ffffff",
                        colour_no_updates="ffffff",
                        fontsize=15,
                        display_format=" !{updates}",
                        mouse_callbacks={"Button1":lazy.spawn("kitty ./.config/qtile/update.sh")},
                        **circle,
                    ),
                    widget.StatusNotifier(
                        highlight_colour=Color7,
                        menu_foreground=Color7,
                        menu_foreground_highlighted=Color0,
                        menu_background=Color1,
                        separator_colour=Color7,
                        menu_offset_y=10,
                        padding=7,
                        **circle,
                        icon_size=20,
                        icon_theme="Tela circle dark"
                    ),
                    ],
                **circle2,
                close_button_location="right",
                text_closed="  ",
                text_open="  ",
                foreground=Color0,
                ),

                widget.Spacer(length=9,**circle),

                widget.PulseVolume(
                    **circle,
                    icon_size=20,
                    theme_path="/home/nizar/.local/share/icons/Breeze-Noir-White-Blue/status/22/",
                ),

                widget.Spacer(length=-8,**circle),

                widget.PulseVolumeExtra(
                    **circle,
                    mode="bar",
                    bar_colour_high=Color1,
                    bar_colour_loud=Color1,
                    bar_colour_mute=Color1,
                    bar_colour_normal=Color1,
                    bar_width=40,

                    unmute_format='{volume}% ',
                    fontsize=15
                ),
                 widget.KeyboardLayout(
                    configured_keyboards=['us','ara'],
                    background="#00000070",
                    padding=7,
                    **circle
                ),


                widget.WiFiIcon(
                    background="#00000070",
                    active_colour="#E1E1E1",
                    padding_x=7,
                    padding_y=3,
                    **circle
                ),

                widget.UPowerWidget(
                    background = "#00000070",
                    border_colour = "#ffffff",
                    border_critical_colour = "#cc0000",
                    border_charge_colour = "#ffffff",
                    fill_low = "#ffff00",
                    fill_charge = "#00cc66",
                    fill_critical = "#cc0000",
                    fill_normal = "#ffffff",
                    percentage_low = 0.4,
                    percentage_critical = 0.2,
                    text_charging="({percentage:.0f}%)",
                    text_discharging="{percentage:.0f}%",
                    text_displaytime=3666,
                    battery_height=13,
                    battery_width=27,
                    spacing=6,
                    **circle,
                ),

                
                widget.Spacer(length=7,**circle,background="#00000070"), 

                
                
                widget.TextBox(
                        "⏻ ",
                        **circle1,
                        padding=20,
                        fontsize=15,
                        mouse_callbacks={"Button1":lazy.function(show_power_menu)}
                ),

                widget.Spacer(length=6,**circle,background="#00000070"),

                widget.Spacer(
                    width=10,
                    length=0,
                    background="#00000070",
                ),

            ],

            25,
        #this ^^ is the bar hight 
            border_width=[0, 0,0,0],#Draw top and bottom borders
            border_color=[
                "#00000070",
                "0070cc",
                "#00000070", 
                "0070cc"
            ],
            x=0,
            y=0,
            width=1920,
            hight=1080,
            margin = [5,10,0,10],
              # Borders are magenta (UP,SIDE,DOWN,SIDE)
            opacity=1,
            background="00000070",
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
        Match(wm_class="qalculate-gtk"),  # gitk
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="copyq"),
        Match(wm_class="krunner"),
        Match(wm_class="plasma-emojier"),
        Match(wm_class="wpg"),
        Match(wm_class="lxappearance"),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="korganizer"),  # GPG key password entry

    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True



wmname = "LG3D"
