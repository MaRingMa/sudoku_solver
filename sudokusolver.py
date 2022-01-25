"""
Sudoku solver - solves sudoku
Author : Martin Ringmaier
"""


def print_sudo(grid):
    """ prints sudoku table"""
    for k in range(3):
        for x in range(3):
            for c in range(3):
                b = k*3+c
                print("|", end=" ")
                for y in range(3):
                    print(grid[b][y+x*3], end=" ")
                print("|", end=" ")
            print()
        print("-----------------------------")


def fill_sudo(grid):
    """ input of numbers from starting sudoku"""
    print("1,2,3,4,5,6,7,8,9\n")
    for x in range(9):
        a = str.split(input(), ",")
        for y in range(9):
            grid[x][y] = int(a[y])
    return grid


def print_supp(supp):
    """ prints taken/ empty positions"""
    for k in range(3):
        for x in range(3):
            for c in range(3):
                b = k*3+c
                print("|", end=" ")
                for y in range(3):
                    print(supp[b][y+x*3][0], end=" ")
                print("|", end=" ")
            print()
        print("-----------------------------")


def fill_supp(grid, supp):
    """ fills support table if there's number in final table"""
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                supp[x][y][0] = 0
            if grid[x][y] != 0:
                for i in range(1, 10):
                    supp[x][y][i] = 0
    return supp


def check_x(grid, supp):
    """ search row for unusable numbers"""
    row_num = []
    for z in range(3):
        for c in range(3):
            for x in range(3):
                for y in range(3):
                    a = x+z*3
                    b = y+c*3
                    if grid[a][b] != 0:
                        # print("x = ", a, "  y = ", b, "  ",grid[a][b])
                        row_num.append(grid[a][b])

            supp = check_sup_x(supp, row_num, z, c)
            row_num = []
            # print("-------------------")
    return supp


def check_y(grid, supp):
    """ search a column for unusable numbers"""
    col_num = []
    for z in range(3):
        for c in range(3):
            for x in range(3):
                for y in range(3):
                    a = x*3+z
                    b = y*3+c
                    if grid[a][b] != 0:
                        # print("x = ", a, "  y = ", b, "  ",grid[a][b])
                        col_num.append(grid[a][b])

            supp = check_sup_y(supp, col_num, z, c)
            col_num = []
            # print("-------------------")
    return supp


def check_sup_x(supp, row_num, z, c):
    """ delete unusable numbers from rows """
    for x in range(3):
        for y in range(3):
            for k in row_num:
                supp[x+z*3][y+c*3][k] = 0
    return supp


def check_sup_y(supp, col_num, z, c):
    """ delete unusable numbers from columns"""
    for x in range(3):
        for y in range(3):
            for k in col_num:
                supp[x*3+z][y*3+c][k] = 0
    return supp


def check_box(grid, supp):
    """ search box for unusable numbers and delete them"""
    box_num = []
    for x in range(9):
        for y in range(9):
            if grid[x][y] != 0:
                box_num.append(grid[x][y])
        for z in box_num:
            for a in range(9):
                supp[x][a][z] = 0
        box_num = []

    return supp


def check_unique(grid, supp):
    """ check for unique numbers in row, column and box"""
    current = []
    for rx in range(3):
        for ry in range(3):
            supp = check_all(supp, grid)
            for x in range(3):
                for y in range(3):
                    for i in range(1, 10):
                        if(supp[rx*3+x][ry*3+y][i] == 1):
                            current.append(i)

            for c in range(1, 10):
                if(current.count(c) == 1):
                    for x in range(3):
                        for y in range(3):
                            if(supp[rx*3+x][ry*3+y][c] == 1):
                                grid[rx*3+x][ry*3+y] = c
                                supp[rx*3+x][ry*3+y][0] = 1
                                for i in range(1, 10):
                                    supp[rx*3+x][ry*3+y][i] = 0
            current = []
            supp = check_all(supp, grid)
            for x in range(3):
                for y in range(3):
                    for i in range(1, 10):
                        if (supp[x*3+rx][y*3+ry][i] == 1):
                            current.append(i)

            for c in range(1, 10):
                if(current.count(c) == 1):
                    for x in range(3):
                        for y in range(3):
                            if(supp[x*3+rx][y*3+ry][c] == 1):
                                grid[x*3+rx][y*3+ry] = c
                                supp[x*3+rx][y*3+ry][0] = 1
                                for i in range(1, 10):
                                    supp[x*3+rx][y*3+ry][i] = 0
            current = []

    return grid, supp


def printsuppx(supp):
    """ prints (un)usable numbers for each cell"""
    for k in range(3):
        for x in range(3):
            for c in range(3):
                b = k*3+c
                print("|", end=" ")
                for y in range(3):
                    for z in range(1, 10):
                        print(supp[b][y+x*3][z], end="")
                    print(" |", end=" ")
                print("|", end=" ")
            print()
        print("-----------------------------")


def check_all(supp, grid):
    """ chceck whole grid for unusable numbers"""
    supp = check_x(grid, supp)
    supp = check_y(grid, supp)
    supp = check_box(grid, supp)
    return supp


def test_solve(supp, grid):
    """ fills numbers into grid"""
    for x in range(9):
        for y in range(9):
            a = 0
            if supp[x][y][0] == 0:
                for i in range(1, 10):
                    a = a + supp[x][y][i]
                if a == 1:
                    for i in range(1, 10):
                        if supp[x][y][i] == 1:
                            grid[x][y] = i
    return grid


def check_for_solve(grid):
    """ checks if grid is full / filled"""
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                return False
    return True


def solve(grid, supp):
    """ solves sudoku / main function"""
    a = 0
    while ((not check_for_solve(grid)) and (a < 1000)):
        a = a + 1
        grid, supp = check_unique(grid, supp)
        supp = check_all(supp, grid)
        grid = test_solve(supp, grid)
    if a == 1000:
        print("Program se zasekl na : ")
        print_sudo(grid)
        printsuppx(supp)
        return

    print("Výsledek : ")
    print("-----------------------------")
    print_sudo(grid)
    print("\nPočet projetí : ", a)


if __name__ == "__main__":
    grid_main = [[0 for x in range(9)] for y in range(9)]
    supp_main = [[[1 for x in range(10)] for y in range(9)] for z in range(9)]
    print("Čísla zadávejte na řádek po 'čtverečkách' oddělená čárkou. \
        Zleva doprava.")
    print("0 značí prázdné místo")
    grid_main = fill_sudo(grid_main)
    supp_main = fill_supp(grid_main, supp_main)
    print("\n\n\n\n")
    # printsuppx(supp)
    print("Zadáno : ")
    print("-----------------------------")
    print_sudo(grid_main)
    print()
    solve(grid_main, supp_main)
