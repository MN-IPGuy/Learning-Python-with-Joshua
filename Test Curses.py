__author__ = 'Dan'
import pygcurse

win = pygcurse.PygcurseWindow(40, 25, 'Hello World Program')
win.pygprint('Hello world!')
pygcurse.waitforkeypress()