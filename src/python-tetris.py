#!/usr/bin/env python3
import pyglet

from src.window.window import Window

if __name__ == '__main__':
    window = Window(400, 880, "Python Tetris")
    pyglet.clock.schedule_interval(window.update, 1 / 120.0)
    pyglet.app.run()
