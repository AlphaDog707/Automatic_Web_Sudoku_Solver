import pyautogui as pg
import time

grid = []

while True:
    row = list(input('Row: '))
    ints = []

    for n in row:
        ints.append(int(n))
    grid.append(ints)

    if len(grid) == 9:
        break
    print('Row ' + str(len(grid)) + ' Complete')

time.sleep(3)


def possible(row, column, number):
    global grid
    # Is the number appearing in the given row?
    for i in range(0, 9):
        if grid[row][i] == number:
            return False

    # Is the number appearing in the given column?
    for i in range(0, 9):
        if grid[i][column] == number:
            return False

    # Is the number appearing in the given square?
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == number:
                return False

    return True


def solveSudoku():
    global grid
    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solveSudoku()
                        grid[row][column] = 0

                return

    outputOnWebsite(grid)
    # input('More possible solutions')


def outputOnWebsite(matrix):
    final = []
    str_fin = []
    for i in range(9):
        final.append(matrix[i])

    for lists in final:
        for num in lists:
            str_fin.append(str(num))

    counter = []

    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter)%9 == 0:
            pg.hotkey('down')
            for i in range(8):
                pg.hotkey('left')

solveSudoku()










