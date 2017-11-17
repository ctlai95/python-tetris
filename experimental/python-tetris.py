import pyglet

import config
import coordinate
import square
import tetromino
import map


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.map = map.Map(int(self.width / config.UNIT),
                           int(self.height / config.UNIT))

    def on_draw(self):
        self.clear()
        self.map.render_map()
        self.map.print_matrix()

    def on_key_press(self, symbol, modifier):
        if symbol == pyglet.window.key.LEFT:
            self.map.current_tetromino.move_left()
        elif symbol == pyglet.window.key.RIGHT:
            self.map.current_tetromino.move_right()
        elif symbol == pyglet.window.key.DOWN:
            self.map.current_tetromino.move_down()
        elif symbol == pyglet.window.key.ESCAPE:
            pyglet.app.exit()


if __name__ == '__main__':
    window = Window(400, 880, "Python Tetris")
    pyglet.app.run()
