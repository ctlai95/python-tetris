#!/usr/bin/env python3
import pyglet

from src.window.window import Window

if __name__ == '__main__':
    window = Window(400, 880, "Python Tetris")

    while True:
        pyglet.clock.tick()
        window.keyboard.start_listeners()

        for win in pyglet.app.windows:
            win.switch_to()
            win.dispatch_events()
            win.dispatch_event('on_draw')
            win.flip()
