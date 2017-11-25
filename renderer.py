import pyglet

import config


class Renderer:
    """Renderer handles drawing of colored squares at a given position"""

    def __init__(self, x_pos, y_pos, color):
        self.x = x_pos * config.UNIT
        self.y = y_pos * config.UNIT
        self.color = color

    def draw(self):
        """Creates a vertex list with the square's position
        and color and draws it to the screen"""
        vertex_list = pyglet.graphics.vertex_list(4, 'v2i', 'c3B')
        vertex_list.vertices = [self.x, self.y,
                                self.x + config.UNIT, self.y,
                                self.x + config.UNIT, self.y + config.UNIT,
                                self.x, self.y + config.UNIT]
        vertex_list.colors = self.color * 4
        vertex_list.draw(pyglet.gl.GL_TRIANGLE_FAN)
        # The border uses the same vertices and a darker shade of the same color
        border_color = [int(c * 0.8) for c in vertex_list.colors]
        vertex_list.colors = [border_color[0],
                              border_color[1],
                              border_color[2]] * 4
        pyglet.gl.glLineWidth(2)  # make it thicker
        vertex_list.draw(pyglet.gl.GL_LINE_LOOP)
