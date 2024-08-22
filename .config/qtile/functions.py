
#from config import colordict
from qtile_extras.widget import decorations
import subprocess 
import os
import json
from libqtile import qtile
from qtile_extras import widget, layout
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupText, PopupImage ,PopupWidget,PopupGridLayout
from libqtile.lazy import lazy




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
############################
#     _       __          #
#    | |     / _|         #
#  __| | ___| |_   ___    #
# / _` |/ _ \  _| / __|   #
#| (_| |  __/ |   \__ \   #
# \__,_|\___|_|   |___/   #
#                         #
###########################
def create_icon(filename, row, col):
    return PopupImage(
        filename=filename,
        row=row,
        col=col,
    )

# Define a function to create a text label with associated action
def create_label(text, row, col, command, font="Iosevka NF SemiBold",fontsize=15,foreground_highlighted=Color0,highlight=Color7,highlight_radius=9,highlight_border=5,):
    return PopupText(
        text=text,
        row=row,
        col=col,
        col_span=9,  # Span across 6 columns
        mouse_callbacks={"Button1": lazy.spawn(command)},
        font=font,
        fontsize=fontsize,
        foreground_highlighted=foreground_highlighted,
        highlight=highlight,
        highlight_radius=highlight_radius,
        highlight_border=highlight_border,
    )

def qtile_menu(qtile):
    controls = [
        create_icon("~/.local/share/icons/Deepin2022-Dark/scalable@2x/apps/firefox.svg", 0, 0),
        create_icon("~/.local/share/icons/Deepin2022-Dark/scalable@2x/apps/file-manager.svg", 1, 0 ),
        create_icon("~/.local/share/icons/hicolor/24x24/apps/lvim.svg", 2, 0, ),
        create_icon("~/.local/share/icons/Deepin2022-Dark/scalable@2x/apps/kitty.svg", 3, 0 ),
        
        create_label(" Browser", 0, 1, "firefox"),
        create_label(" File Manager", 1, 1, "nemo"),
        create_label(" Text Editor", 2, 1, "kitty -e lvim"),
        create_label(" Terminal", 3, 1, "kitty"),
        create_label(" Reload config", 4, 1, "qtile cmd-obj -o root -f reload_config"),
        PopupText(" ",row=4,col=0,col_span=1,font="Iosevka NF SemiBold",fontsize=16)
    ]

    layout = PopupGridLayout(
        qtile,
        rows=5,  # Adjust rows dynamically
        cols=10,
        height=170,
        width=200,
        controls=controls,
        border_width=3,
        border=Color7,
        background=Color1,
        hide_on_timeout=4,
        hide_interval=1,
    )
    layout.show(x=8, y=38,hide_on_timeout=4,)



"""
def qtile_menu(qtile):

    menu_items = [
        ("~/.local/share/icons/Deepin2022-Dark/scalable@2x/apps/com.brave.Browser.svg", " Browser", "com.brave.Browser"),
        ("~/.local/share/icons/Deepin2022-Dark/scalable@2x/apps/file-manager.svg", " file Manager", "nemo"),
        ("~/.local/share/icons/hicolor/24x24/apps/lvim.svg", " Text Editor", "kitty -e lvim"),
        ("~/.local/share/icons/Deepin2022-Dark/scalable@2x/apps/kitty.svg", " Terminal", "kitty"),
    ]
    controls = []
    for row, (icon, text, command) in enumerate(menu_items):
        callbacks = {"Button1": lazy.spawn(command)}
        controls.extend([
            PopupText("", row=row, col=0, col_span=10, background=Color2, mouse_callbacks=callbacks),  # Highlight background
            PopupImage(filename=icon, row=row, col=1, mouse_callbacks=callbacks),
            PopupText(text, row=row, col=2, col_span=6, font="Iosevka NF SemiBold", mouse_callbacks=callbacks),
        ])

    # Add the "Reload config" option
    controls.append(PopupText("   Reload config", row=4, col=1, col_span=6, 
                              mouse_callbacks={"Button1": lazy.spawn("qtile cmd-obj -o root -f reload_config")},
                              font="Iosevka NF SemiBold"))

    layout = PopupGridLayout(
        qtile,
        rows=5, cols=10,
        height=170, width=200,
        controls=controls,
        border_width=3, border=Color7,
        background=Color1
    )
    layout.show(x=8, y=38)

    controls=[
        #PopupWidget(
         #   row=0,col=1,
          #  col_span=9,
           # widget=widget.WidgetBox(
            #    widgets=[
             #       widget.Image(filename="~/.local/share/icons/Deepin2022-Dark/scalable@2x/apps/com.brave.Browser.svg"),
              #      widget.TextBox(text="Browser")
               #     ],
                #start_opened=True,text_open="",text_close="",close_button_location="right"),
                 #),
        #row=0,col=9,mouse_callbacks={"Button1":lazy.spawn("com.brave.Browser")}), 
        PopupImage(filename="~/.local/share/icons/Deepin2022-Dark/scalable@2x/apps/brave.svg",row=0,col=1,mouse_callbacks={"Button1":lazy.spawn("com.brave.Browser")}),
        PopupImage(filename="~/.local/share/icons/Deepin2022-Dark/scalable@2x/apps/file-manager.svg",row=1,col=1,mouse_callbacks={"Button1":lazy.spawn("nemo")}),
        PopupImage(filename="~/.local/share/icons/hicolor/24x24/apps/lvim.svg",row=2,col=1,mouse_callbacks={"Button1":lazy.spawn("kitty -e lvim")}),
        PopupImage(filename="~/.local/share/icons/Deepin2022-Dark/scalable@2x/apps/kitty.svg",row=3,col=1,mouse_callbacks={"Button1":lazy.spawn("kitty")}),
        PopupText(" Browser",row=0,col=2,col_span=6,mouse_callbacks={"Button1":lazy.spawn("com.brave.Browser")},font="Iosevka NF SemiBold"),
        PopupText(" file Manager",row=1,col=2,col_span=6,mouse_callbacks={"Button1":lazy.spawn("nemo")},font="Iosevka NF SemiBold",),
        PopupText(" Text Editor",row=2,col=2,col_span=6,mouse_callbacks={"Button1":lazy.spawn("kitty -e lvim")},font="Iosevka NF SemiBold",),
        PopupText(" Terminal",row=3,col=2,col_span=6,mouse_callbacks={"Button1":lazy.spawn("kitty")},font="Iosevka NF SemiBold",),
        PopupText("   Reload config",row=4,col=1,col_span=6,mouse_callbacks={"Button1":lazy.spawn("qtile cmd-obj -o root -f reload_config")},font="Iosevka NF SemiBold",), 
    ]
    layout=PopupGridLayout(
            qtile,
            
            rows=5,cols=10,
            height=170,width=200,
            controls=controls,
            border_width=3,border=Color7,
            background=Color1
    )
    layout.show(x=8,y=38)
"""


######################################
def chooser(option):
    def choose(qtile):
        action =None
        if option == "logout":
            action = lazy.shutdown()
        elif option == "suspend":
            action = lazy.spawn("systemctl suspend")
        elif option == "poweroff":
            action = lazy.spawn("poweroff")
        are_you_sure(qtile, action)
    return choose
#######################################
def show_power_menu(qtile):
    time=subprocess.check_output("uptime -p | awk '{print \"Uptime: \" $2, $3, $4, $5}'", shell=True, text=True)
    time=time.strip()
    controls_p = [

        PopupImage(
            filename="/home/nizar/.local/share/icons/Deepin2022-Dark/32@2x/actions/system-log-out.svg",
            pos_x=0.125,
            pos_y=0.3,
            width=0.14,
            height=0.5,
            highlight=Color1,
            highlight_border=-15,
            highlight_radius=57,
            mouse_callbacks={
                "Button1": lazy.function(chooser("logout")) 
            }
        ),
        PopupImage(
            filename="/home/nizar/.local/share/icons/Deepin2022-Dark/32@2x/actions/system-suspend.svg",
            pos_x=0.43,
            pos_y=0.3,
            width=0.14,
            height=0.5,
            highlight=Color1,
            highlight_border=-15,
            highlight_radius=57,
            mouse_callbacks={
                "Button1": lazy.function(chooser("suspend"))
            }
        ),
        PopupImage(
             filename="/home/nizar/.local/share/icons/Deepin2022-Dark/32@2x/actions/system-shutdown.svg",
             pos_x=0.735,
             pos_y=0.3,
             width=0.14,
            height=0.5,
            highlight_border=-15,
            highlight_radius=57,
            highlight="A00000",
            mouse_callbacks={
                "Button1": lazy.function(chooser("poweroff"))
            }
         ),

        PopupWidget(
            widget=widget.TextBox(
                text=time,
                padding=60,
                foreground="#ffffff",
                #background=Color9,
                fontsize=16,
                markup=True,
                decorations=[
                    RectDecoration(
                    colour=Color1,
                    radius=[0,0,11,11],
                    filled=True,
                    extrawidth=0,
                    padding_x=20
                    #group=True
                    )
                ]
            ),

            pos_x=0.25,
            pos_y=-0.05,
            width=0.5,
            height=0.28,
        ),

    ]

    layout = PopupRelativeLayout(
        qtile,
        width=700,
        border_width=3,
        border=Color1,
        height=200,
        controls=controls_p,
        background="00000060",
        initial_focus=None,

    )

    layout.show(centered=True)


def are_you_sure(qtile,action):
    qtile.spawn("ffplay -nodisp -autoexit /usr/share/sounds/ocean/stereo/dialog-question.oga")
    controls_sure=[
        PopupWidget(
            widget=widget.TextBox(
                "  Are you sure about that?",
                foreground="#ffffff",
                background=Color1,
                fontsize=21,
                padding=60,
                ),
            pos_x=-0.02,
            pos_y=0.1,
            width=1.05,
            height=0.2,
            h_align="center"
        ),

        PopupText(
            fontsize=20,
            text="Yes",
            pos_x=0.2,
            h_align="center",
            pos_y=0.5,
            width=0.2,
            height=0.3,
            highlight=Color1,
            highlight_method="block",
            mouse_callbacks={
                "Button1": action
            }
        ),

        PopupText(
            fontsize=20,
            text="No",
            pos_x=0.6,
            h_align="center",
            pos_y=0.5,
            width=0.2,
            height=0.3,
            highlight=Color1,
            highlight_method="block",
            mouse_callbacks={
                "Button1":lazy.spawn("") }  )
        ]
    layout_sure = PopupRelativeLayout(
        qtile,
        width=400,
        hight=170,
        controls=controls_sure,
        background="0000007f",
        border_width=3,
        border=Color1,
    )
    layout_sure.show(centered=True)

def keylay(qtile):
    thelay = subprocess.check_output("setxkbmap -query | grep layout | awk '{print $2}' | tr 'a-z' 'A-z'", shell=True, text=True)
    thelay = "󰌌  : "+thelay.strip()
    controls_kb=[
        PopupText(
            text=thelay,
            font="Iosevka NF SemiBold",
            fontsize=22,
            pos_x=0.0,
            pos_y=0.0,
            height=1,
            width=1,
            #v_align="middle",
            h_align="center",
            ),


    ]
    layout_kb= PopupRelativeLayout(
        qtile,
        width=200,
        height=60,
        background=Color1,
        border=Color7,
        border_width=2,
        controls=controls_kb,
        close_on_click=True,
        hide_on_timeout=2,
    )
    layout_kb.show(x=860,y=140)
