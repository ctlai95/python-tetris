import pyglet
import config
import piece

window = pyglet.window.Window(10*config.UNIT, 22*config.UNIT)
# window.push_handlers(pyglet.window.event.WindowEventLogger())

global current_piece


@window.event
def on_text_motion(motion):
    if motion == pyglet.window.key.MOTION_LEFT or \
       motion == pyglet.window.key.MOTION_RIGHT or \
       motion == pyglet.window.key.MOTION_DOWN:
        current_piece.move(motion)


@window.event
def on_key_press(symbol, modifier):
    if symbol == pyglet.window.key.SPACE or \
       symbol == pyglet.window.key.MOTION_UP:
        current_piece.move(symbol)


current_piece = piece.piece(config.O_PIECE)


@window.event
def on_draw():
    window.clear()

    for i in range(current_piece.size):
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                     [0, 1, 2, 0, 2, 3],
                                     ('v2i', current_piece.opengl_coords()[i]))


pyglet.app.run()
