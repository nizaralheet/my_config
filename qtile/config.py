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
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#################################################################

#IMPORTS 

#################################################################
from libqtile import bar, layout, qtile, hook
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras.widget.decorations import RectDecoration
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal, send_notification

#from qtile_extras.popup.templates.mpris2 import COMPACT_LAYOUT, DEFAULT_LAYOUT

import os
import subprocess


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('/home/nizar/.config/qtile/autostart.sh')
    subprocess.Popen([home])

mod = "mod4"
terminal = "alacritty"
#################################################################

#KEYS

################################################################
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),

    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),

    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),

    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),

    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),

    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),

    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h",
        lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l",
        lazy.layout.grow_right(), desc="Grow window to the right"),
    Key(
        [mod, "control"],
        "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key(
        [mod, "control"], "k",
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
        lazy.spawn(terminal), desc="Launch terminal"),
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

]
#################################################################

#GROUPS

#################################################################
#groups = [Group(i) for i in "12345"]
#group_labels=['-','=','≡','△','□']
#group_name=['1','2','3','4','5']
groups = [
        Group('1',label= '-'),
        Group('2',label= '='),
        Group('3',label= '≡'),
        Group('4',label= '△'),
        Group('5',label= '□'),
        ]
#for i in range(len(group_name)):
 #   groups.append(
  #          Group(
   #             name=group_name[i],
    #            label=group_labels[i]
     #           ))
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
               desc="Switch to & move focused window to group {}".format(i.name),
           ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
            ]
    )
#################################################################

#LAYOUTS

#################################################################
layouts = [
      #Try more layouts by unleashing below layouts.
     #layout.Stack(num_stacks=2),
     #layout.Bsp(),
     #layout.Matrix(),
     #layout.MonadTall(margin=9, border_focus='cce6ff', border_normal='0059b3', border_on_single=True,border_width= 5),
     #layout.MonadWide(),
     #layout.RatioTile(),
     #layout.Tile(),
     #layout.TreeTab(border_width=3, margin= 6, border_focus="ffffff", border_normal="ffff44", active_bg='99ccff', active_fg='000000',sections=[""]),
     #layout.VerticalTile(),
     #layout.Zoomy(),
     layout.Columns(margin=9, border_focus='cce6ff', border_normal='0059b3', border_on_single=True,border_width= 5),
     layout.Max(margin=9, border_focus='cce6ff', border_normal='ffff44',border_width=5),
    # layout.Floating( border_focus='#ffffff', border_normal='#0059b3',border_width=5),

]
#################################################################

#WEDGET_DEFUALTS

#################################################################
widget_defaults = dict(
    font="Source Code Pro",
    fontsize=17,
    padding=3,
)
extension_defaults = widget_defaults.copy()
powerlinea = {
    "decorations": [
        PowerLineDecoration(path='forward_slash')
    ]
}
powerlineb = {
    "decorations": [
        PowerLineDecoration(path='back_slash')
    ]
}
roundshape = {
    "decorations": [
        RectDecoration(colour='#800000',
                       radius=10,
                       filled=True,
                       padding_y=1,
                       group=True)
    ],
    "padding": 10,
}
#################################################################

#SCREENS

#################################################################
screens = [
    Screen(
        wallpaper='/home/nizar/Downloads/55.jpg',
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                #widget.CurrentLayout(),
                widget.Spacer(
                    width=7,
                    length=7,
                    background='0080ff',
                    ),
 
                              
                widget.Image(
                    filename='/home/nizar/Downloads/logo.png',
                    scale=True,
                    margin_x=-3,
                    background='0080ff',
                    
                    ),

               widget.Spacer(
                    width=7,
                    length=7,
                    background='0080ff',
                    **powerlinea
                    ),
 

                widget.GroupBox(
                    fontsize=21,
                    active='000000',
                    background='0073e6',
                    highlight_method='line',
                    highlight_color=['0080ff','0059b3'],
                    this_current_screen_border="004080",
                    margin_x=-1,
                    **powerlinea,
                    ),


                widget.WindowName(
                    background="00000000",
                    **powerlineb,
                    empty_group_string='What a great wallpaper...',
                    ),

                widget.Chord(chords_colors={"launch": ("#ff0000", "#ffffff"),},name_transform=lambda name: name.upper(),),

                widget.CPU(
                    background='0062b3',
                    foreground='000000',
                    format= 'CPU:{load_percent}%',
                    **powerlineb
                    ),

                 widget.UPowerWidget(
                    background = "#0070cc",
                    border_colour = '#000000',
                    border_critical_colour = '#cc0000',
                    border_charge_colour = '#000000',
                    fill_low = '#ff6600',
                    fill_charge = '#00cc66',
                    fill_critical = '#cc0000',
                    fill_normal = '#3d3d29',
                    percentage_low = 0.4,
                    percentage_critical = 0.2,
                    foreground='#000000',
                    text_charging='({percentage:.0f}%)',
                    text_discharging='{percentage:.0f}%',
                    text_displaytime=3666,
                    battery_height=13,
                    battery_width=27,
                    **powerlineb
                    ),


                widget.CheckUpdates(
                    distro='Arch_Sup',
                    no_update_string='No updates',
                    background="#0073e6", 
                    foreground='000000',
                    colour_have_updates='000000',
                    colour_no_updates='000000',
                    display_format='Updates:{updates}',
                    **powerlineb,
                    ),


                #widget.ALSAWidget(mode='icon'),


               # widget.PulseVolume(),
               #widget.Mpris2(popup_layout=COMPACT_LAYOUT), 

                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),

                widget.Clock(
                        format=" %m/%d %I:%M%p ", 
                        background="0080ff", 
                        foreground="#000000",
                        spacing='2'
                        ),

                widget.QuickExit(
                        countdown_format='[   {}   ]',
                        default_text='SHUTDOWN',
                        background="0080ff",
                        padding_x='3',
                        **roundshape
                        ),
                 widget.Spacer(
                    width=7,
                    length=5,
                    background='0080ff',
                    ),


            ],

            24,
            #this ^ is the bar hight 
             border_width=[3, 0, 0, 0],#Draw top and bottom borders
              border_color=["0080ff",
                            "0060cc",
                            "00000000", 
                            "0060cc"
                            ],

              # Borders are magenta (UP,SIDE,DOWN,SIDE)
                opacity=1,
                background='ffffff00',
              ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
         x11_drag_polling_rate = 60,
    ),
]
#################################################################

#MOUSE

#################################################################
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
#################################################################

#OTHER THINGS

#################################################################
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(

        margin=9, border_focus='cce6ff', border_normal='0059b3', border_on_single=True,border_width= 5,



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

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
