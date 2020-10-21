#/usr/bin/env python
#mouseLoggerBasic

from pynput.mouse import Listener
import logging

logging.basicConfig(filename = "mouse_log.txt", level=logging.DEBUG,
                    format='%(asctime)s: %(message)s')

def on_move(x,y):
    #print("Mouse Mover")
    logging.info("Mouse move to ({0},{1})".format(x,y))

def on_click(x, y, button, pressed):
    #print("Mouse Clicked")
    if pressed:
        logging.info('Mouse clicked ar ({0},{1}) with {2}'.format(x,y,button))

def on_scroll(x, y, dx, dy):
    #print("Mouse Scrolled")
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

with Listener(on_move = on_move, on_click=on_click, on_scroll= on_scroll) as listener:
    listener.join()