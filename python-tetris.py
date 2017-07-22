import pyglet

UNIT = 40
O_PIECE = [(4, 20), (5, 20), (4, 21), (5, 21)]
I_PIECE = [(3, 20), (4, 20), (5, 20), (6, 20)]
J_PIECE = [(3, 21), (3, 20), (4, 20), (5, 20)]
L_PIECE = [(3, 20), (4, 20), (5, 20), (5, 21)]
S_PIECE = [(3, 20), (4, 20), (4, 21), (5, 21)]
Z_PIECE = [(3, 21), (4, 21), (4, 20), (5, 20)]
T_PIECE = [(3, 20), (4, 20), (5, 20), (4, 21)]

window = pyglet.window.Window(10*UNIT, 22*UNIT)
# window.push_handlers(pyglet.window.event.WindowEventLogger())

global current_piece


class piece:
    def __init__(self, coords):
        self.coords = []
        for c in coords:
            self.coords.append(tuple(x * UNIT for x in c))
        self.size = len(coords)

    def opengl_coords(self):
        t = []
        for c in self.coords:
            t.append(
                (c[0], c[1],
                 c[0]+UNIT, c[1],
                 c[0]+UNIT, c[1]+UNIT,
                 c[0], c[1]+UNIT)
            )
        return t

    def move_left(self):
        tmp = self.coords
        self.coords = []
        for c in tmp:
            self.coords.append(tuple((c[0]-UNIT, c[1])))

    def move_right(self):
        tmp = self.coords
        self.coords = []
        for c in tmp:
            self.coords.append(tuple((c[0]+UNIT, c[1])))

    def move_up(self):
        tmp = self.coords
        self.coords = []
        for c in tmp:
            self.coords.append(tuple((c[0], c[1]+UNIT)))

    def move_down(self):
        tmp = self.coords
        self.coords = []
        for c in tmp:
            self.coords.append(tuple((c[0], c[1]-UNIT)))


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


current_piece = piece(T_PIECE)


@window.event
def on_draw():
    window.clear()

    for i in range(0, current_piece.size):
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                     [0, 1, 2, 0, 2, 3],
                                     ('v2i', current_piece.opengl_coords()[i]))


pyglet.app.run()
