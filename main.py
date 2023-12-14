solution = [[3, 4, 6, 1, 2, 7, 9, 5, 8],
            [7, 8, 5, 6, 9, 4, 1, 3, 2],
            [2, 1, 9, 3, 8, 5, 4, 6, 7],
            [4, 6, 2, 5, 3, 1, 8, 7, 9],
            [9, 3, 1, 2, 7, 8, 6, 4, 5],
            [8, 5, 7, 9, 4, 6, 2, 1, 3],
            [5, 9, 8, 4, 1, 3, 7, 2, 6],
            [6, 2, 4, 7, 5, 9, 3, 8, 1],
            [1, 7, 3, 8, 6, 2, 5, 9, 4]]

puzzle = [[0, 0, 6, 1, 0, 0, 0, 0, 8],
          [0, 8, 0, 0, 9, 0, 0, 3, 0],
          [2, 0, 0, 0, 0, 5, 4, 0, 0],
          [4, 0, 0, 0, 0, 1, 8, 0, 0],
          [0, 3, 0, 0, 7, 0, 0, 4, 0],
          [0, 0, 7, 9, 0, 0, 0, 0, 3],
          [0, 0, 8, 4, 0, 0, 0, 0, 6],
          [0, 2, 0, 0, 5, 0, 0, 8, 0],
          [1, 0, 0, 0, 0, 2, 5, 0, 0]]


def solver():
    transposed = [list(i) for i in zip(*puzzle)]
    candidates = dict()
    keys = [(0, 3), (3, 6), (6, 9)]
    row_point = None
    col_point = None

    for x in range(len(puzzle)):
        for y in range(len(puzzle[0])):
            candidates['canFor{}_{}'.format(x, y)] = list()

    for x in range(len(puzzle)):
        if x < 3:
            row_point = keys[0]
        elif x < 6:
            row_point = keys[1]
        elif x < 9:
            row_point = keys[2]
        for y in range(len(puzzle[0])):
            if y < 3:
                col_point = keys[0]
            elif y < 6:
                col_point = keys[1]
            elif y < 9:
                col_point = keys[2]
            if puzzle[x][y] == 0:
                for z in range(1, 10):
                    if z not in puzzle[x] and z not in transposed[y] \
                            and z not in [puzzle[row][col] for col in range(*col_point) for row in range(*row_point)]:
                        candidates['canFor{}_{}'.format(x, y)].append(z)
    print(candidates)


solver()
