def kick_test(tetromino, matrix, offset):
    for s in tetromino.sqrs:
        if matrix[s.x][s.y] == 1:
