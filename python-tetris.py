import pyglet

window = pyglet.window.Window(500, 1000)
# window.push_handlers(pyglet.window.event.WindowEventLogger())

multiplier = 50
global t


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


class tetromino:
    def __init__(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def move_right(self):
        if self.right.origin()[0] < 450:
            self.left.move_right()
            self.right.move_right()
            self.top.move_right()
            self.bottom.move_right()

    def move_left(self):
        if self.left.origin()[0] > 0:
            self.left.move_left()
            self.right.move_left()
            self.top.move_left()
            self.bottom.move_left()

    def move_up(self):
        if self.top.origin()[1] < 950:
            self.left.move_up()
            self.right.move_up()
            self.top.move_up()
            self.bottom.move_up()

    def move_down(self):
        if self.bottom.origin()[1] > 0:
            self.left.move_down()
            self.right.move_down()
            self.top.move_down()
            self.bottom.move_down()


@window.event
def on_text_motion(motion):

    if(motion == pyglet.window.key.MOTION_LEFT):
        t.move_left()
    if(motion == pyglet.window.key.MOTION_RIGHT):
        t.move_right()
    if(motion == pyglet.window.key.MOTION_UP):
        t.move_up()
    if(motion == pyglet.window.key.MOTION_DOWN):
        t.move_down()


t = tetromino(
    square(0, 0, 50),
    square(100, 0, 50),
    square(50, 50, 50),
    square(50, 0, 50)
    )


@window.event
def on_draw():
    window.clear()

    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2, 0, 2, 3],
                                 ('v2i', t.left.position()))

    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2, 0, 2, 3],
                                 ('v2i', t.right.position()))

    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2, 0, 2, 3],
                                 ('v2i', t.top.position()))

    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2, 0, 2, 3],
                                 ('v2i', t.bottom.position()))


pyglet.app.run()
