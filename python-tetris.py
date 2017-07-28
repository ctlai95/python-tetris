import pyglet

UNIT = 40
LEFT_BORDER = 0
RIGHT_BORDER = 10
UPPER_BORDER = 22
LOWER_BORDER = 0
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

    def move(self, key):
        if key == pyglet.window.key.MOTION_LEFT:
            moveable = True
            for c in self.coords:
                if c[0] <= LEFT_BORDER*UNIT:
                    moveable = False
            if moveable is True:
                tmp = self.coords
                self.coords = []
                for c in tmp:
                    self.coords.append(tuple((c[0]-UNIT, c[1])))
        if key == pyglet.window.key.MOTION_RIGHT:
            moveable = True
            for c in self.coords:
                if c[0]+UNIT >= RIGHT_BORDER*UNIT:
                    moveable = False
            if moveable is True:
                tmp = self.coords
                self.coords = []
                for c in tmp:
                    self.coords.append(tuple((c[0]+UNIT, c[1])))
        if key == pyglet.window.key.MOTION_UP:
            moveable = True
            for c in self.coords:
                if c[1]+UNIT >= UPPER_BORDER*UNIT:
                    moveable = False
            if moveable is True:
                tmp = self.coords
                self.coords = []
                for c in tmp:
                    self.coords.append(tuple((c[0], c[1]+UNIT)))
        if key == pyglet.window.key.MOTION_DOWN:
            moveable = True
            for c in self.coords:
                if c[1] <= LOWER_BORDER*UNIT:
                    moveable = False
            if moveable is True:
                tmp = self.coords
                self.coords = []
                for c in tmp:
                    self.coords.append(tuple((c[0], c[1]-UNIT)))
        if key == pyglet.window.key.SPACE:
            height = UPPER_BORDER*UNIT
            for c in self.coords:
                if c[1] < height:
                    height = c[1]
            tmp = self.coords
            self.coords = []
            for c in tmp:
                self.coords.append(tuple((c[0], c[1]-height)))


@window.event
def on_text_motion(motion):
    if motion == pyglet.window.key.MOTION_LEFT or \
       motion == pyglet.window.key.MOTION_RIGHT or \
       motion == pyglet.window.key.MOTION_DOWN:
        current_piece.move(motion)


@window.event
def on_key_press(symbol, modifier):
    if symbol == pyglet.window.key.SPACE:
        current_piece.move(symbol)


current_piece = piece(O_PIECE)


@window.event
def on_draw():
    window.clear()

    for i in range(current_piece.size):
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                     [0, 1, 2, 0, 2, 3],
                                     ('v2i', current_piece.opengl_coords()[i]))


pyglet.app.run()
