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
    def __init__(self, one, two, three, four):
        self.one = one
        self.two = two
        self.three = three
        self.four = four

    def move_right(self):
        self.one.move_right()
        self.two.move_right()
        self.three.move_right()
        self.four.move_right()

    def move_left(self):
        self.one.move_left()
        self.two.move_left()
        self.three.move_left()
        self.four.move_left()

    def move_up(self):
        self.one.move_up()
        self.two.move_up()
        self.three.move_up()
        self.four.move_up()

    def move_down(self):
        self.one.move_down()
        self.two.move_down()
        self.three.move_down()
        self.four.move_down()


@window.event
def on_text_motion(motion):
    global t
    if(motion == pyglet.window.key.MOTION_LEFT):
        t.move_left()
    if(motion == pyglet.window.key.MOTION_RIGHT):
        t.move_right()
    if(motion == pyglet.window.key.MOTION_UP):
        t.move_up()
    if(motion == pyglet.window.key.MOTION_DOWN):
        t.move_down()


global t
t = tetromino(
    square(0, 0, 50),
    square(50, 0, 50),
    square(100, 0, 50),
    square(50, 50, 50)
    )


@window.event
def on_draw():
    window.clear()

    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2, 0, 2, 3],
                                 ('v2i', t.one.position()))

    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2, 0, 2, 3],
                                 ('v2i', t.two.position()))

    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2, 0, 2, 3],
                                 ('v2i', t.three.position()))

    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2, 0, 2, 3],
                                 ('v2i', t.four.position()))


pyglet.app.run()
