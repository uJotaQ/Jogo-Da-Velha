import os


def show_symbol(m):
    if m == 0:
        print(" ", end="")
    elif m == 1:
        print("X", end="")
    elif m == 2:
        print("O", end="")


def show_table(m):
    os.system('cls')
    print("\033[31m-\033[0;0m"*30)
    print(" "*8, ("\033[32mJogo Da Velha\033[0;0m"), " "*18)
    print("\033[31m-\033[0;0m"*30)
    print(" "*8, "\033[34mC1.\033[0;0m", " "*1, "\033[34mC2.\033[0;0m",
          " "*1, "\033[34mC3.\033[0;0m")
    print()
    print(" "*3, "\033[31mL1.\033[0;0m", " "*1,
          show_symbol(m[0][0]), " \033[32m|\033[0;0m ", show_symbol(m[0][1]),
          " \033[32m|\033[0;0m ", show_symbol(m[0][2]))
    print(" "*7, "\033[32m-\033[0;0m"*17)
    print(" "*3, "\033[31mL2.\033[0;0m",
          " "*1, show_symbol(m[1][0]), " \033[32m|\033[0;0m ",
          show_symbol(m[1][1]), " \033[32m|\033[0;0m ", show_symbol(m[1][2]))
    print(" "*7, "\033[32m-\033[0;0m"*17)
    print(" "*3, "\033[31mL3.\033[0;0m",
          " "*1, show_symbol(m[2][0]), " \033[32m|\033[0;0m ",
          show_symbol(m[2][1]), " \033[32m|\033[0;0m ", show_symbol(m[2][2]))
    print()


def put_x():
    valid_pick: bool = False
    while valid_pick is False:
        pick_line = int(input("Em qual Linha (L) deseja colocar o 'x': "))
        if pick_line == 1:
            pick_line = 0
        elif pick_line == 2:
            pick_line = 1
        elif pick_line == 3:
            pick_line = 2
        pick_colum = int(input("Em qual Coluna (C) deseja colocar o 'x': "))
        if pick_colum == 1:
            pick_colum = 0
        elif pick_colum == 2:
            pick_colum = 1
        elif pick_colum == 3:
            pick_colum = 2
        if matriz[pick_line][pick_colum] == 0:
            matriz[pick_line][pick_colum] = 1
            valid_pick = True
        else:
            valid_pick = False


def put_o():
    valid_pick: bool = False
    while valid_pick is False:
        pick_line = int(input("Em qual Linha (L) deseja colocar o 'O': "))
        if pick_line == 1:
            pick_line = 0
        elif pick_line == 2:
            pick_line = 1
        elif pick_line == 3:
            pick_line = 2
        pick_colum = int(input("Em qual Coluna (C) deseja colocar o 'O': "))
        if pick_colum == 1:
            pick_colum = 0
        elif pick_colum == 2:
            pick_colum = 1
        elif pick_colum == 3:
            pick_colum = 2
        if matriz[pick_line][pick_colum] == 0:
            matriz[pick_line][pick_colum] = 2
            valid_pick = True
        else:
            valid_pick = False


matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(4):
    show_table(matriz)
    put_x()
    show_table(matriz)
    put_o()
