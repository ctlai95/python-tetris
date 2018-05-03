"""The main game file."""
#!/usr/bin/env python3
import logging

import pyglet

from src.config import LOG_LEVEL
from src.window.window import Window

logging.basicConfig(level=LOG_LEVEL,
                    format="%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s")
log = logging.getLogger(__name__)

if __name__ == '__main__':
    log.info("Starting python-tetris")
    log.info("Log level: {}".format(LOG_LEVEL))
    window = Window(400, 880, "Python Tetris")
    log.info("Entering main loop")
    pyglet.app.run()
    log.info("Exiting main loop")
