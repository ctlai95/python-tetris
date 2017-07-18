import pyglet

window = pyglet.window.Window(500, 1000)
# window.push_handlers(pyglet.window.event.WindowEventLogger())

multiplier = 50
global current_piece


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
    def __init__(self, type):
        if type == "I":
            self.one = square(150, 900, 50)
            self.two = square(200, 900, 50)
            self.three = square(250, 900, 50)
            self.four = square(300, 900, 50)

        if type == "O":
            self.one = square(200, 900, 50)
            self.two = square(250, 900, 50)
            self.three = square(200, 950, 50)
            self.four = square(250, 950, 50)

        if type == "T":
            self.one = square(150, 900, 50)
            self.two = square(200, 900, 50)
            self.three = square(250, 900, 50)
            self.four = square(200, 950, 50)

        if type == "S":
            self.one = square(150, 900, 50)
            self.two = square(200, 900, 50)
            self.three = square(200, 950, 50)
            self.four = square(250, 950, 50)

        if type == "Z":
            self.one = square(200, 900, 50)
            self.two = square(250, 900, 50)
            self.three = square(150, 950, 50)
            self.four = square(200, 950, 50)

        if type == "J":
            self.one = square(150, 900, 50)
            self.two = square(200, 900, 50)
            self.three = square(250, 900, 50)
            self.four = square(150, 950, 50)

        if type == "L":
            self.one = square(150, 900, 50)
            self.two = square(200, 900, 50)
            self.three = square(250, 900, 50)
            self.four = square(250, 950, 50)


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
        current_piece.move_left()
    if(motion == pyglet.window.key.MOTION_RIGHT):
        current_piece.move_right()
    if(motion == pyglet.window.key.MOTION_UP):
        current_piece.move_up()
    if(motion == pyglet.window.key.MOTION_DOWN):
        current_piece.move_down()



current_piece = tetromino("L")


@window.event
def on_draw():
    window.clear()

    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2, 0, 2, 3],
                                 ('v2i', current_piece.one.position()))

    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2, 0, 2, 3],
                                 ('v2i', current_piece.two.position()))

    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2, 0, 2, 3],
                                 ('v2i', current_piece.three.position()))

    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2, 0, 2, 3],
                                 ('v2i', current_piece.four.position()))


pyglet.app.run()
