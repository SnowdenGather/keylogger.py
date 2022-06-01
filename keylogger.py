import datetime
import time
import os


from pynput.keyboard import Key, Listener

def on_press(key):
    print("{0} Pressionado".format(key))

def write_file(keys):
        for key in keys:
            f.write(keys)


def on_realease(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_realease=on_realease) as Listener:
    Listener.join()
