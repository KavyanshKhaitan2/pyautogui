"""
To Implement:
[x] _position
[ ] _size
[ ] _vscroll
[ ] _hscroll
[ ] _scroll
[ ] _click
[ ] _mouse_is_swapped
[ ] _moveTo
[ ] _mouseDown
[ ] _mouseUp
[ ] _keyDown
[ ] _keyUp
[ ] 
"""

import pyautogui
import sys
import os
import subprocess
from pyautogui import LEFT, MIDDLE, RIGHT

import wayland_automation

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
