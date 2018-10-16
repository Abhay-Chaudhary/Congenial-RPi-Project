import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import os

from constants import _img_dir, _img_prefix, _img_resolution, _img_format, _log_file_name, next_img_index, screen_width, screen_height
from camera_control import *
from led_control import *


log_file = open(_log_file_name, 'w+')

def on_button_toggled(button, name):
    """
    GTK ToggleButton click handling
    :param button: Instance of button object which has been clicked
    :param name: Unique identity name of button (not its label)
    :return:
    """
    if name == "visible":
        if button.get_active():
            # IF VISIBLE LIGHT'S BUTTON IS CLICKED, AND ITS STATE IS PRESSED, TURN ON VISIBLE LEDs
            turn_on_visible_led()
        else:
            turn_off_visible_led()
    elif name == "ir":
        if button.get_active():
            turn_on_ir_led()
        else:
            turn_off_ir_led()


# MANAGES UI OF WINDOW WITH BUTTONS
class ToggleButtonWindow(Gtk.Window):

    def __init__(self):
        
        Gtk.Window.__init__(self, title="NIR Camera")
        self.set_border_width(10)
        self.move(round(screen_width*0.5), round(screen_height*0.75))

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.ToggleButton("Visible LED")
        button.connect("toggled", on_button_toggled, "visible")
        hbox.pack_start(button, True, True, 0)

        button = Gtk.ToggleButton("IR LED")
        button.connect("toggled", on_button_toggled, "ir")
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("Preview")
        button.connect("clicked", preview)
        hbox.pack_start(button, True, True, 0)
        
        button = Gtk.Button.new_with_label("Capture")
        button.connect("clicked", capture)
        hbox.pack_start(button, True, True, 0)

def setup():
    """
    Initialize image directory
    :return:
    """
    # check whether the image directory exists. if not create one
    if not os.path.isdir(_img_dir):
        os.mkdir(_img_dir)

    # turn off both LEDs initially
    turn_off_visible_led()
    turn_off_ir_led()


# INITIALIZE CAMERA & RPi
setup()
# GET NUMBER OF FILES IN IMAGE DIRECTORY
next_img_index = get_next_image_index(_img_dir)

# SETUP GUI FOR BUTTONS
win = ToggleButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

# CLOSE FILE WHEN PROGRAM ENDS
log_file.write('Exiting\n')
log_file.close()
close_camera()