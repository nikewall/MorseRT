#!/usr/bin/env python3

from pynput import keyboard
import time


def on_keydown(key):
    global pressed
    global t
    global t2

    if not pressed:
        if t2 is not 0:
            ti2 = time.time() - t2
            if ti2 > 0.650:
                print(" ", end=" ")

            # ti2 = str(time.time() - t2)[0:5]
            # print(f"There was a break for {ti2} seconds")

        t = time.time()
        pressed = True


def on_keyup(key):
    ti1 = time.time() - t
    if ti1 > 0.205:
        print("-", end=" ")
    else:
        print(".", end=" ")

    # ti1 = str(time.time() - t)[0:5]  # time actual
    # print(f"The key {key} was pressed for {ti1} seconds")

    global pressed
    pressed = False

    global t2
    t2 = time.time()

    if str(key) == 'Key.esc':
        return False  # stop listening


with keyboard.Listener(
    on_press=on_keydown,
        on_release=on_keyup) as listener:
    pressed = False
    t2 = 0
    listener.join()


# TODO:
#   Features:
#       -> Quantify (one per unrestricted size) that "spaces" or breaks occur
#            ===> Should be "risky", since feeling latency is not ideal...
#       -> Choose a DS/A (maybe map?) to 'convert' morse to ascii AFAP
