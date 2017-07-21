import pyglet

unit = 40

window = pyglet.window.Window(10*unit, 22*unit)
# window.push_handlers(pyglet.window.event.WindowEventLogger())

global current_piece


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class square:
    def __init__(self, origin, side_length):
        self.origin = origin
        self.side_length = side_length

    def position(self):
        return (self.origin.x, self.origin.y,
                self.origin.x+self.side_length, self.origin.y,
                self.origin.x+self.side_length, self.origin.y+self.side_length,
                self.origin.x, self.origin.y+self.side_length)

    def move_right(self):
        self.origin.x += self.side_length

    def move_left(self):
        self.origin.x -= self.side_length

    def move_up(self):
        self.origin.y += self.side_length

    def move_down(self):
        self.origin.y -= self.side_length


class tetromino:
    def __init__(self, type, origin):
        self.pieces = []
        if type == "I":
            for i in range(0, 4):
                self.pieces.append(
                    square(
                        point(origin.x + (i * unit), origin.y),
                        unit))

        if type == "O":
            for i in range(0, 2):
                for y in range(0, 2):
                    self.pieces.append(
                        square(
                            point(origin.x + (y * unit),
                                  origin.y + (i * unit)),
                            unit))

        if type == "T":
            for i in range(0, 3):
                self.pieces.append(
                    square(
                        point(origin.x + (i * unit), origin.y),
                        unit))
            self.pieces.append(
                square(
                    point(origin.x + unit, origin.y + unit),
                    unit))

        if type == "S":
            for i in range(0, 2):
                self.pieces.append(
                    square(
                        point(origin.x + (i * unit), origin.y),
                        unit))

            for i in range(1, 3):
                self.pieces.append(
                    square(
                        point(origin.x + (i * unit), origin.y + unit),
                        unit))

        if type == "Z":
            for i in range(1, 3):
                self.pieces.append(
                    square(
                        point(origin.x + (i * unit), origin.y),
                        unit))

            for i in range(0, 2):
                self.pieces.append(
                    square(
                        point(origin.x + (i * unit), origin.y + unit),
                        unit))

        if type == "J":
            for i in range(0, 3):
                self.pieces.append(
                    square(
                        point(origin.x + (i * unit), origin.y),
                        unit))

            self.pieces.append(
                square(
                    point(origin.x, origin.y + unit),
                    unit))

        if type == "L":
            for i in range(0, 3):
                self.pieces.append(
                    square(
                        point(origin.x + (i * unit), origin.y),
                        unit)
                )
            self.pieces.append(
                square(
                    point(origin.x + (2 * unit), origin.y + unit),
                    unit)
            )

    def move_right(self):
        for p in self.pieces:
            p.move_right()

    def move_left(self):
        for p in self.pieces:
            p.move_left()

    def move_up(self):
        for p in self.pieces:
            p.move_up()

    def move_down(self):
        for p in self.pieces:
            p.move_down()


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


current_piece = tetromino("L", point(3*unit, 20*unit))


@window.event
def on_draw():
    window.clear()

    for c in current_piece.pieces:
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                     [0, 1, 2, 0, 2, 3],
                                     ('v2i', c.position()))


pyglet.app.run()
