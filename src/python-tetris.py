#!/usr/bin/env python3
import logging

import pyglet

from src.window.window import Window

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s")
log = logging.getLogger(__name__)

if __name__ == '__main__':
    log.info("Starting python-tetris")
    window = Window(400, 880, "Python Tetris")
    pyglet.clock.schedule_interval(window.update, 1 / 60.0)
    log.info("Entering main loop")
    pyglet.app.run()
    log.info("Exiting main loop")
