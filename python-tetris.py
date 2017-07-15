import pyglet
from pyglet.window import key

window = pyglet.window.Window(600, 400)
# window.push_handlers(pyglet.window.event.WindowEventLogger())

multiplier = 50
xpos = 0
ypos = 0


def move_right():
    global xpos
    if xpos >= 450:
        return
    xpos += 1*multiplier


def move_left():
    global xpos
    if xpos <= -100:
        return
    xpos -= 1*multiplier


def move_up():
    global ypos
    if ypos >= 250:
        return
    ypos += 1*multiplier


def move_down():
    global ypos
    if ypos <= -100:
        return
    ypos -= 1*multiplier


@window.event
def on_text_motion(motion):
    global xpos, ypos, pressed_keys

    if(motion == pyglet.window.key.MOTION_LEFT):
        move_left()
    if(motion == pyglet.window.key.MOTION_RIGHT):
        move_right()
    if(motion == pyglet.window.key.MOTION_UP):
        move_up()
    if(motion == pyglet.window.key.MOTION_DOWN):
        move_down()


@window.event
def on_draw():
    window.clear()
    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2, 0, 2, 3],
                                 ('v2i', (100+xpos, 100+ypos,
                                          150+xpos, 100+ypos,
                                          150+xpos, 150+ypos,
                                          100+xpos, 150+ypos))
                                 )


pyglet.app.run()
