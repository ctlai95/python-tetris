import pyglet

UNIT = 40

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


current_piece = piece([(0, 0),
                       (1, 0),
                       (2, 0),
                       (3, 0)])


@window.event
def on_draw():
    window.clear()

    for i in range(0, current_piece.size):
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                     [0, 1, 2, 0, 2, 3],
                                     ('v2i', current_piece.opengl_coords()[i]))


pyglet.app.run()
