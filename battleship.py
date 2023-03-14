# вывести поля
F1 = [[" ", "1", "2", "3", "4", "5", "6"],
     ["1", "O", "O", "O", "O", "O", "O"],
     ["2", "O", "O", "O", "O", "O", "O"],
     ["3", "O", "O", "O", "O", "O", "O"],
     ["4", "O", "O", "O", "O", "O", "O"],
     ["5", "O", "O", "O", "O", "O", "O"],
     ["6", "O", "O", "O", "O", "O", "O"]]

F2 = [[" ", "1", "2", "3", "4", "5", "6"],
     ["1", "O", "O", "O", "O", "O", "O"],
     ["2", "O", "O", "O", "O", "O", "O"],
     ["3", "O", "O", "O", "O", "O", "O"],
     ["4", "O", "O", "O", "O", "O", "O"],
     ["5", "O", "O", "O", "O", "O", "O"],
     ["6", "O", "O", "O", "O", "O", "O"]]

F3 = [[" ", "1", "2", "3", "4", "5", "6"],
     ["1", "O", "O", "O", "O", "O", "O"],
     ["2", "O", "O", "O", "O", "O", "O"],
     ["3", "O", "O", "O", "O", "O", "O"],
     ["4", "O", "O", "O", "O", "O", "O"],
     ["5", "O", "O", "O", "O", "O", "O"],
     ["6", "O", "O", "O", "O", "O", "O"]]

# задать класс корабли
class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length

ships = [
    {
    "name": "big_ship",
    "length": 3,
    },
    {
    "name": "medium_ship1",
    "length": 2,
    },
    {
    "name": "medium_ship2",
    "length": 2,
    },
    {
    "name": "small_ship1",
    "length": 1,
    },
    {
    "name": "small_ship2",
    "length": 1,
    },
    {
    "name": "small_ship3",
    "length": 1,
    },
    {
    "name": "small_ship4",
    "length": 1,
    },
]

#Генерация поля игрока
#Изначально я пробовала сделать так, чтобы программа случайно выбирала координаты два раза из списка от 1 до 6, но там не получалась корректная проверка занятости точек.
#4 корабля в 1 точку длиной не всегда помещаются в поле.
coordinates = [11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56, 61, 62, 63, 64, 65, 66]
coordinates1 = [11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56, 61, 62, 63, 64, 65, 66]


import random


for ship in ships:
    ship_obj = Ship(name=ship.get("name"),
                    length=ship.get("length"))
    try:
        start = random.choice(coordinates1)
    except IndexError:
        print("Ошибка генерации поля. Все корабли не влезли. Перезапустите программу!")
        quit()
    st_str = repr(start)
    last_digit_str = st_str[-1]
    last_digit = int(last_digit_str)
    first_digit = start // 10
    F1[first_digit][last_digit] = "■"
    try:
        coordinates1.remove(start)
    except ValueError:
        print("Все клетки уже заняты!")
        quit()

    # Функции удаления смежных координатов, чтобы не ставить корабли по близости.

    def up1():
        global coordinates1
        try:
            coordinates1.remove(start - 21)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates1.remove(start - 19)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates1.remove(start - 20)
        except ValueError:
            pass
        except IndexError:
            pass

    def down1():
        global coordinates1
        try:
            coordinates1.remove(start + 21)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates1.remove(start + 19)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates1.remove(start + 20)
        except ValueError:
            pass
        except IndexError:
            pass

    def up2():
        global coordinates1
        try:
            coordinates1.remove(start - 31)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates1.remove(start - 29)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates1.remove(start - 30)
        except ValueError:
            pass
        except IndexError:
            pass

    def down2():
        global coordinates1
        try:
            coordinates1.remove(start + 31)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates1.remove(start + 29)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates1.remove(start + 30)
        except ValueError:
            pass
        except IndexError:
            pass

    def left1():
        global coordinates1
        try:
            coordinates1.remove(start + 8)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates1.remove(start - 12)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates1.remove(start - 2)
        except ValueError:
            pass
        except IndexError:
            pass

    def right1():
        global coordinates1
        try:
            coordinates1.remove(start - 8)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates1.remove(start + 12)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates1.remove(start + 2)
        except ValueError:
            pass
        except IndexError:
            pass

    def left2():
        global coordinates1
        try:
            coordinates1.remove(start + 7)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates1.remove(start - 13)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates1.remove(start - 3)
        except ValueError:
            pass
        except IndexError:
            pass

    def right2():
        global coordinates1
        try:
            coordinates1.remove(start - 7)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates1.remove(start + 13)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates1.remove(start + 3)
        except ValueError:
            pass
        except IndexError:
            pass

# Добавление ячеек к длинным кораблям

    try:
        if ship_obj.length > 1:
            orient = ["down", "right", "up", "left"]
            orientation = random.choice(orient)

    # 2 down

            if orientation == "down":
                if (start + 10) not in coordinates1 or first_digit == 6:
                    F1[first_digit - 1][last_digit] = "■"
                    up1()

    # 2 down straight

                else:
                    F1[first_digit+1][last_digit] = "■"
                    down1()

    # 2 up

            if orientation == "up":
                if (start - 10) not in coordinates1 or first_digit == 1:
                    F1[first_digit + 1][last_digit] = "■"
                    down1()

    # 2 up straight

                else:
                    F1[first_digit - 1][last_digit] = "■"
                    up1()

    # 2 right

            if orientation == "right":
                if (start + 1) not in coordinates1 or last_digit == 6:
                    F1[first_digit][last_digit-1] = "■"
                    left1()

    # 2 right straight

                else:
                    F1[first_digit][last_digit+1] = "■"
                    right1()

    # 2 left

            if orientation == "left":
                if (start - 1) not in coordinates1 or last_digit == 1:
                    F1[first_digit][last_digit + 1] = "■"
                    right1()

    # 2 left straight

                else:
                    F1[first_digit][last_digit - 1] = "■"
                    left1()

    # 3 down

            if ship_obj.length == 3:
                if orientation == "down":
                    if first_digit == 6:
                        F1[first_digit-2][last_digit] = "■"
                        up2()

                    elif first_digit + 2 > 6:
                        F1[first_digit - 1][last_digit] = "■"
                        up1()

                    else:
                        F1[first_digit + 2][last_digit] = "■"
                        down2()

    # 3 up

                if orientation == "up":
                    if first_digit == 1:
                        F1[first_digit+2][last_digit] = "■"
                        down2()

                    elif first_digit - 2 < 1:
                        F1[first_digit + 1][last_digit] = "■"
                        down1()

                    else:
                        F1[first_digit - 2][last_digit] = "■"
                        up2()

    # 3 right

                if orientation == "right":
                    if last_digit == 6:
                        F1[first_digit][last_digit-2] = "■"
                        left2()

                    elif last_digit + 2 > 6:
                        F1[first_digit][last_digit - 1] = "■"
                        left1()

                    else:
                        F1[first_digit][last_digit + 2] = "■"
                        right2()

    # 3 left

                if orientation == "left":
                    if last_digit == 1:
                        F1[first_digit][last_digit+2] = "■"
                        right2()

                    elif last_digit - 2 < 1:
                        F1[first_digit][last_digit + 1] = "■"
                        right1()

                    else:
                        F1[first_digit][last_digit - 2] = "■"
                        left2()

        try:
            coordinates1.remove(start - 11)
        except ValueError:
            pass
        try:
            coordinates1.remove(start - 9)
        except ValueError:
            pass
        try:
            coordinates1.remove(start + 11)
        except ValueError:
            pass
        try:
            coordinates1.remove(start + 9)
        except ValueError:
            pass
        try:
            coordinates1.remove(start - 10)
        except ValueError:
            pass
        try:
            coordinates1.remove(start - 1)
        except ValueError:
            pass
        try:
            coordinates1.remove(start + 1)
        except ValueError:
            pass
        try:
            coordinates1.remove(start + 10)
        except ValueError:
            pass
    except IndexError:
        print("Ошибка генерации поля. Перезапустите программу.")
        quit()
    for i in range(6):
        if F1[0][i] == "■" or F1[i][0] == "■":
            print("Корабли вылезли за сетку. Перезапустите программу.")
            quit()

    # Генерация поля компьютера

for ship in ships:
    ship_obj = Ship(name=ship.get("name"),
                    length=ship.get("length"))
    try:
        start = random.choice(coordinates)
    except IndexError:
        print("Ошибка генерации поля. Все корабли не влезли. Перезапустите программу!")
        quit()
    st_str = repr(start)
    last_digit_str = st_str[-1]
    last_digit = int(last_digit_str)
    first_digit = start // 10
    F2[first_digit][last_digit] = "■"
    try:
        coordinates.remove(start)
    except ValueError:
        print("Все клетки уже заняты!")
        quit()

    # functions

    def upc1():
        global coordinates
        try:
            coordinates.remove(start - 21)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates.remove(start - 19)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates.remove(start - 20)
        except ValueError:
            pass
        except IndexError:
            pass

    def downc1():
        global coordinates
        try:
            coordinates.remove(start + 21)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates.remove(start + 19)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates.remove(start + 20)
        except ValueError:
            pass
        except IndexError:
            pass

    def upc2():
        global coordinates
        try:
            coordinates.remove(start - 31)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates.remove(start - 29)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates.remove(start - 30)
        except ValueError:
            pass
        except IndexError:
            pass

    def downc2():
        global coordinates
        try:
            coordinates.remove(start + 31)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates.remove(start + 29)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates.remove(start + 30)
        except ValueError:
            pass
        except IndexError:
            pass

    def leftc1():
        global coordinates
        try:
            coordinates.remove(start + 8)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates.remove(start - 12)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates.remove(start - 2)
        except ValueError:
            pass
        except IndexError:
            pass

    def rightc1():
        global coordinates
        try:
            coordinates.remove(start - 8)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates.remove(start + 12)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates.remove(start + 2)
        except ValueError:
            pass
        except IndexError:
            pass

    def leftc2():
        global coordinates
        try:
            coordinates.remove(start + 7)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates.remove(start - 13)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates.remove(start - 3)
        except ValueError:
            pass
        except IndexError:
            pass

    def rightc2():
        global coordinates
        try:
            coordinates.remove(start - 7)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates.remove(start + 13)
        except ValueError:
            pass
        except IndexError:
            pass
        try:
            coordinates.remove(start + 3)
        except ValueError:
            pass
        except IndexError:
            pass

    try:
        if ship_obj.length > 1:
            orient = ["down", "right", "up", "left"]
            orientation = random.choice(orient)

    # 2 down

            if orientation == "down":
                if (start + 10) not in coordinates or first_digit + 1 > 6:
                    F2[first_digit - 1][last_digit] = "■"
                    upc1()

    # 2 down straight

                else:
                    F2[first_digit+1][last_digit] = "■"
                    downc1()

    # 2 up

            if orientation == "up":
                if (start - 10) not in coordinates or first_digit - 1 < 1:
                    F2[first_digit + 1][last_digit] = "■"
                    downc1()

    # 2 up straight

                else:
                    F2[first_digit - 1][last_digit] = "■"
                    upc1()

    # 2 right

            if orientation == "right":
                if (start + 1) not in coordinates or last_digit + 1 > 6:
                    F2[first_digit][last_digit-1] = "■"
                    leftc1()

    # 2 right straight

                else:
                    F2[first_digit][last_digit+1] = "■"
                    rightc1()

    # 2 left

            if orientation == "left":
                if (start - 1) not in coordinates or last_digit - 1 < 1 :
                    F2[first_digit][last_digit + 1] = "■"
                    rightc1()

    # 2 left straight

                else:
                    F2[first_digit][last_digit - 1] = "■"
                    leftc1()

    # 3 down

            if ship_obj.length == 3:
                if orientation == "down":
                    if first_digit == 6:
                        F2[first_digit-2][last_digit] = "■"
                        upc2()

                    elif first_digit + 2 > 6:
                        F2[first_digit - 1][last_digit] = "■"
                        upc1()

                    else:
                        F2[first_digit + 2][last_digit] = "■"
                        downc2()

    # 3 up

                if orientation == "up":
                    if first_digit == 1:
                        F2[first_digit+2][last_digit] = "■"
                        downc2()

                    elif first_digit - 2 < 1:
                        F2[first_digit + 1][last_digit] = "■"
                        downc1()

                    else:
                        F2[first_digit - 2][last_digit] = "■"
                        upc2()

    # 3 right

                if orientation == "right":
                    if last_digit == 6:
                        F2[first_digit][last_digit-2] = "■"
                        leftc2()

                    elif last_digit + 2 > 6:
                        F2[first_digit][last_digit - 1] = "■"
                        leftc1()

                    else:
                        F2[first_digit][last_digit + 2] = "■"
                        rightc2()

    # 3 left

                if orientation == "left":
                    if last_digit == 1:
                        F2[first_digit][last_digit+2] = "■"
                        rightc2()

                    elif last_digit - 2 < 1:
                        F2[first_digit][last_digit + 1] = "■"
                        rightc1()

                    else:
                        F2[first_digit][last_digit - 2] = "■"
                        leftc2()

        try:
            coordinates.remove(start - 11)
        except ValueError:
            pass
        try:
            coordinates.remove(start - 9)
        except ValueError:
            pass
        try:
            coordinates.remove(start + 11)
        except ValueError:
            pass
        try:
            coordinates.remove(start + 9)
        except ValueError:
            pass
        try:
            coordinates.remove(start - 10)
        except ValueError:
            pass
        try:
            coordinates.remove(start - 1)
        except ValueError:
            pass
        try:
            coordinates.remove(start + 1)
        except ValueError:
            pass
        try:
            coordinates.remove(start + 10)
        except ValueError:
            pass
    except IndexError:
        print("Ошибка генерации поля. Перезапустите программу.")
        quit()
    for i in range(6):
        if F1[0][i] == "■" or F1[i][0] == "■":
            print("Корабли вылезли за сетку. Перезапустите программу.")
            quit()

print("\nПоле игрока:\n")
for line in F1:
    print ('  '.join(map(str, line)))

print("\nПоле компьютера:\n")
for line in F3:
    print ('  '.join(map(str, line)))

# Счетчики ходов
n = 1
m = 1

# Переменные
first_d_hit = 0
last_d_hit = 0
F4 = F1
coordinates2 = [11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56, 61, 62, 63, 64, 65, 66]
coordinates3 = [11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56, 61, 62, 63, 64, 65, 66]
targets = []
miss = False

# ход игрока
while True:
    print("Ваш ход!")
    try:
        print("Выберите строку!")
        x = int(input())
        while x < 1 or x > 6:
            print("Ой! Не то число! Попробуйте снова!")
            a = int(input())
    except TypeError:
        print("Выберите строку!")
        x = int(input())
    except ValueError:
        print("Выберите строку!")
        x = int(input())
    try:
        print("А теперь выберите столбец!")
        y = int(input())
        while y < 1 or y > 6:
            print("Ой! Не то число! Выберите столбец снова!")
            y = int(input())
    except ValueError:
        print("Выберите столбец!")
        y = int(input())
    except TypeError:
        print("Выберите столбец!")
        y = int(input())

    while F2[x][y] == "T" or F2[x][y] == "X":
        try:
            print("Вы сюда уже стреляли! Выберите строку!")
            x = int(input())
            while x < 1 or x > 6:
                print("Ой! Не то число! Попробуйте снова!")
                a = int(input())
        except TypeError:
            print("Выберите строку!")
            x = int(input())
        except ValueError:
            print("Выберите строку!")
            x = int(input())
        try:
            print("А теперь выберите столбец!")
            y = int(input())
            while y < 1 or y > 6:
                print("Ой! Не то число! Выберите столбец снова!")
                y = int(input())
        except ValueError:
            print("Выберите столбец!")
            y = int(input())
        except TypeError:
            print("Выберите столбец!")
            y = int(input())


    # проверка попадания

    if F2[x][y] == "■":
        F2[x][y] = "X"
        F3[x][y] = "X"
        print("Прямо в цель!")
        n+=1
        if n == 12:
            print("Вы победили!")
            print("\nПоле компьютера:\n")
            for line in F3:
                print('  '.join(map(str, line)))
            break

# Выделение клеток вокруг корабля
        try:
            if F2[x][y] == "X" and F2[x - 1][y] == "X":
                try:
                    if F2[x - 2][y] == "O" or int('%i%i' % (x - 2, y)) not in coordinates3:
                        try:
                            F2[x - 2][y] = "-"
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F2[x - 2][y - 1] == "O" or int('%i%i' % (x - 2, y-1)) not in coordinates3:
                        try:
                            F2[x - 2][y - 1] = "-"
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F2[x - 2][y + 1] == "O" or int('%i%i' % (x - 2, y+1)) not in coordinates3:
                        try:
                            F2[x - 2][y + 1] = "-"
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
        except IndexError:
            pass

        try:
            if F2[x][y] == "X" and F2[x + 1][y] == "X":
                try:
                    if F2[x + 2][y] == "O" or int('%i%i' % (x + 2, y)) not in coordinates3:
                        try:
                            F2[x + 2][y] = "-"
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F2[x + 2][y - 1] == "O" or int('%i%i' % (x + 2, y-1)) not in coordinates3:
                        try:
                            F2[x + 2][y - 1] = "-"
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F2[x + 2][y + 1] == "O" or int('%i%i' % (x + 2, y+1)) not in coordinates3:
                        try:
                            F2[x + 2][y + 1] = "-"
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
        except IndexError:
            pass

        try:
            if F2[x][y] == "X" and F2[x][y + 1] == "X":
                try:
                    if F2[x][y + 2] == "O" or int('%i%i' % (x, y+2)) not in coordinates3:
                        try:
                            F2[x][y + 2] = "-"
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F2[x - 1][y + 2] == "O" or int('%i%i' % (x-1, y+2)) not in coordinates3:
                        try:
                            F2[x - 1][y + 2] = "-"
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F2[x + 1][y + 2] == "O" or int('%i%i' % (x+1, y+2)) not in coordinates3:
                        try:
                            F2[x + 1][y + 2] = "-"
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
        except IndexError:
            pass

        try:
            if F2[x][y] == "X" and F2[x][y - 1] == "X":
                try:
                    if F2[x][y - 2] == "O" or int('%i%i' % (x, y-2)) not in coordinates3:
                        try:
                            F2[x][y - 2] = "-"
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F2[x - 1][y - 2] == "O" or int('%i%i' % (x-1, y-2)) not in coordinates3:
                        try:
                            F2[x - 1][y - 2] = "-"
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F2[x + 1][y - 2] == "O" or int('%i%i' % (x+1, y-2)) not in coordinates3:
                        try:
                            F2[x + 1][y - 2] = "-"
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
        except IndexError:
            pass

        try:
            if F2[x][y] == "X" and F2[x - 1][y] == "X" and F2[x - 2][
                y] == "X":
                try:
                    if F2[x - 3][y] == "O" or int('%i%i' % (x-3, y)) not in coordinates3:
                        try:
                            F2[x - 3][y] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x - 3][y - 1] == "O" or int('%i%i' % (x-3, y-1)) not in coordinates3:
                        try:
                            F2[x - 3][y - 1] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x - 3][y + 1] == "O" or int('%i%i' % (x-3, y+1)) not in coordinates3:
                        try:
                            F2[x - 3][y + 1] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x - 2][y - 1] == "O" or int('%i%i' % (x-2, y-1)) not in coordinates3:
                        try:
                            F2[x - 2][y - 1] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x - 2][y + 1] == "O" or int('%i%i' % (x-2, y+1)) not in coordinates3:
                        try:
                            F2[x - 2][y + 1] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
        except IndexError:
            pass

        try:
            if F2[x][y] == "X" and F2[x + 1][y] == "X" and F2[x + 2][
                y] == "X":
                try:
                    if F2[x + 3][y] == "O" or int('%i%i' % (x+3, y)) not in coordinates3:
                        try:
                            F2[x + 3][y] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x + 3][y - 1] == "O" or int('%i%i' % (x+3, y-1)) not in coordinates3:
                        try:
                            F2[x + 3][y - 1] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x + 3][y + 1] == "O" or int('%i%i' % (x+3, y+1)) not in coordinates3:
                        try:
                            F2[x + 3][y + 1] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x + 2][y - 1] == "O" or int('%i%i' % (x+2, y-1)) not in coordinates3:
                        try:
                            F2[x + 2][y - 1] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x + 2][y + 1] == "O" or int('%i%i' % (x+2, y+1)) not in coordinates3:
                        try:
                            F2[x + 2][y + 1] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
        except IndexError:
            pass

        try:
            if F2[x][y] == "X" and F2[x - 1][y] == "X" and F2[x + 1][
                y] == "X":
                try:
                    if F2[x - 2][y] == "O" or int('%i%i' % (x-2, y)) not in coordinates3:
                        try:
                            F2[x - 2][y] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x - 2][y - 1] == "O" or int('%i%i' % (x-2, y-1)) not in coordinates3:
                        try:
                            F2[x - 2][y - 1] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x - 2][y + 1] == "O" or int('%i%i' % (x-2, y+1)) not in coordinates3:
                        try:
                            F2[x - 2][y + 1] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x + 2][y] == "O" or int('%i%i' % (x+2, y)) not in coordinates3:
                        try:
                            F2[x + 2][y] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x + 2][y - 1] == "O" or int('%i%i' % (x+2, y-1)) not in coordinates3:
                        try:
                            F2[x + 2][y - 1] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x + 2][y + 1] == "O" or int('%i%i' % (x+2, y+1)) not in coordinates3:
                        try:
                            F2[x + 2][y + 1] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
        except IndexError:
            pass

        try:
            if F2[x][y] == "X" and F2[x][y + 1] == "X" and F2[x][
                y + 2] == "X":
                try:
                    if F2[x][y + 3] == "O" or int('%i%i' % (x, y+3)) not in coordinates3:
                        try:
                            F2[x][y + 3] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x - 1][y + 3] == "O" or int('%i%i' % (x-1, y+3)) not in coordinates3:
                        try:
                            F2[x - 1][y + 3] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x + 1][y + 3] == "O" or int('%i%i' % (x+1, y+3)) not in coordinates3:
                        try:
                            F2[x + 1][y + 3] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x - 1][y + 2] == "O" or int('%i%i' % (x-1, y+2)) not in coordinates3:
                        try:
                            F2[x - 1][y + 2] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x + 1][y + 2] == "O" or int('%i%i' % (x+1, y+2)) not in coordinates3:
                        try:
                            F2[x + 1][y + 2] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
        except IndexError:
            pass

        try:
            if F2[x][y] == "X" and F2[x][y - 1] == "X" and F2[x][
                y - 2] == "X":
                try:
                    if F2[x][y - 3] == "O" or int('%i%i' % (x, y-3)) not in coordinates3:
                        try:
                            F2[x][y - 3] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x - 1][y - 3] == "O" or int('%i%i' % (x-1, y-3)) not in coordinates3:
                        try:
                            F2[x - 1][y - 3] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x + 1][y - 3] == "O" or int('%i%i' % (x+1, y-3)) not in coordinates3:
                        try:
                            F2[x + 1][y - 3] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x - 1][y - 2] == "O" or int('%i%i' % (x-1, y-2)) not in coordinates3:
                        try:
                            F2[x - 1][y - 2] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x + 1][y - 2] == "O" or int('%i%i' % (x+1, y-2)) not in coordinates3:
                        try:
                            F2[x + 1][y - 2] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
        except IndexError:
            pass

        try:
            if F2[x][y] == "X" and F2[x][y - 1] == "X" and F2[x][
                y + 1] == "X":
                try:
                    if F2[x][y + 2] == "O" or int('%i%i' % (x, y+2)) not in coordinates3:
                        try:
                            F2[x][y + 2] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x - 1][y + 2] == "O" or int('%i%i' % (x-1, y+2)) not in coordinates3:
                        try:
                            F2[x - 1][y + 2] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x + 1][y + 2] == "O" or int('%i%i' % (x+1, y+2)) not in coordinates3:
                        try:
                            F2[x + 1][y + 2] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x][y - 2] == "O" or int('%i%i' % (x, y-2)) not in coordinates3:
                        try:
                            F2[x][y - 2] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x - 1][y - 2] == "O" or int('%i%i' % (x-1, y-2)) not in coordinates3:
                        try:
                            F2[x - 1][y - 2] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
                try:
                    if F2[x + 1][y - 2] == "O" or int('%i%i' % (x+1, y+2)) not in coordinates3:
                        try:
                            F2[x + 1][y - 2] = "-"
                        except IndexError:
                            pass
                except IndexError:
                    pass
        except IndexError:
            pass

        if x == 6 and y == 6:
            if F2[x - 1][y] != "■" and F2[x][y - 1] != "■":
                if F2[x - 1][y - 1] == "O":
                    try:
                        F2[x - 1][y - 1] = "-"
                        F3[x - 1][y - 1] = "-"
                    except IndexError:
                        pass
                if F2[x - 1][y] == "O":
                    try:
                        F2[x - 1][y] = "-"
                        F3[x - 1][y] = "-"
                    except IndexError:
                        pass
                if F2[x][y - 1] == "O":
                    try:
                        F2[x][y - 1] = "-"
                        F3[x][y - 1] = "-"
                    except IndexError:
                        pass
            else:
                pass
        elif x == 6:
            if F2[x][y + 1] != "■" and F2[x - 1][y] != "■" and F2[x][y - 1] != "■":
                if F2[x - 1][y - 1] == "O":
                    try:
                        F2[x - 1][y - 1] = "-"
                        F3[x - 1][y - 1] = "-"
                    except IndexError:
                        pass
                if F2[x - 1][y] == "O":
                    try:
                        F2[x - 1][y] = "-"
                        F3[x - 1][y] = "-"
                    except IndexError:
                        pass
                if F2[x][y - 1] == "O":
                    try:
                        F2[x][y - 1] = "-"
                        F3[x][y - 1] = "-"
                    except IndexError:
                        pass
                if F2[x][y + 1] == "O":
                    try:
                        F2[x][y + 1] = "-"
                        F3[x][y + 1] = "-"
                    except IndexError:
                        pass
                if F2[x - 1][y + 1] == "O":
                    try:
                        F2[x - 1][y + 1] = "-"
                        F3[x - 1][y + 1] = "-"
                    except IndexError:
                        pass
            else:
                pass
        elif y == 6:
            if F2[x + 1][y] != "■" and F2[x - 1][y] != "■" and F2[x][y - 1] != "■":
                if F2[x - 1][y - 1] == "O":
                    try:
                        F2[x - 1][y - 1] = "-"
                        F3[x - 1][y - 1] = "-"
                    except IndexError:
                        pass
                if F2[x - 1][y] == "O":
                    try:
                        F2[x - 1][y] = "-"
                        F3[x - 1][y] = "-"
                    except IndexError:
                        pass
                if F2[x][y - 1] == "O":
                    try:
                        F2[x][y - 1] = "-"
                        F3[x][y - 1] = "-"
                    except IndexError:
                        pass
                if F2[x + 1][y] == "O":
                    try:
                        F2[x + 1][y] = "-"
                        F3[x + 1][y] = "-"
                    except IndexError:
                        pass
                if F2[x + 1][y - 1] == "O":
                    try:
                        F2[x + 1][y - 1] = "-"
                        F3[x + 1][y - 1] = "-"
                    except IndexError:
                        pass
            else:
                pass
        elif F2[x + 1][y] != "■" and F2[x - 1][y] != "■" and F2[x][y + 1] != "■" and F2[x][y - 1] != "■":
            if F2[x + 1][y] == "O":
                try:
                    F2[x + 1][y] = "-"
                    F3[x + 1][y] = "-"
                except IndexError:
                    pass
            if F2[x + 1][y + 1] == "O":
                try:
                    F2[x + 1][y + 1] = "-"
                    F3[x + 1][y + 1] = "-"
                except IndexError:
                    pass
            if F2[x + 1][y - 1] == "O":
                try:
                    F2[x + 1][y - 1] = "-"
                    F3[x + 1][y - 1] = "-"
                except IndexError:
                    pass
            if F2[x - 1][y] == "O":
                try:
                    F2[x - 1][y] = "-"
                    F3[x - 1][y] = "-"
                except IndexError:
                    pass
            if F2[x - 1][y + 1] == "O":
                try:
                    F2[x - 1][y + 1] = "-"
                    F3[x - 1][y + 1] = "-"
                except IndexError:
                    pass
            if F2[x - 1][y - 1] == "O":
                try:
                    F2[x - 1][y - 1] = "-"
                    F3[x - 1][y - 1] = "-"
                except IndexError:
                    pass
            if F2[x][y + 1] == "O":
                try:
                    F2[x][y + 1] = "-"
                    F3[x][y + 1] = "-"
                except IndexError:
                    pass
            if F2[x][y - 1] == "O":
                try:
                    F2[x][y - 1] = "-"
                    F3[x][y - 1] = "-"
                except IndexError:
                    pass
    if F2[x][y] == "O" or F2[x][y] == "-":
        F2[x][y] = "T"
        F3[x][y] = "T"
        print("Мимо!")

    # вывод поля

    print("\nПоле компьютера:\n")
    for line in F3:
        print ('  '.join(map(str, line)))
    print("\n")

    def skip():
        input("Нажмите Enter, чтобы продолжить.")

    try:
        skip()
    except KeyboardInterrupt:
        skip()
    except ValueError:
        skip()

    # ход компьютера
    print("Ход компьютера.")

    # Попытка добить подбитый корабль
    if miss is True:
        targets.remove(hit)
        try:
            hit = random.choice(targets)
        except IndexError:
            hit = random.choice(coordinates2)
        st_str = repr(hit)
        last_digit_str = st_str[-1]
        last_d_hit = int(last_digit_str)
        first_d_hit = hit // 10
        coordinates2.remove(hit)
    elif F4[first_d_hit][last_d_hit] == "X":
        if first_d_hit == 6 and last_d_hit == 6:
            if F4[first_d_hit - 1][last_d_hit] != "-" and F4[first_d_hit][last_d_hit - 1] != "-":
                targets = []
                if 65 in coordinates2:
                    targets.append(65)
                else:
                    pass
                if 56 in coordinates2:
                    targets.append(56)
                else:
                    pass
                try:
                    hit = random.choice(targets)
                except IndexError:
                    hit = random.choice(coordinates2)
                st_str = repr(hit)
                last_digit_str = st_str[-1]
                last_d_hit = int(last_digit_str)
                first_d_hit = hit // 10
                coordinates2.remove(hit)
            else:
                hit = random.choice(coordinates2)
                st_str = repr(hit)
                last_digit_str = st_str[-1]
                last_d_hit = int(last_digit_str)
                first_d_hit = hit // 10
                coordinates2.remove(hit)
        elif first_d_hit == 6:
            if F4[first_d_hit][last_d_hit + 1] != "-" and F4[first_d_hit - 1][last_d_hit] != "-" and F4[first_d_hit][
                last_d_hit - 1] != "-":
                tx1 = first_d_hit
                ty1 = last_d_hit + 1
                tx2 = first_d_hit - 1
                ty2 = last_d_hit
                tx3 = first_d_hit
                ty3 = last_d_hit - 1
                t1 = [tx1, ty1]
                t2 = [tx2, ty2]
                t3 = [tx3, ty3]
                tar1 = "".join(map(str, t1))
                tar2 = "".join(map(str, t2))
                tar3 = "".join(map(str, t3))
                target1 = int(tar1)
                target2 = int(tar2)
                target3 = int(tar3)
                targets = []
                if target1 in coordinates2:
                    targets.append(target1)
                else:
                    pass
                if target2 in coordinates2:
                    targets.append(target2)
                else:
                    pass
                if target3 in coordinates2:
                    targets.append(target3)
                else:
                    pass
                try:
                    hit = random.choice(targets)
                except IndexError:
                    hit = random.choice(coordinates2)
                st_str = repr(hit)
                last_digit_str = st_str[-1]
                last_d_hit = int(last_digit_str)
                first_d_hit = hit // 10
                coordinates2.remove(hit)
            else:
                hit = random.choice(coordinates2)
                st_str = repr(hit)
                last_digit_str = st_str[-1]
                last_d_hit = int(last_digit_str)
                first_d_hit = hit // 10
                coordinates2.remove(hit)
        elif last_d_hit == 6:
            if F4[first_d_hit + 1][last_d_hit] != "-" and F4[first_d_hit - 1][last_d_hit] != "-" and F4[first_d_hit][
                last_d_hit - 1] != "-":
                tx1 = first_d_hit + 1
                ty1 = last_d_hit
                tx2 = first_d_hit - 1
                ty2 = last_d_hit
                tx3 = first_d_hit
                ty3 = last_d_hit - 1
                t1 = [tx1, ty1]
                t2 = [tx2, ty2]
                t3 = [tx3, ty3]
                tar1 = "".join(map(str, t1))
                tar2 = "".join(map(str, t2))
                tar3 = "".join(map(str, t3))
                target1 = int(tar1)
                target2 = int(tar2)
                target3 = int(tar3)
                targets = []
                if target1 in coordinates2:
                    targets.append(target1)
                else:
                    pass
                if target2 in coordinates2:
                    targets.append(target2)
                else:
                    pass
                if target3 in coordinates2:
                    targets.append(target3)
                else:
                    pass
                try:
                    hit = random.choice(targets)
                except IndexError:
                    hit = random.choice(coordinates2)
                st_str = repr(hit)
                last_digit_str = st_str[-1]
                last_d_hit = int(last_digit_str)
                first_d_hit = hit // 10
                coordinates2.remove(hit)
            else:
                hit = random.choice(coordinates2)
                st_str = repr(hit)
                last_digit_str = st_str[-1]
                last_d_hit = int(last_digit_str)
                first_d_hit = hit // 10
                coordinates2.remove(hit)
        elif F4[first_d_hit + 1][last_d_hit] != "-" and F4[first_d_hit - 1][last_d_hit] != "-" and F4[first_d_hit][
            last_d_hit + 1] != "-" and F4[first_d_hit][last_d_hit - 1] != "-":
            tx1 = first_d_hit + 1
            ty1 = last_d_hit
            tx2 = first_d_hit - 1
            ty2 = last_d_hit
            tx3 = first_d_hit
            ty3 = last_d_hit - 1
            tx4 = first_d_hit
            ty4 = last_d_hit + 1
            t1 = [tx1, ty1]
            t2 = [tx2, ty2]
            t3 = [tx3, ty3]
            t4 = [tx4, ty4]
            tar1 = "".join(map(str, t1))
            tar2 = "".join(map(str, t2))
            tar3 = "".join(map(str, t3))
            tar4 = "".join(map(str, t4))
            target1 = int(tar1)
            target2 = int(tar2)
            target3 = int(tar3)
            target4 = int(tar4)
            targets = []
            if target1 in coordinates2:
                targets.append(target1)
            else:
                pass
            if target2 in coordinates2:
                targets.append(target2)
            else:
                pass
            if target3 in coordinates2:
                targets.append(target3)
            else:
                pass
            if target4 in coordinates2:
                targets.append(target4)
            try:
                hit = random.choice(targets)
            except IndexError:
                hit = random.choice(coordinates2)
            st_str = repr(hit)
            last_digit_str = st_str[-1]
            last_d_hit = int(last_digit_str)
            first_d_hit = hit // 10
            coordinates2.remove(hit)
        else:
            hit = random.choice(coordinates2)
            st_str = repr(hit)
            last_digit_str = st_str[-1]
            last_d_hit = int(last_digit_str)
            first_d_hit = hit // 10
            coordinates2.remove(hit)

    else:
        hit = random.choice(coordinates2)
        st_str = repr(hit)
        last_digit_str = st_str[-1]
        last_d_hit = int(last_digit_str)
        first_d_hit = hit // 10
        coordinates2.remove(hit)

    print(first_d_hit, last_d_hit)

# Проверка попадания
    if F4[first_d_hit][last_d_hit] == "■":
        F4[first_d_hit][last_d_hit] = "X"
        print("Прямо в цель!")
        targets = []
        miss = False
        m+=1
        if m == 12:
            print("Вас победил компьютер!")
            print("\nПоле игрока:\n")
            for line in F4:
                print('  '.join(map(str, line)))
            break

# Выделение и удаление соседних клеток
        try:
            if F4[first_d_hit][last_d_hit] == "X" and F4[first_d_hit - 1][last_d_hit] == "X":
                try:
                    if F4[first_d_hit - 2][last_d_hit] == "O" or int('%i%i' % (first_d_hit - 2, last_d_hit)) not in coordinates3:
                        try:
                            F4[first_d_hit - 2][last_d_hit] = "-"
                            num = int('%i%i' % (first_d_hit - 2, last_d_hit))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit - 2][last_d_hit - 1] == "O" or int('%i%i' % (first_d_hit - 2, last_d_hit-1)) not in coordinates3:
                        try:
                            F4[first_d_hit - 2][last_d_hit - 1] = "-"
                            num = int('%i%i' % (first_d_hit - 2, last_d_hit - 1))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit - 2][last_d_hit + 1] == "O" or int('%i%i' % (first_d_hit - 2, last_d_hit+1)) not in coordinates3:
                        try:
                            F4[first_d_hit - 2][last_d_hit + 1] = "-"
                            num = int('%i%i' % (first_d_hit - 2, last_d_hit + 1))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
        except IndexError:
            pass

        try:
            if F4[first_d_hit][last_d_hit] == "X" and F4[first_d_hit + 1][last_d_hit] == "X":
                try:
                    if F4[first_d_hit + 2][last_d_hit] == "O" or int('%i%i' % (first_d_hit + 2, last_d_hit)) not in coordinates3:
                        try:
                            F4[first_d_hit + 2][last_d_hit] = "-"
                            num = int('%i%i' % (first_d_hit + 2, last_d_hit))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit + 2][last_d_hit - 1] == "O" or int('%i%i' % (first_d_hit + 2, last_d_hit-1)) not in coordinates3:
                        try:
                            F4[first_d_hit + 2][last_d_hit - 1] = "-"
                            num = int('%i%i' % (first_d_hit + 2, last_d_hit - 1))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit + 2][last_d_hit + 1] == "O" or int('%i%i' % (first_d_hit + 2, last_d_hit+1)) not in coordinates3:
                        try:
                            F4[first_d_hit + 2][last_d_hit + 1] = "-"
                            num = int('%i%i' % (first_d_hit + 2, last_d_hit + 1))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
        except IndexError:
            pass

        try:
            if F4[first_d_hit][last_d_hit] == "X" and F4[first_d_hit][last_d_hit + 1] == "X":
                try:
                    if F4[first_d_hit][last_d_hit + 2] == "O" or int('%i%i' % (first_d_hit, last_d_hit+2)) not in coordinates3:
                        try:
                            F4[first_d_hit][last_d_hit + 2] = "-"
                            num = int('%i%i' % (first_d_hit, last_d_hit + 2))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit - 1][last_d_hit + 2] == "O" or int('%i%i' % (first_d_hit-1, last_d_hit+2)) not in coordinates3:
                        try:
                            F4[first_d_hit - 1][last_d_hit + 2] = "-"
                            num = int('%i%i' % (first_d_hit - 1, last_d_hit + 2))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit + 1][last_d_hit + 2] == "O" or int('%i%i' % (first_d_hit+1, last_d_hit+2)) not in coordinates3:
                        try:
                            F4[first_d_hit + 1][last_d_hit + 2] = "-"
                            num = int('%i%i' % (first_d_hit + 1, last_d_hit + 2))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
        except IndexError:
            pass

        try:
            if F4[first_d_hit][last_d_hit] == "X" and F4[first_d_hit][last_d_hit - 1] == "X":
                try:
                    if F4[first_d_hit][last_d_hit - 2] == "O" or int('%i%i' % (first_d_hit, last_d_hit-2)) not in coordinates3:
                        try:
                            F4[first_d_hit][last_d_hit - 2] = "-"
                            num = int('%i%i' % (first_d_hit, last_d_hit - 2))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit - 1][last_d_hit - 2] == "O" or int('%i%i' % (first_d_hit-1, last_d_hit-2)) not in coordinates3:
                        try:
                            F4[first_d_hit - 1][last_d_hit - 2] = "-"
                            num = int('%i%i' % (first_d_hit - 1, last_d_hit - 2))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit + 1][last_d_hit - 2] == "O" or int('%i%i' % (first_d_hit+1, last_d_hit-2)) not in coordinates3:
                        try:
                            F4[first_d_hit + 1][last_d_hit - 2] = "-"
                            num = int('%i%i' % (first_d_hit + 1, last_d_hit - 2))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
        except IndexError:
            pass

        try:
            if F4[first_d_hit][last_d_hit] == "X" and F4[first_d_hit - 1][last_d_hit] == "X" and F4[first_d_hit - 2][
                last_d_hit] == "X":
                try:
                    if F4[first_d_hit - 3][last_d_hit] == "O" or int('%i%i' % (first_d_hit - 3, last_d_hit)) not in coordinates3:
                        try:
                            F4[first_d_hit - 3][last_d_hit] = "-"
                            num = int('%i%i' % (first_d_hit - 3, last_d_hit))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit - 3][last_d_hit - 1] == "O" or int('%i%i' % (first_d_hit - 3, last_d_hit-1)) not in coordinates3:
                        try:
                            F4[first_d_hit - 3][last_d_hit - 1] = "-"
                            num = int('%i%i' % (first_d_hit - 3, last_d_hit - 1))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit - 3][last_d_hit + 1] == "O" or int('%i%i' % (first_d_hit - 3, last_d_hit+1)) not in coordinates3:
                        try:
                            F4[first_d_hit - 3][last_d_hit + 1] = "-"
                            num = int('%i%i' % (first_d_hit - 3, last_d_hit + 1))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit - 2][last_d_hit - 1] == "O" or int('%i%i' % (first_d_hit - 2, last_d_hit-1)) not in coordinates3:
                        try:
                            F4[first_d_hit - 2][last_d_hit - 1] = "-"
                            num = int('%i%i' % (first_d_hit - 2, last_d_hit - 1))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit - 2][last_d_hit + 1] == "O" or int('%i%i' % (first_d_hit - 2, last_d_hit+1)) not in coordinates3:
                        try:
                            F4[first_d_hit - 2][last_d_hit + 1] = "-"
                            num = int('%i%i' % (first_d_hit - 2, last_d_hit + 1))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
        except IndexError:
            pass

        try:
            if F4[first_d_hit][last_d_hit] == "X" and F4[first_d_hit + 1][last_d_hit] == "X" and F4[first_d_hit + 2][
                last_d_hit] == "X":
                try:
                    if F4[first_d_hit + 3][last_d_hit] == "O" or int('%i%i' % (first_d_hit + 3, last_d_hit)) not in coordinates3:
                        try:
                            F4[first_d_hit + 3][last_d_hit] = "-"
                            num = int('%i%i' % (first_d_hit + 3, last_d_hit))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit + 3][last_d_hit - 1] == "O" or int('%i%i' % (first_d_hit + 3, last_d_hit-1)) not in coordinates3:
                        try:
                            F4[first_d_hit + 3][last_d_hit - 1] = "-"
                            num = int('%i%i' % (first_d_hit + 3, last_d_hit - 1))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit + 3][last_d_hit + 1] == "O" or int('%i%i' % (first_d_hit + 3, last_d_hit+1)) not in coordinates3:
                        try:
                            F4[first_d_hit + 3][last_d_hit + 1] = "-"
                            num = int('%i%i' % (first_d_hit + 3, last_d_hit + 1))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit + 2][last_d_hit - 1] == "O" or int('%i%i' % (first_d_hit +2, last_d_hit-1)) not in coordinates3:
                        try:
                            F4[first_d_hit + 2][last_d_hit - 1] = "-"
                            num = int('%i%i' % (first_d_hit + 2, last_d_hit - 1))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit + 2][last_d_hit + 1] == "O" or int('%i%i' % (first_d_hit +2, last_d_hit+1)) not in coordinates3:
                        try:
                            F4[first_d_hit + 2][last_d_hit + 1] = "-"
                            num = int('%i%i' % (first_d_hit + 2, last_d_hit + 1))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
        except IndexError:
            pass

        try:
            if F4[first_d_hit][last_d_hit] == "X" and F4[first_d_hit - 1][last_d_hit] == "X" and F4[first_d_hit + 1][
                last_d_hit] == "X":
                try:
                    if F4[first_d_hit - 2][last_d_hit] == "O" or int('%i%i' % (first_d_hit - 2, last_d_hit)) not in coordinates3:
                        try:
                            F4[first_d_hit - 2][last_d_hit] = "-"
                            num = int('%i%i' % (first_d_hit - 2, last_d_hit))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit - 2][last_d_hit - 1] == "O" or int('%i%i' % (first_d_hit - 2, last_d_hit-1)) not in coordinates3:
                        try:
                            F4[first_d_hit - 2][last_d_hit - 1] = "-"
                            num = int('%i%i' % (first_d_hit - 2, last_d_hit - 1))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit - 2][last_d_hit + 1] == "O" or int('%i%i' % (first_d_hit - 2, last_d_hit+2)) not in coordinates3:
                        try:
                            F4[first_d_hit - 2][last_d_hit + 1] = "-"
                            num = int('%i%i' % (first_d_hit - 2, last_d_hit + 1))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit + 2][last_d_hit] == "O" or int('%i%i' % (first_d_hit +2, last_d_hit)) not in coordinates3:
                        try:
                            F4[first_d_hit + 2][last_d_hit] = "-"
                            num = int('%i%i' % (first_d_hit + 2, last_d_hit))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit + 2][last_d_hit - 1] == "O" or int('%i%i' % (first_d_hit +2, last_d_hit-1)) not in coordinates3:
                        try:
                            F4[first_d_hit + 2][last_d_hit - 1] = "-"
                            num = int('%i%i' % (first_d_hit + 2, last_d_hit - 1))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit + 2][last_d_hit + 1] == "O" or int('%i%i' % (first_d_hit +2, last_d_hit+1)) not in coordinates3:
                        try:
                            F4[first_d_hit + 2][last_d_hit + 1] = "-"
                            num = int('%i%i' % (first_d_hit + 2, last_d_hit + 1))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
        except IndexError:
            pass

        try:
            if F4[first_d_hit][last_d_hit] == "X" and F4[first_d_hit][last_d_hit + 1] == "X" and F4[first_d_hit][
                last_d_hit + 2] == "X":
                try:
                    if F4[first_d_hit][last_d_hit + 3] == "O" or int('%i%i' % (first_d_hit, last_d_hit+3)) not in coordinates3:
                        try:
                            F4[first_d_hit][last_d_hit + 3] = "-"
                            num = int('%i%i' % (first_d_hit, last_d_hit + 3))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit - 1][last_d_hit + 3] == "O" or int('%i%i' % (first_d_hit-1, last_d_hit+3)) not in coordinates3:
                        try:
                            F4[first_d_hit - 1][last_d_hit + 3] = "-"
                            num = int('%i%i' % (first_d_hit - 1, last_d_hit + 3))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit + 1][last_d_hit + 3] == "O" or int('%i%i' % (first_d_hit+1, last_d_hit+3)) not in coordinates3:
                        try:
                            F4[first_d_hit + 1][last_d_hit + 3] = "-"
                            num = int('%i%i' % (first_d_hit + 1, last_d_hit + 3))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit - 1][last_d_hit + 2] == "O" or int('%i%i' % (first_d_hit-1, last_d_hit+2)) not in coordinates3:
                        try:
                            F4[first_d_hit - 1][last_d_hit + 2] = "-"
                            num = int('%i%i' % (first_d_hit - 1, last_d_hit + 2))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit + 1][last_d_hit + 2] == "O" or int('%i%i' % (first_d_hit+1, last_d_hit+2)) not in coordinates3:
                        try:
                            F4[first_d_hit + 1][last_d_hit + 2] = "-"
                            num = int('%i%i' % (first_d_hit + 1, last_d_hit + 2))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
        except IndexError:
            pass

        try:
            if F4[first_d_hit][last_d_hit] == "X" and F4[first_d_hit][last_d_hit - 1] == "X" and F4[first_d_hit][
                last_d_hit - 2] == "X":
                try:
                    if F4[first_d_hit][last_d_hit - 3] == "O" or int('%i%i' % (first_d_hit, last_d_hit-3)) not in coordinates3:
                        try:
                            F4[first_d_hit][last_d_hit - 3] = "-"
                            num = int('%i%i' % (first_d_hit, last_d_hit - 3))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit - 1][last_d_hit - 3] == "O" or int('%i%i' % (first_d_hit-1, last_d_hit-3)) not in coordinates3:
                        try:
                            F4[first_d_hit - 1][last_d_hit - 3] = "-"
                            num = int('%i%i' % (first_d_hit - 1, last_d_hit - 3))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit + 1][last_d_hit - 3] == "O" or int('%i%i' % (first_d_hit+1, last_d_hit-3)) not in coordinates3:
                        try:
                            F4[first_d_hit + 1][last_d_hit - 3] = "-"
                            num = int('%i%i' % (first_d_hit + 1, last_d_hit - 3))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit - 1][last_d_hit - 2] == "O" or int('%i%i' % (first_d_hit-1, last_d_hit-2)) not in coordinates3:
                        try:
                            F4[first_d_hit - 1][last_d_hit - 2] = "-"
                            num = int('%i%i' % (first_d_hit - 1, last_d_hit - 2))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit + 1][last_d_hit - 2] == "O" or int('%i%i' % (first_d_hit+1, last_d_hit-2)) not in coordinates3:
                        try:
                            F4[first_d_hit + 1][last_d_hit - 2] = "-"
                            num = int('%i%i' % (first_d_hit + 1, last_d_hit - 2))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
        except IndexError:
            pass

        try:
            if F4[first_d_hit][last_d_hit] == "X" and F4[first_d_hit][last_d_hit - 1] == "X" and F4[first_d_hit][
                last_d_hit + 1] == "X":
                try:
                    if F4[first_d_hit][last_d_hit + 2] == "O" or int('%i%i' % (first_d_hit, last_d_hit+2)) not in coordinates3:
                        try:
                            F4[first_d_hit][last_d_hit + 2] = "-"
                            num = int('%i%i' % (first_d_hit, last_d_hit + 2))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit - 1][last_d_hit + 2] == "O" or int('%i%i' % (first_d_hit-1, last_d_hit+2)) not in coordinates3:
                        try:
                            F4[first_d_hit - 1][last_d_hit + 2] = "-"
                            num = int('%i%i' % (first_d_hit - 1, last_d_hit + 2))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit + 1][last_d_hit + 2] == "O" or int('%i%i' % (first_d_hit+1, last_d_hit+2)) not in coordinates3:
                        try:
                            F4[first_d_hit + 1][last_d_hit + 2] = "-"
                            num = int('%i%i' % (first_d_hit + 1, last_d_hit + 2))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit][last_d_hit - 2] == "O" or int('%i%i' % (first_d_hit, last_d_hit-2)) not in coordinates3:
                        try:
                            F4[first_d_hit][last_d_hit - 2] = "-"
                            num = int('%i%i' % (first_d_hit, last_d_hit - 2))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit - 1][last_d_hit - 2] == "O" or int('%i%i' % (first_d_hit-1, last_d_hit-2)) not in coordinates3:
                        try:
                            F4[first_d_hit - 1][last_d_hit - 2] = "-"
                            num = int('%i%i' % (first_d_hit - 1, last_d_hit - 2))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
                try:
                    if F4[first_d_hit + 1][last_d_hit - 2] == "O" or int('%i%i' % (first_d_hit+1, last_d_hit-2)) not in coordinates3:
                        try:
                            F4[first_d_hit + 1][last_d_hit - 2] = "-"
                            num = int('%i%i' % (first_d_hit + 1, last_d_hit - 2))
                            coordinates2.remove(num)
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                except IndexError:
                    pass
                except ValueError:
                    pass
        except IndexError:
            pass

        if first_d_hit == 6 and last_d_hit == 6:
            if F4[first_d_hit - 1][last_d_hit] != "■" and F4[first_d_hit][last_d_hit - 1] != "■":
                if F4[first_d_hit - 1][last_d_hit - 1] == "O":
                    try:
                        F4[first_d_hit - 1][last_d_hit - 1] = "-"
                        num = int('%i%i' % (first_d_hit - 1, last_d_hit - 1))
                        coordinates2.remove(num)
                    except IndexError:
                        pass
                if F4[first_d_hit - 1][last_d_hit] == "O":
                    try:
                        F4[first_d_hit - 1][last_d_hit] = "-"
                        num = int('%i%i' % (first_d_hit - 1, last_d_hit))
                        coordinates2.remove(num)
                    except IndexError:
                        pass
                if F4[first_d_hit][last_d_hit - 1] == "O":
                    try:
                        F4[first_d_hit][last_d_hit - 1] = "-"
                        num = int('%i%i' % (first_d_hit, last_d_hit - 1))
                        coordinates2.remove(num)
                    except IndexError:
                        pass
                else:
                    pass
        elif first_d_hit == 6:
            if F4[first_d_hit][last_d_hit + 1] != "■" and F4[first_d_hit - 1][last_d_hit] != "■" and F4[first_d_hit][last_d_hit - 1] != "■":
                if F4[first_d_hit - 1][last_d_hit - 1] == "O":
                    try:
                        F4[first_d_hit - 1][last_d_hit - 1] = "-"
                        num = int('%i%i' % (first_d_hit - 1, last_d_hit - 1))
                        coordinates2.remove(num)
                    except IndexError:
                        pass
                if F4[first_d_hit - 1][last_d_hit] == "O":
                    try:
                        F4[first_d_hit - 1][last_d_hit] = "-"
                        num = int('%i%i' % (first_d_hit - 1, last_d_hit))
                        coordinates2.remove(num)
                    except IndexError:
                        pass
                if F4[first_d_hit][last_d_hit - 1] == "O":
                    try:
                        F4[first_d_hit][last_d_hit - 1] = "-"
                        num = int('%i%i' % (first_d_hit, last_d_hit - 1))
                        coordinates2.remove(num)
                    except IndexError:
                        pass
                if F4[first_d_hit][last_d_hit + 1] == "O":
                    try:
                        F4[first_d_hit][last_d_hit + 1] = "-"
                        num = int('%i%i' % (first_d_hit, last_d_hit + 1))
                        coordinates2.remove(num)
                    except IndexError:
                        pass
                if F4[first_d_hit - 1][last_d_hit + 1] == "O":
                    try:
                        F4[first_d_hit - 1][last_d_hit + 1] = "-"
                        num = int('%i%i' % (first_d_hit - 1, last_d_hit + 1))
                        coordinates2.remove(num)
                    except IndexError:
                        pass
            else:
                pass
        elif last_d_hit == 6:
            if F4[first_d_hit + 1][last_d_hit] != "■" and F4[first_d_hit - 1][last_d_hit] != "■" and F4[first_d_hit][last_d_hit - 1] != "■":
                if F4[first_d_hit - 1][last_d_hit - 1] == "O":
                    try:
                        F4[first_d_hit - 1][last_d_hit - 1] = "-"
                        num = int('%i%i' % (first_d_hit - 1, last_d_hit - 1))
                        coordinates2.remove(num)
                    except IndexError:
                        pass
                if F4[first_d_hit - 1][last_d_hit] == "O":
                    try:
                        F4[first_d_hit - 1][last_d_hit] = "-"
                        num = int('%i%i' % (first_d_hit - 1, last_d_hit))
                        coordinates2.remove(num)
                    except IndexError:
                        pass
                if F4[first_d_hit][last_d_hit - 1] == "O":
                    try:
                        F4[first_d_hit][last_d_hit - 1] = "-"
                        num = int('%i%i' % (first_d_hit, last_d_hit - 1))
                        coordinates2.remove(num)
                    except IndexError:
                        pass
                if F4[first_d_hit + 1][last_d_hit] == "O":
                    try:
                        F4[first_d_hit + 1][last_d_hit] = "-"
                        num = int('%i%i' % (first_d_hit + 1, last_d_hit))
                        coordinates2.remove(num)
                    except IndexError:
                        pass
                if F4[first_d_hit + 1][last_d_hit - 1] == "O":
                    try:
                        F4[first_d_hit + 1][last_d_hit - 1] = "-"
                        num = int('%i%i' % (first_d_hit + 1, last_d_hit - 1))
                        coordinates2.remove(num)
                    except IndexError:
                        pass
            else:
                pass
        elif F4[first_d_hit + 1][last_d_hit] != "■" and F4[first_d_hit - 1][last_d_hit] != "■" and F4[first_d_hit][last_d_hit + 1] != "■" and F4[first_d_hit][last_d_hit - 1] != "■":
            if F4[first_d_hit + 1][last_d_hit] == "O":
                try:
                    F4[first_d_hit + 1][last_d_hit] = "-"
                    num = int('%i%i' % (first_d_hit + 1, last_d_hit))
                    coordinates2.remove(num)
                except IndexError:
                    pass
            if F4[first_d_hit + 1][last_d_hit + 1] == "O":
                try:
                    F4[first_d_hit + 1][last_d_hit + 1] = "-"
                    num = int('%i%i' % (first_d_hit + 1, last_d_hit + 1))
                    coordinates2.remove(num)
                except IndexError:
                    pass
            if F4[first_d_hit + 1][last_d_hit - 1] == "O":
                try:
                    F4[first_d_hit + 1][last_d_hit - 1] = "-"
                    num = int('%i%i' % (first_d_hit + 1, last_d_hit - 1))
                    coordinates2.remove(num)
                except IndexError:
                    pass
            if F4[first_d_hit - 1][last_d_hit] == "O":
                try:
                    F4[first_d_hit - 1][last_d_hit] = "-"
                    num = int('%i%i' % (first_d_hit - 1, last_d_hit))
                    coordinates2.remove(num)
                except IndexError:
                    pass
            if F4[first_d_hit - 1][last_d_hit + 1] == "O":
                try:
                    F4[first_d_hit - 1][last_d_hit + 1] = "-"
                    num = int('%i%i' % (first_d_hit - 1, last_d_hit + 1))
                    coordinates2.remove(num)
                except IndexError:
                    pass
            if F4[first_d_hit - 1][last_d_hit - 1] == "O":
                try:
                    F4[first_d_hit - 1][last_d_hit - 1] = "-"
                    num = int('%i%i' % (first_d_hit - 1, last_d_hit - 1))
                    coordinates2.remove(num)
                except IndexError:
                    pass
            if F4[first_d_hit][last_d_hit + 1] == "O":
                try:
                    F4[first_d_hit][last_d_hit + 1] = "-"
                    num = int('%i%i' % (first_d_hit, last_d_hit + 1))
                    coordinates2.remove(num)
                except IndexError:
                    pass
            if F4[first_d_hit][last_d_hit - 1] == "O":
                try:
                    F4[first_d_hit][last_d_hit - 1] = "-"
                    num = int('%i%i' % (first_d_hit, last_d_hit - 1))
                    coordinates2.remove(num)
                except IndexError:
                    pass

    if F4[first_d_hit][last_d_hit] == "O":
        F4[first_d_hit][last_d_hit] = "T"
        print("Мимо!")
        if targets:
            miss = True


    # вывод поля

    print("\nПоле игрока:\n")
    for line in F4:
        print ('  '.join(map(str, line)))
    print("\n")