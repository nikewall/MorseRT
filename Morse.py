#!/usr/bin/env python3

from pynput import keyboard
import time

asciiOf = {
    ". - "     : "A",
    "- . . . " : "B",
    "- . - . " : "C",
    "- . . "   : "D",
    ". "       : "E",
    ". . - . " : "F",
    "- - . "   : "G",
    ". . . . " : "H",
    ". . "     : "I",
    ". - - - " : "J",
    "- . - "   : "K",
    ". - . . " : "L",
    "- - "     : "M",
    "- . "     : "N",
    "- - - "   : "O",
    ". - - . " : "P",
    "- - . - " : "Q",
    ". - . "   : "R",
    ". . . "   : "S",
    "- "       : "T",
    ". . - "   : "U",
    ". . . - " : "V",
    ". - - "   : "W",
    "- . . - " : "X",
    "- . - - " : "Y",
    "- - . . " : "Z"
}


def on_keydown(key):
    global pressed
    global t
    global t2
    global morseStr
    global fullStr

    if not pressed:
        if t2 is not 0:
            ti2 = time.time() - t2
            if ti2 > 0.650:
                if ti2 > 1.2:
                    try:
                        fullStr += asciiOf[morseStr]
                    except KeyError:
                        print(f"{morseStr} is invalid Morse Code...")
                        exit(-1)

                    print(f"\nTranslates to: {fullStr}")
                    fullStr = ""
                    morseStr = ""
                else:
                    fullStr += asciiOf[morseStr]
                    print(" ", end=" ")
                    morseStr = ""

        t = time.time()
        pressed = True


def on_keyup(key):
    global morseStr
    global pressed
    global t2

    ti1 = time.time() - t
    if ti1 > 0.205:
        print("-", end=" ")
        morseStr += "- "
    else:
        print(".", end=" ")
        morseStr += ". "

    pressed = False
    t2 = time.time()

    if str(key) == 'Key.esc':
        return False


with keyboard.Listener(
    on_press=on_keydown,
        on_release=on_keyup) as listener:
    pressed = False
    t2 = 0
    morseStr = ""
    fullStr = ""
    listener.join()


