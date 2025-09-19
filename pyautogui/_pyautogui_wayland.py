"""
To Implement:
(LAZY IMPLEMENT) [ ] _mouse_is_swapped: Check if LR mouse buttons are swapped.
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
    subprocess.run(["ydotool", "mousemove", "-a", "-x", x, "-y", y])


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
    assert button in (
        LEFT,
        MIDDLE,
        RIGHT,
    ), "button arg to _click() must be one of 'left', 'middle', or 'right'"

    _moveTo(x, y)
    if button == LEFT:
        pydotool.left_click()
    if button == MIDDLE:
        pydotool.click(ClickEnum.MIDDLE + ClickEnum.MOUSE_CLICK)
    if button == RIGHT:
        pydotool.right_click()


def _mouse_is_swapped():
    # TODO: Cant figure out how to get this, so assuming the value is False.
    return False


def _mouseDown(x, y, button):
    assert button in (
        LEFT,
        MIDDLE,
        RIGHT,
    ), "button arg to _click() must be one of 'left', 'middle', or 'right'"

    _moveTo(x, y)
    if button == LEFT:
        pydotool.click(ClickEnum.LEFT + ClickEnum.MOUSE_DOWN)
    if button == MIDDLE:
        pydotool.click(ClickEnum.MIDDLE + ClickEnum.MOUSE_DOWN)
    if button == RIGHT:
        pydotool.click(ClickEnum.RIGHT + ClickEnum.MOUSE_DOWN)


def _mouseUp(x, y, button):
    assert button in (
        LEFT,
        MIDDLE,
        RIGHT,
    ), "button arg to _click() must be one of 'left', 'middle', or 'right'"

    _moveTo(x, y)
    if button == LEFT:
        pydotool.click(ClickEnum.LEFT + ClickEnum.MOUSE_UP)
    if button == MIDDLE:
        pydotool.click(ClickEnum.MIDDLE + ClickEnum.MOUSE_UP)
    if button == RIGHT:
        pydotool.click(ClickEnum.RIGHT + ClickEnum.MOUSE_UP)


""" Information for keyboardMapping derived from PyKeyboard's special_key_assignment() function.

The *KB dictionaries in pyautogui map a string that can be passed to keyDown(),
keyUp(), or press() into the code used for the OS-specific keyboard function.

They should always be lowercase, and the same keys should be used across all OSes."""
keyboardMapping = dict([(key, None) for key in pyautogui.KEY_NAMES])
keyboardMapping.update(
    {
        "\t": pydotool.KEY_TAB,
        "\n": pydotool.KEY_ENTER,
        "\r": pydotool.KEY_ENTER,
        " ": pydotool.KEY_SPACE,
        "!": pydotool.KEY_1 | pydotool.FLAG_UPPERCASE,
        '"': pydotool.KEY_APOSTROPHE | pydotool.FLAG_UPPERCASE,
        "#": pydotool.KEY_3 | pydotool.FLAG_UPPERCASE,
        "$": pydotool.KEY_4 | pydotool.FLAG_UPPERCASE,
        "%": pydotool.KEY_5 | pydotool.FLAG_UPPERCASE,
        "&": pydotool.KEY_7 | pydotool.FLAG_UPPERCASE,
        "'": pydotool.KEY_APOSTROPHE,
        "(": pydotool.KEY_9 | pydotool.FLAG_UPPERCASE,
        ")": pydotool.KEY_0 | pydotool.FLAG_UPPERCASE,
        "*": pydotool.KEY_8 | pydotool.FLAG_UPPERCASE,
        "+": pydotool.KEY_EQUAL | pydotool.FLAG_UPPERCASE,
        ",": pydotool.KEY_COMMA,
        "-": pydotool.KEY_MINUS,
        ".": pydotool.KEY_DOT,
        "/": pydotool.KEY_DOT,
        "0": pydotool.KEY_0,
        "1": pydotool.KEY_1,
        "2": pydotool.KEY_2,
        "3": pydotool.KEY_3,
        "4": pydotool.KEY_4,
        "5": pydotool.KEY_5,
        "6": pydotool.KEY_6,
        "7": pydotool.KEY_7,
        "8": pydotool.KEY_8,
        "9": pydotool.KEY_9,
        ":": pydotool.KEY_SEMICOLON | pydotool.FLAG_UPPERCASE,
        ";": pydotool.KEY_SEMICOLON,
        "<": pydotool.KEY_COMMA | pydotool.FLAG_UPPERCASE,
        "=": pydotool.KEY_EQUAL,
        ">": pydotool.KEY_DOT | pydotool.FLAG_UPPERCASE,
        "?": pydotool.KEY_SLASH | pydotool.FLAG_UPPERCASE,
        "@": pydotool.KEY_2 | pydotool.FLAG_UPPERCASE,
        "[": pydotool.KEY_LEFTBRACE,
        "\\": pydotool.KEY_BACKSLASH,
        "]": pydotool.KEY_RIGHTBRACE,
        "^": pydotool.KEY_6 | pydotool.FLAG_UPPERCASE,
        "_": pydotool.KEY_MINUS | pydotool.FLAG_UPPERCASE,
        "`": pydotool.KEY_GRAVE,
        "a": pydotool.KEY_A,
        "b": pydotool.KEY_B,
        "c": pydotool.KEY_C,
        "d": pydotool.KEY_D,
        "e": pydotool.KEY_E,
        "f": pydotool.KEY_F,
        "g": pydotool.KEY_G,
        "h": pydotool.KEY_H,
        "i": pydotool.KEY_I,
        "j": pydotool.KEY_J,
        "k": pydotool.KEY_K,
        "l": pydotool.KEY_L,
        "m": pydotool.KEY_M,
        "n": pydotool.KEY_N,
        "o": pydotool.KEY_O,
        "p": pydotool.KEY_P,
        "q": pydotool.KEY_Q,
        "r": pydotool.KEY_R,
        "s": pydotool.KEY_S,
        "t": pydotool.KEY_T,
        "u": pydotool.KEY_U,
        "v": pydotool.KEY_V,
        "w": pydotool.KEY_W,
        "x": pydotool.KEY_X,
        "y": pydotool.KEY_Y,
        "z": pydotool.KEY_Z,
        "{": pydotool.KEY_LEFTBRACE | pydotool.FLAG_UPPERCASE,
        "|": pydotool.KEY_BACKSLASH | pydotool.FLAG_UPPERCASE,
        "}": pydotool.KEY_RIGHTBRACE | pydotool.FLAG_UPPERCASE,
        "~": pydotool.KEY_GRAVE | pydotool.FLAG_UPPERCASE,
        "add": pydotool.KEY_KPPLUS,
        "alt": pydotool.KEY_ALT,
        "altleft": pydotool.KEY_LEFTALT,
        "altright": pydotool.KEY_RIGHTALT,
        "backspace": pydotool.KEY_BACKSPACE,
        "capslock": pydotool.KEY_CAPSLOCK,
        "ctrl": pydotool.KEY_LEFTCTRL,
        "ctrlleft": pydotool.KEY_LEFTCTRL,
        "ctrlright": pydotool.KEY_RIGHTCTRL,
        "decimal": pydotool.KEY_KPDOT,
        "del": pydotool.KEY_DELETE,
        "delete": pydotool.KEY_DELETE,
        "divide": pydotool.KEY_KPSLASH,
        "down": pydotool.KEY_DOWN,
        "end": pydotool.KEY_END,
        "enter": pydotool.KEY_ENTER,
        "esc": pydotool.KEY_ESC,
        "escape": pydotool.KEY_ESC,
        "f1": pydotool.KEY_F1,
        "f2": pydotool.KEY_F2,
        "f3": pydotool.KEY_F3,
        "f4": pydotool.KEY_F4,
        "f5": pydotool.KEY_F5,
        "f6": pydotool.KEY_F6,
        "f7": pydotool.KEY_F7,
        "f8": pydotool.KEY_F8,
        "f9": pydotool.KEY_F9,
        "f10": pydotool.KEY_F10,
        "f11": pydotool.KEY_F11,
        "f12": pydotool.KEY_F12,
        "f13": pydotool.KEY_F13,
        "f14": pydotool.KEY_F14,
        "f15": pydotool.KEY_F15,
        "f16": pydotool.KEY_F16,
        "f17": pydotool.KEY_F17,
        "f18": pydotool.KEY_F18,
        "f19": pydotool.KEY_F19,
        "f20": pydotool.KEY_F20,
        "f21": pydotool.KEY_F21,
        "f22": pydotool.KEY_F22,
        "f23": pydotool.KEY_F23,
        "f24": pydotool.KEY_F24,
        "help": pydotool.KEY_HELP,
        "home": pydotool.KEY_HOME,
        "insert": pydotool.KEY_INSERT,
        "left": pydotool.KEY_LEFT,
        "multiply": pydotool.KEY_KPASTERISK,
        "num0": pydotool.KEY_KP0,
        "num1": pydotool.KEY_KP1,
        "num2": pydotool.KEY_KP2,
        "num3": pydotool.KEY_KP3,
        "num4": pydotool.KEY_KP4,
        "num5": pydotool.KEY_KP5,
        "num6": pydotool.KEY_KP6,
        "num7": pydotool.KEY_KP7,
        "num8": pydotool.KEY_KP8,
        "num9": pydotool.KEY_KP9,
        "numlock": pydotool.KEY_NUMLOCK,
        "pagedown": pydotool.KEY_PAGEDOWN,
        "pageup": pydotool.KEY_PAGEUP,
        "pause": pydotool.KEY_PAUSE,
        "pgdn": pydotool.KEY_PAGEDOWN,
        "pgup": pydotool.KEY_PAGEUP,
        "print": pydotool.KEY_PRINT,
        "printscreen": pydotool.KEY_PRINT,
        "prntscrn": pydotool.KEY_PRINT,
        "prtsc": pydotool.KEY_PRINT,
        "prtscr": pydotool.KEY_PRINT,
        "return": pydotool.KEY_ENTER,
        "right": pydotool.KEY_RIGHT,
        "scrolllock": pydotool.KEY_SCROLLLOCK,
        "shift": pydotool.KEY_LEFTSHIFT,
        "shiftleft": pydotool.KEY_LEFTSHIFT,
        "shiftright": pydotool.KEY_RIGHTSHIFT,
        "sleep": pydotool.KEY_SLEEP,
        "space": pydotool.KEY_SPACE,
        "stop": pydotool.KEY_STOP,
        "subtract": pydotool.KEY_KPMINUS,
        "tab": pydotool.KEY_TAB,
        "up": pydotool.KEY_UP,
        "volumedown": pydotool.KEY_VOLUMEDOWN,
        "volumemute": pydotool.KEY_MUTE,
        "volumeup": pydotool.KEY_VOLUMEUP,
        "win": None,
        "winleft": None,
        "winright": None,
    }
)


def _keyDown(key):
    """Performs a keyboard key press without the release. This will put that
    key in a held down state.

    Args:
      key (str): The key to be pressed down. The valid names are listed in
      pyautogui.KEY_NAMES.

    Returns:
      None
    """
    
    if key.isinstance(int):
        pydotool.key_seq([(key, pydotool.DOWN)])
        return
    
    if key not in keyboardMapping or keyboardMapping[key] is None:
        return

    pydotool.key_seq()

    needsShift = pyautogui.isShiftCharacter(key)
    if needsShift:
        pydotool.key_seq([(pydotool.KEY_LEFTSHIFT, pydotool.DOWN)])
    
    pydotool.key_seq([(keyboardMapping[key], pydotool.UP)])

    if needsShift:
        pydotool.key_seq([(pydotool.KEY_LEFTSHIFT, pydotool.UP)])

def _keyUp(key):
    """Performs a keyboard key release (without the press down beforehand).

    Args:
      key (str): The key to be released up. The valid names are listed in
      pyautogui.KEY_NAMES.

    Returns:
      None
    """
    if key not in keyboardMapping or keyboardMapping[key] is None:
        return

    if key.isinstance(int):
        keycode = key
    else:
        keycode = keyboardMapping[key]

    pydotool.key_seq([(keycode, pydotool.UP)])