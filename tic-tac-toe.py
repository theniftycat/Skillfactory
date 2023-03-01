# display the field
F = [[" ", "1", "2", "3"],
     ["1", "-", "-", "-"],
     ["2", "-", "-", "-"],
     ["3", "-", "-", "-"]]
for line in F:
    print ('  '.join(map(str, line)))
# ask Player 1 to place X
n = 1
while True:
    print("Player 1, make a move! First, select a row.")
    a = int(input())
    while a < 1 or a > 3:
        print("Oops! wrong number, try again!")
        a = int(input())
    print("Now select a column!")
    b = int(input())
    while b < 1 or b > 3:
        print("Oops! wrong number, try again!")
        b = int(input())
    while F[a][b] == "O" or F[a][b] == "X":
        print("Place already taken! Pick another one! First, select a row.")
        a = int(input())
        while a < 1 or a > 3:
            print("Oops! wrong number, try again!")
            a = int(input())
        print("Now select a column!")
        b = int(input())
        while b < 1 or b > 3:
            print("Oops! wrong number, try again!")
            b = int(input())
    F[a][b] = "X"
    n += 1
    for line in F:
        print ('  '.join(map(str, line)))
    if n > 9:
        print("Looks like there's no winners!")
        break
    if (F[1][1] == "X" and F[1][2] == "X" and F[1][3] == "X") or (F[2][1] == "X" and F[2][2] == "X" and F[2][3] == "X") or (F[3][1] == "X" and F[3][2] == "X" and F[3][3] == "X") or (F[1][1] == "X" and F[2][1] == "X" and F[3][1] == "X") or (F[1][2] == "X" and F[2][2] == "X" and F[3][2] == "X") or (F[1][3] == "X" and F[2][3] == "X" and F[3][3] == "X") or (F[1][1] == "X" and F[2][2] == "X" and F[3][3] == "X") or (F[3][1] == "X" and F[2][2] == "X" and F[1][3] == "X"):
        print("Player 1 won!")
        break

    # ask Player 2 to place O
    print("Player 2, make a move! First, select a row.")
    a = int(input())
    while a < 1 or a > 3:
        print("Oops! wrong number, try again!")
        a = int(input())
    print("Now select a column!")
    b = int(input())
    while b < 1 or b > 3:
        print("Oops! wrong number, try again!")
        b = int(input())
    while F[a][b] == "O" or F[a][b] == "X":
        print("Place already taken! Pick another one! First, select a row.")
        a = int(input())
        while a < 1 or a > 3:
            print("Oops! wrong number, try again!")
            a = int(input())
        print("Now select a column!")
        b = int(input())
        while b < 1 or b > 3:
            print("Oops! wrong number, try again!")
            b = int(input())
    F[a][b] = "O"
    n += 1
    for line in F:
        print ('  '.join(map(str, line)))
    if (F[1][1] == "O" and F[1][2] == "O" and F[1][3] == "O") or (F[2][1] == "O" and F[2][2] == "O" and F[2][3] == "O") or (F[3][1] == "O" and F[3][2] == "O" and F[3][3] == "O") or (F[1][1] == "O" and F[2][1] == "O" and F[3][1] == "O") or (F[1][2] == "O" and F[2][2] == "O" and F[3][2] == "O") or (F[1][3] == "O" and F[2][3] == "O" and F[3][3] == "O") or (F[1][1] == "O" and F[2][2] == "O" and F[3][3] == "O") or (F[3][1] == "O" and F[2][2] == "O" and F[1][3] == "O"):
        print("Player 2 won!")
        break
