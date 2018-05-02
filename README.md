# Python Tetris
A Tetris clone written entirely in `python`.

## Dependencies
Python Tetris requires [python3](https://www.python.org/download/releases/3.0/) and [pyglet](https://bitbucket.org/pyglet/pyglet/wiki/Home) to be installed in order to run.

## Usage
Before starting Python Tetris, ensure that a configuration file exists at `src/config.py`.
If it doesn't, you can copy the example configuration file at `src/config.py.example`.

To start Python Tetris, run the `python-tetris.py` script located in the `src` directory.

    src/python-tetris.py


## Running Tests
Unit tests can be run using [pytest](https://docs.pytest.org/en/latest/).

To run all tests recursively, run `pytest` at the project's root directory.

To run single test file, run `pytest` followed by the path to the file. For example,

    pytest src/tetromino/tetromino_test.py
