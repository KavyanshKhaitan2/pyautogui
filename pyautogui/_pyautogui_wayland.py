"""
To Implement:
[x] _position: Return xy coordinates of mouse
[ ] _size: Return screen size
[ ] _vscroll: Vertical mouse scroll
[ ] _hscroll: Horizontal mouse scroll
[ ] _scroll: Mouse scroll
[ ] _click: Mouse click
[ ] _mouse_is_swapped: Check if LR mouse buttons are swapped.
[ ] _moveTo: Moves the mouse cursor to a point on the screen
[ ] _mouseDown: Mouse Down
[ ] _mouseUp: Mouse Up (if mouse is down)
[ ] _keyDown: Key Down
[ ] _keyUp: Key Up (if key is down)
"""

import pyautogui
import sys
import os
import subprocess
from pyautogui import LEFT, MIDDLE, RIGHT

import wayland_automation
import pyscreenshot

def _position():
    """Returns the current xy coordinates of the mouse cursor as a two-integer
    tuple.

    Returns:
        (x, y) tuple of the current xy coordinates of the mouse cursor.
    """
    gen = wayland_automation.mouse_position_generator()
    pos = next(gen)
    gen.close()
    return pos
