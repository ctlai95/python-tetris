import pyglet
from pyglet.window import key

window = pyglet.window.Window(600, 400)
# window.push_handlers(pyglet.window.event.WindowEventLogger())

multiplier = 50

global sq


class square:
    def __init__(self, x_orig, y_orig, side_length):
        self.x_orig = x_orig
        self.y_orig = y_orig
        self.side_length = side_length

    def origin(self):
        return self.x_orig, self.y_orig

    def position(self):
        return (self.x_orig, self.y_orig,
                self.x_orig+50, self.y_orig,
                self.x_orig+50, self.y_orig+50,
                self.x_orig, self.y_orig+50)

    def move_right(self):
        self.x_orig += 1*multiplier

    def move_left(self):
        self.x_orig -= 1*multiplier

    def move_up(self):
        self.y_orig += 1*multiplier

    def move_down(self):
        self.y_orig -= 1*multiplier


@window.event
def on_text_motion(motion):
    global sq
    if(motion == pyglet.window.key.MOTION_LEFT):
        sq.move_left()
    if(motion == pyglet.window.key.MOTION_RIGHT):
        sq.move_right()
    if(motion == pyglet.window.key.MOTION_UP):
        sq.move_up()
    if(motion == pyglet.window.key.MOTION_DOWN):
        sq.move_down()


global sq
sq = square(0, 0, 50)


@window.event
def on_draw():
    window.clear()
    # pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
    #                              [0, 1, 2, 0, 2, 3],
    #                              ('v2i', (100+xpos, 100+ypos,
    #                                       150+xpos, 100+ypos,
    #                                       150+xpos, 150+ypos,
    #                                       100+xpos, 150+ypos))
    #                              )

    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2, 0, 2, 3],
                                 ('v2i', sq.position()))


pyglet.app.run()
