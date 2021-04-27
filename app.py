# https://youtu.be/2RocXKPPx4o?t=302

from dearpygui.core import *
from dearpygui.simple import *

set_main_window_size(540, 720)
set_global_font_scale(1.25)
set_theme("Gold")

with window("Simple SMS Spam Filter", width=520, height=677):
    print("GUI is running ...")
    set_window_pos("Simple SMS Spam Filter", 0, 0)

start_dearpygui()
