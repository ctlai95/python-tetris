from src.board.board import Board
from src.colors import colors
from src.movement.movement import Movement
from src.point.point import Point
from src.square.square import Square
from src.tetromino.constants import LAYOUTS, SPAWN
from src.tetromino.state import State
from src.tetromino.tetromino import Tetromino

movement = Movement(Board(10, 22))
tetrominos_id_list = ['O', 'I', 'J', 'L', 'S', 'Z', 'T']
barrier_tetromino = Tetromino("O", Point(4, 9), colors.ASH)


def get_tetromino_width(tetromino_id):
    leftmost = movement.board.width
    rightmost = 0
    for layout in LAYOUTS[tetromino_id]:
        if layout[0] < leftmost:
            leftmost = layout[0]
        if layout[0] > rightmost:
            rightmost = layout[0]
    return rightmost - leftmost


def get_tetromino_height(tetromino_id):
    lowest = movement.board.height
    highest = 0
    for layout in LAYOUTS[tetromino_id]:
        if layout[1] < lowest:
            lowest = layout[1]
        if layout[1] > highest:
            highest = layout[1]
    return highest - lowest


def set_up_barrier_tetromino():
    movement.board.board_tetrominos.append(barrier_tetromino)
    movement.board.update_matrices()


def clean_up_barrier_tetromino():
    movement.board.board_tetrominos = []
    movement.board.update_matrices()


def test_init():
    assert isinstance(movement, Movement)
    assert movement.board is not None


def test_move_left_wall_barrier():
    for tetromino_id in tetrominos_id_list:
        movement.board.current_tetromino = Tetromino(tetromino_id, Point(
            SPAWN[tetromino_id][0], SPAWN[tetromino_id][1]), colors.ASH)
        position_before_move = movement.board.current_tetromino.origin
        for i in range(SPAWN[tetromino_id][0]):
            movement.move_left()
            assert (movement.board.current_tetromino.origin.x,
                    movement.board.current_tetromino.origin.y) == (position_before_move.x - (i + 1), position_before_move.y)
        assert (movement.board.current_tetromino.origin.x,
                movement.board.current_tetromino.origin.y) == (0, position_before_move.y)
        movement.move_left()
        assert (movement.board.current_tetromino.origin.x,
                movement.board.current_tetromino.origin.y) == (0, position_before_move.y)


def test_move_right_wall_barrier():
    for tetromino_id in tetrominos_id_list:
        movement.board.current_tetromino = Tetromino(tetromino_id, Point(
            SPAWN[tetromino_id][0], SPAWN[tetromino_id][1]), colors.ASH)
        position_before_move = movement.board.current_tetromino.origin
        tetromino_width = get_tetromino_width(tetromino_id)
        for i in range((movement.board.width - 1) - SPAWN[movement.board.current_tetromino.id][0] - tetromino_width):
            movement.move_right()
            assert (movement.board.current_tetromino.origin.x,
                    movement.board.current_tetromino.origin.y) == (position_before_move.x + (i + 1), position_before_move.y)
        assert (movement.board.current_tetromino.origin.x,
                movement.board.current_tetromino.origin.y) == ((movement.board.width - 1) - tetromino_width, position_before_move.y)
        movement.move_right()
        assert (movement.board.current_tetromino.origin.x,
                movement.board.current_tetromino.origin.y) == ((movement.board.width - 1) - tetromino_width, position_before_move.y)


def test_move_down_wall_barrier():
    for tetromino_id in tetrominos_id_list:
        movement.board.current_tetromino = Tetromino(tetromino_id, Point(
            SPAWN[tetromino_id][0], SPAWN[tetromino_id][1]), colors.ASH)
        position_before_move = movement.board.current_tetromino.origin
        for i in range(SPAWN[tetromino_id][1]):
            movement.move_down()
            assert (movement.board.current_tetromino.origin.x,
                    movement.board.current_tetromino.origin.y) == (position_before_move.x, position_before_move.y - (i + 1))
        assert (movement.board.current_tetromino.origin.x,
                movement.board.current_tetromino.origin.y) == (position_before_move.x, 0)
        movement.move_down()
        assert (movement.board.current_tetromino.origin.x,
                movement.board.current_tetromino.origin.y) == (position_before_move.x, 0)


def test_move_up_wall_barrier():
    for tetromino_id in tetrominos_id_list:
        movement.board.current_tetromino = Tetromino(tetromino_id, Point(
            SPAWN[tetromino_id][0], SPAWN[tetromino_id][1]), colors.ASH)
        position_before_move = movement.board.current_tetromino.origin
        tetromino_height = get_tetromino_height(tetromino_id)
        for i in range((movement.board.height - 1) - SPAWN[tetromino_id][1] - tetromino_height):
            movement.move_up()
            assert (movement.board.current_tetromino.origin.x,
                    movement.board.current_tetromino.origin.y) == (position_before_move.x, position_before_move.y + (i + 1))
        assert (movement.board.current_tetromino.origin.x,
                movement.board.current_tetromino.origin.y) == (position_before_move.x, (movement.board.height - 1) - tetromino_height)
        movement.move_up()
        assert (movement.board.current_tetromino.origin.x,
                movement.board.current_tetromino.origin.y) == (position_before_move.x, (movement.board.height - 1) - tetromino_height)


def test_move_left_tetromino_barrier():
    set_up_barrier_tetromino()
    for tetromino_id in tetrominos_id_list:
        movement.board.current_tetromino = Tetromino(
            tetromino_id, Point(barrier_tetromino.origin.x + get_tetromino_width(barrier_tetromino.id), barrier_tetromino.origin.y), colors.ASH)
        origin = movement.board.current_tetromino.origin
        movement.move_left()
        assert (movement.board.current_tetromino.origin.x,
                movement.board.current_tetromino.origin.y) == (origin.x, origin.y)
    clean_up_barrier_tetromino()


def test_move_right_tetromino_barrier():
    set_up_barrier_tetromino()
    for tetromino_id in tetrominos_id_list:
        tetromino_width = get_tetromino_width(tetromino_id)
        movement.board.current_tetromino = Tetromino(
            tetromino_id, Point(barrier_tetromino.origin.x - get_tetromino_width(tetromino_id), barrier_tetromino.origin.y), colors.ASH)
        position_before_move = movement.board.current_tetromino.origin
        movement.move_right()
        assert (movement.board.current_tetromino.origin.x,
                movement.board.current_tetromino.origin.y) == (position_before_move.x, position_before_move.y)
    clean_up_barrier_tetromino()


def test_move_down_tetromino_barrier():
    set_up_barrier_tetromino()
    for tetromino_id in tetrominos_id_list:
        movement.board.current_tetromino = Tetromino(
            tetromino_id, Point(barrier_tetromino.origin.x, barrier_tetromino.origin.y + get_tetromino_height(barrier_tetromino.id)), colors.ASH)
        position_before_move = movement.board.current_tetromino.origin
        movement.move_down()
        assert (movement.board.current_tetromino.origin.x,
                movement.board.current_tetromino.origin.y) == (position_before_move.x, position_before_move.y)
    clean_up_barrier_tetromino()


def test_move_up_tetromino_barrier():
    set_up_barrier_tetromino()
    for tetromino_id in tetrominos_id_list:
        movement.board.current_tetromino = Tetromino(
            tetromino_id, Point(barrier_tetromino.origin.x, barrier_tetromino.origin.y - get_tetromino_height(tetromino_id)), colors.ASH)
        position_before_move = movement.board.current_tetromino.origin
        movement.move_up()
        assert (movement.board.current_tetromino.origin.x,
                movement.board.current_tetromino.origin.y) == (position_before_move.x, position_before_move.y)
    clean_up_barrier_tetromino()


def test_wall_kick_test_pass_no_offset():
    for tetromino_id in tetrominos_id_list:
        for i in range(movement.board.width - get_tetromino_width(tetromino_id)):
            for j in range(movement.board.height - get_tetromino_height(tetromino_id)):
                movement.board.current_tetromino = Tetromino(
                    tetromino_id, Point(i, j), colors.ASH)
                assert movement.wall_kick_test_pass(0, 0)


def test_wall_kick_test_pass_offset_wall_barrier():
    for tetromino_id in tetrominos_id_list:
        movement.board.current_tetromino = Tetromino(
            tetromino_id, Point(0, 0), colors.ASH)
        assert not movement.wall_kick_test_pass(-1, 0)
        assert not movement.wall_kick_test_pass(0, -1)
        movement.board.current_tetromino = Tetromino(
            tetromino_id, Point(movement.board.width - get_tetromino_height(tetromino_id), 0), colors.ASH)
        assert not movement.wall_kick_test_pass(1, 0)
        movement.board.current_tetromino = Tetromino(
            tetromino_id, Point(0, movement.board.height - get_tetromino_height(tetromino_id)), colors.ASH)
        assert not movement.wall_kick_test_pass(0, 1)


def test_wall_kick_test_pass_offset_tetromino_barrier():
    set_up_barrier_tetromino()
    for tetromino_id in tetrominos_id_list:
        movement.board.current_tetromino = Tetromino(tetromino_id, Point(
            barrier_tetromino.origin.x + get_tetromino_width(barrier_tetromino.id), barrier_tetromino.origin.y), colors.ASH)
        assert not movement.wall_kick_test_pass(-1, 0)
        movement.board.current_tetromino = Tetromino(tetromino_id, Point(
            barrier_tetromino.origin.x - get_tetromino_width(tetromino_id), barrier_tetromino.origin.y), colors.ASH)
        assert not movement.wall_kick_test_pass(1, 0)
        movement.board.current_tetromino = Tetromino(tetromino_id, Point(
            barrier_tetromino.origin.x, barrier_tetromino.origin.y + get_tetromino_height(barrier_tetromino.id)), colors.ASH)
        assert not movement.wall_kick_test_pass(0, -1)
        movement.board.current_tetromino = Tetromino(tetromino_id, Point(
            barrier_tetromino.origin.x, barrier_tetromino.origin.y - get_tetromino_height(barrier_tetromino.id)), colors.ASH)
        assert not movement.wall_kick_test_pass(0, 1)
    clean_up_barrier_tetromino()


# http://tetris.wikia.com/wiki/List_of_twists
class Twist_Test:
    def __init__(self, tetromino_id, initial_position, initial_rotation, initial_offset, initial_state, square_positions, rotation, final_position, final_state):
        self.tetromino_id = tetromino_id
        self.initial_position = initial_position
        self.initial_rotation = initial_rotation
        self.initial_offset = initial_offset
        self.initial_state = initial_state
        self.square_positions = square_positions
        self.rotation = rotation
        self.final_position = final_position
        self.final_state = final_state


twist_test_list = [
    Twist_Test(
        tetromino_id="T",
        initial_position=Point(4, 1),
        initial_rotation=movement.rotate_ccw,
        initial_offset=None,
        initial_state=State.THREE,
        square_positions=[
            Point(3, 0),
            Point(3, 1),
            Point(4, 0),
            Point(6, 0),
            Point(6, 2)
        ],
        rotation=movement.rotate_ccw,
        final_position=Point(4, 1),
        final_state=State.TWO
    ),
    Twist_Test(
        tetromino_id="T",
        initial_position=Point(3, 2),
        initial_rotation=movement.rotate_cw,
        initial_offset=None,
        initial_state=State.ONE,
        square_positions=[
            Point(3, 0),
            Point(3, 1),
            Point(3, 2),
            Point(4, 0),
            Point(6, 0),
            Point(6, 2),
            Point(7, 0),
            Point(7, 1),
            Point(7, 2)
        ],
        rotation=movement.rotate_cw,
        final_position=Point(4, 1),
        final_state=State.TWO
    ),
    Twist_Test(
        tetromino_id="T",
        initial_position=Point(6, 1),
        initial_rotation=None,
        initial_offset=None,
        initial_state=State.ZERO,
        square_positions=[
            Point(5, 0),
            Point(5, 1),
            Point(5, 2),
            Point(7, 0),
            Point(8, 0)
        ],
        rotation=movement.rotate_cw,
        final_position=Point(5, 1),
        final_state=State.ONE
    ),
    Twist_Test(
        tetromino_id="T",
        initial_position=Point(0, 1),
        initial_rotation=None,
        initial_offset=None,
        initial_state=State.ZERO,
        square_positions=[
            Point(1, 0),
            Point(2, 0),
            Point(3, 0),
            Point(3, 1)
        ],
        rotation=movement.rotate_cw,
        final_position=Point(-1, 1),
        final_state=State.ONE
    ),
    Twist_Test(
        tetromino_id="T",
        initial_position=Point(2, 3),
        initial_rotation=None,
        initial_offset=None,
        initial_state=State.ZERO,
        square_positions=[
            Point(2, 0),
            Point(2, 1),
            Point(2, 2),
            Point(3, 0),
            Point(3, 2),
            Point(4, 4),
            Point(5, 0),
            Point(5, 1),
            Point(5, 2),
            Point(5, 3),
            Point(5, 4)
        ],
        rotation=movement.rotate_ccw,
        final_position=Point(3, 1),
        final_state=State.THREE
    ),
    Twist_Test(
        tetromino_id="T",
        initial_position=Point(4, 1),
        initial_rotation=None,
        initial_offset=None,
        initial_state=State.ZERO,
        square_positions=[
            Point(3, 0),
            Point(3, 1),
            Point(3, 2),
            Point(3, 3),
            Point(4, 3),
            Point(5, 0),
            Point(6, 0)
        ],
        rotation=movement.rotate_cw,
        final_position=Point(3, 1),
        final_state=State.ONE
    ),
    Twist_Test(
        tetromino_id="I",
        initial_position=Point(3, 4),
        initial_rotation=None,
        initial_offset=None,
        initial_state=State.ZERO,
        square_positions=[
            Point(2, 0),
            Point(2, 1),
            Point(2, 2),
            Point(2, 3),
            Point(3, 0),
            Point(3, 1),
            Point(3, 3),
            Point(5, 0),
            Point(5, 1),
            Point(5, 3),
            Point(6, 0),
            Point(6, 1),
            Point(6, 3),
            Point(7, 0),
            Point(7, 1),
            Point(7, 2),
            Point(7, 3)
        ],
        rotation=movement.rotate_ccw,
        final_position=Point(3, 4),
        final_state=State.THREE
    ),
    Twist_Test(
        tetromino_id="I",
        initial_position=Point(3, 2),
        initial_rotation=movement.rotate_ccw,
        initial_offset=None,
        initial_state=State.THREE,
        square_positions=[
            Point(2, 0),
            Point(2, 1),
            Point(2, 2),
            Point(2, 3),
            Point(3, 0),
            Point(3, 1),
            Point(3, 3),
            Point(5, 0),
            Point(5, 1),
            Point(5, 3),
            Point(6, 0),
            Point(6, 1),
            Point(6, 3),
            Point(7, 0),
            Point(7, 1),
            Point(7, 2),
            Point(7, 3)
        ],
        rotation=movement.rotate_cw,
        final_position=Point(3, 2),
        final_state=State.ZERO
    ),
    Twist_Test(
        tetromino_id="I",
        initial_position=Point(2, 3),
        initial_rotation=None,
        initial_offset=None,
        initial_state=State.ZERO,
        square_positions=[
            Point(1, 0),
            Point(1, 1),
            Point(1, 2),
            Point(1, 3),
            Point(1, 4),
            Point(2, 4),
            Point(3, 0),
            Point(3, 1),
            Point(3, 2),
            Point(4, 0),
            Point(4, 1),
            Point(4, 2),
            Point(5, 0),
            Point(5, 1),
            Point(5, 2),
        ],
        rotation=movement.rotate_cw,
        final_position=Point(0, 2),
        final_state=State.ONE,
    ),
    Twist_Test(
        tetromino_id="S",
        initial_position=Point(3, 1),
        initial_rotation=movement.rotate_ccw,
        initial_offset=movement.move_down,
        initial_state=State.THREE,
        square_positions=[
            Point(2, 0),
            Point(2, 1),
            Point(5, 0),
            Point(5, 2),
            Point(6, 0),
            Point(6, 1),
            Point(6, 2)
        ],
        rotation=movement.rotate_ccw,
        final_position=Point(3, 1),
        final_state=State.TWO
    ),
    Twist_Test(
        tetromino_id="Z",
        initial_position=Point(4, 1),
        initial_rotation=movement.rotate_cw,
        initial_offset=movement.move_down,
        initial_state=State.ONE,
        square_positions=[
            Point(3, 0),
            Point(3, 1),
            Point(3, 2),
            Point(4, 0),
            Point(4, 2),
            Point(7, 0),
            Point(7, 1)
        ],
        rotation=movement.rotate_cw,
        final_position=Point(4, 1),
        final_state=State.TWO
    ),
    Twist_Test(
        tetromino_id="S",
        initial_position=Point(2, 2),
        initial_rotation=movement.rotate_cw,
        initial_offset=None,
        initial_state=State.ONE,
        square_positions=[
            Point(2, 0),
            Point(2, 1),
            Point(3, 1),
            Point(5, 0),
            Point(6, 0),
            Point(6, 1)
        ],
        rotation=movement.rotate_cw,
        final_position=Point(3, 1),
        final_state=State.TWO
    ),
    Twist_Test(
        tetromino_id="Z",
        initial_position=Point(3, 3),
        initial_rotation=None,
        initial_offset=None,
        initial_state=State.ZERO,
        square_positions=[
            Point(3, 0),
            Point(3, 1),
            Point(3, 2),
            Point(4, 2),
            Point(5, 0),
            Point(5, 4),
            Point(6, 0),
            Point(6, 1),
            Point(6, 2),
            Point(6, 3),
            Point(6, 4)
        ],
        rotation=movement.rotate_ccw,
        final_position=Point(4, 1),
        final_state=State.THREE
    ),
    Twist_Test(
        tetromino_id="S",
        initial_position=Point(4, 3),
        initial_rotation=None,
        initial_offset=None,
        initial_state=State.ZERO,
        square_positions=[
            Point(3, 0),
            Point(3, 1),
            Point(3, 2),
            Point(3, 3),
            Point(3, 4),
            Point(4, 0),
            Point(4, 4),
            Point(5, 2),
            Point(6, 0),
            Point(6, 1),
            Point(6, 2)
        ],
        rotation=movement.rotate_cw,
        final_position=Point(3, 1),
        final_state=State.ONE
    ),
    Twist_Test(
        tetromino_id="L",
        initial_position=Point(3, 1),
        initial_rotation=movement.rotate_cw,
        initial_offset=None,
        initial_state=State.ONE,
        square_positions=[
            Point(2, 0),
            Point(2, 1),
            Point(5, 2),
            Point(6, 0),
            Point(6, 1),
            Point(6, 2)
        ],
        rotation=movement.rotate_cw,
        final_position=Point(3, 1),
        final_state=State.TWO
    ),
    Twist_Test(
        tetromino_id="J",
        initial_position=Point(2, 1),
        initial_rotation=movement.rotate_cw,
        initial_offset=None,
        initial_state=State.ONE,
        square_positions=[
            Point(2, 0),
            Point(2, 1),
            Point(4, 1),
            Point(5, 1),
            Point(6, 0),
            Point(6, 1)
        ],
        rotation=movement.rotate_ccw,
        final_position=Point(3, 0),
        final_state=State.ZERO
    ),
    Twist_Test(
        tetromino_id="L",
        initial_position=Point(4, 1),
        initial_rotation=movement.rotate_ccw,
        initial_offset=None,
        initial_state=State.THREE,
        square_positions=[
            Point(2, 0),
            Point(2, 1),
            Point(3, 1),
            Point(4, 1),
            Point(6, 0),
            Point(6, 1)
        ],
        rotation=movement.rotate_cw,
        final_position=Point(3, 0),
        final_state=State.ZERO
    ),
    Twist_Test(
        tetromino_id="L",
        initial_position=Point(1, 1),
        initial_rotation=movement.rotate_cw,
        initial_offset=None,
        initial_state=State.ONE,
        square_positions=[
            Point(3, 1),
            Point(3, 2),
            Point(4, 2),
            Point(5, 0),
            Point(5, 1),
            Point(5, 2)
        ],
        rotation=movement.rotate_ccw,
        final_position=Point(2, 0),
        final_state=State.ZERO
    ),
    Twist_Test(
        tetromino_id="J",
        initial_position=Point(6, 1),
        initial_rotation=movement.rotate_ccw,
        initial_offset=None,
        initial_state=State.THREE,
        square_positions=[
            Point(4, 0),
            Point(4, 1),
            Point(4, 2),
            Point(5, 2),
            Point(6, 1),
            Point(6, 2)
        ],
        rotation=movement.rotate_cw,
        final_position=Point(5, 0),
        final_state=State.ZERO
    ),
    Twist_Test(
        tetromino_id="L",
        initial_position=Point(5, 2),
        initial_rotation=movement.rotate_ccw,
        initial_offset=None,
        initial_state=State.THREE,
        square_positions=[
            Point(3, 0),
            Point(3, 1),
            Point(3, 2),
            Point(4, 2),
            Point(5, 0),
            Point(5, 2),
            Point(6, 0),
            Point(7, 0)
        ],
        rotation=movement.rotate_ccw,
        final_position=Point(4, 1),
        final_state=State.TWO
    ),
    Twist_Test(
        tetromino_id="J",
        initial_position=Point(2, 2),
        initial_rotation=movement.rotate_cw,
        initial_offset=None,
        initial_state=State.ONE,
        square_positions=[
            Point(3, 0),
            Point(4, 0),
            Point(4, 2),
            Point(5, 2),
            Point(6, 0),
            Point(6, 1),
            Point(6, 2)
        ],
        rotation=movement.rotate_cw,
        final_position=Point(3, 1),
        final_state=State.TWO
    ),
    Twist_Test(
        tetromino_id="L",
        initial_position=Point(5, 1),
        initial_rotation=movement.rotate_ccw,
        initial_offset=None,
        initial_state=State.THREE,
        square_positions=[
            Point(3, 0),
            Point(3, 1),
            Point(3, 2),
            Point(4, 2),
            Point(5, 0)
        ],
        rotation=movement.rotate_ccw,
        final_position=Point(4, 1),
        final_state=State.TWO
    ),
    Twist_Test(
        tetromino_id="J",
        initial_position=Point(2, 1),
        initial_rotation=movement.rotate_cw,
        initial_offset=None,
        initial_state=State.ONE,
        square_positions=[
            Point(4, 0),
            Point(5, 2),
            Point(6, 0),
            Point(6, 1),
            Point(6, 2)
        ],
        rotation=movement.rotate_cw,
        final_position=Point(3, 1),
        final_state=State.TWO
    ),
    Twist_Test(
        tetromino_id="L",
        initial_position=Point(4, 2),
        initial_rotation=movement.rotate_ccw,
        initial_offset=None,
        initial_state=State.THREE,
        square_positions=[
            Point(2, 0),
            Point(2, 1),
            Point(2, 2),
            Point(3, 2),
            Point(4, 0),
            Point(5, 0),
            Point(6, 0),
            Point(6, 1),
            Point(6, 2)
        ],
        rotation=movement.rotate_ccw,
        final_position=Point(3, 1),
        final_state=State.TWO
    ),
    Twist_Test(
        tetromino_id="J",
        initial_position=Point(2, 2),
        initial_rotation=movement.rotate_cw,
        initial_offset=None,
        initial_state=State.ONE,
        square_positions=[
            Point(2, 0),
            Point(2, 1),
            Point(2, 2),
            Point(3, 0),
            Point(4, 0),
            Point(5, 2),
            Point(6, 0),
            Point(6, 1),
            Point(6, 2)
        ],
        rotation=movement.rotate_cw,
        final_position=Point(3, 1),
        final_state=State.TWO
    ),
    Twist_Test(
        tetromino_id="L",
        initial_position=Point(2, 2),
        initial_rotation=movement.rotate_cw,
        initial_offset=None,
        initial_state=State.ONE,
        square_positions=[
            Point(2, 0),
            Point(2, 1),
            Point(4, 0),
            Point(5, 0),
            Point(5, 2),
            Point(6, 0),
            Point(6, 1),
            Point(6, 2)
        ],
        rotation=movement.rotate_cw,
        final_position=Point(3, 1),
        final_state=State.TWO
    ),
    Twist_Test(
        tetromino_id="J",
        initial_position=Point(4, 2),
        initial_rotation=movement.rotate_ccw,
        initial_offset=None,
        initial_state=State.THREE,
        square_positions=[
            Point(2, 0),
            Point(2, 1),
            Point(2, 2),
            Point(3, 0),
            Point(3, 2),
            Point(4, 0),
            Point(6, 0),
            Point(6, 1)
        ],
        rotation=movement.rotate_ccw,
        final_position=Point(3, 1),
        final_state=State.TWO
    ),
    Twist_Test(
        tetromino_id="L",
        initial_position=Point(4, 2),
        initial_rotation=movement.rotate_cw,
        initial_offset=None,
        initial_state=State.ONE,
        square_positions=[
            Point(4, 0),
            Point(6, 0),
            Point(6, 2),
            Point(7, 0),
            Point(7, 2),
            Point(8, 0),
            Point(8, 1),
            Point(8, 2)
        ],
        rotation=movement.rotate_cw,
        final_position=Point(5, 1),
        final_state=State.TWO
    ),
    Twist_Test(
        tetromino_id="J",
        initial_position=Point(4, 2),
        initial_rotation=movement.rotate_ccw,
        initial_offset=None,
        initial_state=State.THREE,
        square_positions=[
            Point(2, 0),
            Point(2, 1),
            Point(2, 2),
            Point(3, 0),
            Point(3, 2),
            Point(4, 0),
            Point(4, 2),
            Point(6, 2)
        ],
        rotation=movement.rotate_ccw,
        final_position=Point(3, 1),
        final_state=State.TWO
    )
]


def test_rotation_twists():
    for twist_test in twist_test_list:
        movement.board.current_tetromino = Tetromino(
            twist_test.tetromino_id, twist_test.initial_position, colors.ASH)
        if twist_test.initial_rotation is not None:
            twist_test.initial_rotation()
        if twist_test.initial_offset is not None:
            twist_test.initial_offset()
        assert (movement.board.current_tetromino.origin.x,
                movement.board.current_tetromino.origin.y) == (twist_test.initial_position.x, twist_test.initial_position.y)
        assert movement.board.current_tetromino.state == twist_test.initial_state
        for board_square_position in twist_test.square_positions:
            movement.board.fill_matrix(
                movement.board.board_tetrominos_matrix, Square(board_square_position))
        twist_test.rotation()
        assert (movement.board.current_tetromino.origin.x, movement.board.current_tetromino.origin.y) == (
            twist_test.final_position.x, twist_test.final_position.y)
        assert movement.board.current_tetromino.state == twist_test.final_state
        movement.board.clear_matrix(movement.board.board_tetrominos_matrix)


def test_hard_drop():
    for tetromino_id in tetrominos_id_list:
        for i in range(movement.board.width - get_tetromino_width(tetromino_id)):
            for j in range(movement.board.height - get_tetromino_height(tetromino_id)):
                movement.board.current_tetromino = Tetromino(
                    tetromino_id, Point(i, j), colors.ASH)
                position_before_move = movement.board.current_tetromino.origin
                movement.hard_drop()
                assert (movement.board.board_tetrominos[0].origin.x, movement.board.board_tetrominos[0].origin.y) == (
                    position_before_move.x, 0)
                assert movement.board.holdable is True
                movement.board.board_tetrominos = []
                movement.board.update_matrices()
