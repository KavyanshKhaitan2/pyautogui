"""
To Implement:
[x] _position: Return xy coordinates of mouse
[x] _size: Return screen size
[x] _vscroll: Vertical mouse scroll
[x] _hscroll: Horizontal mouse scroll
[x] _scroll: Mouse scroll
[x] _click: Mouse click
[ ] _mouse_is_swapped: Check if LR mouse buttons are swapped.
[x] _moveTo: Moves the mouse cursor to a point on the screen
[x] _mouseDown: Mouse Down
[x] _mouseUp: Mouse Up (if mouse is down)
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
import pydotool
from pydotool import ClickEnum
from PIL import Image

pydotool.init()


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


def _size():
    im: Image.Image = pyscreenshot.grab()
    return im.size


def _moveTo(x, y):
    pydotool.mouse_move((x, y), True)


def _vscroll(clicks, x=None, y=None):
    clicks = int(clicks)
    if clicks == 0:
        return

    if x is not None and y is not None:
        _moveTo(x, y)

    subprocess.run(["ydotool", "scroll", "0", clicks])


def _hscroll(clicks, x=None, y=None):
    clicks = int(clicks)
    if clicks == 0:
        return

    if x is not None and y is not None:
        _moveTo(x, y)

    subprocess.run(["ydotool", "scroll", clicks, "0"])


def _scroll(clicks, x=None, y=None):
    return _vscroll(clicks, x, y)


def _click(x, y, button):
    assert button in (LEFT, MIDDLE, RIGHT), "button arg to _click() must be one of 'left', 'middle', or 'right'"

    _moveTo(x, y)
    if button == LEFT:
        pydotool.left_click()
    if button == MIDDLE:
        pydotool.click(ClickEnum.MIDDLE+ClickEnum.MOUSE_CLICK)
    if button == RIGHT:
        pydotool.right_click()

def _mouse_is_swapped():
    # TODO: Cant figure out how to get this, so assuming the value is False.
    return False

def _mouseDown(x, y, button):
    assert button in (LEFT, MIDDLE, RIGHT), "button arg to _click() must be one of 'left', 'middle', or 'right'"

    _moveTo(x, y)
    if button == LEFT:
        pydotool.click(ClickEnum.LEFT+ClickEnum.MOUSE_DOWN)
    if button == MIDDLE:
        pydotool.click(ClickEnum.MIDDLE+ClickEnum.MOUSE_DOWN)
    if button == RIGHT:
        pydotool.click(ClickEnum.RIGHT+ClickEnum.MOUSE_DOWN)

def _mouseUp(x, y, button):
    assert button in (LEFT, MIDDLE, RIGHT), "button arg to _click() must be one of 'left', 'middle', or 'right'"

    _moveTo(x, y)
    if button == LEFT:
        pydotool.click(ClickEnum.LEFT+ClickEnum.MOUSE_UP)
    if button == MIDDLE:
        pydotool.click(ClickEnum.MIDDLE+ClickEnum.MOUSE_UP)
    if button == RIGHT:
        pydotool.click(ClickEnum.RIGHT+ClickEnum.MOUSE_UP)

