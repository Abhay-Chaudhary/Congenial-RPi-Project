import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

w = Gtk.Window()
screen = w.get_screen()
screen_width = screen.get_width()
screen_height = screen.get_height()

# CAMERA CONFIGURATION
_img_dir = '/home/pi/Pictures/'
_img_prefix = 'sample_image_'
_img_resolution = (640, 480)
_img_format = 'jpeg'
_log_file_name = 'camera_log.txt'

next_img_index = 1