print("Даниленко Кірілл Артурович \nЛабораторна робота №1 \nВаріант 2 \nПорівняння відстані точок від початку координат \n")

def myfunc():
    try:
        coord_xa = float(input("Введите координату x для А: "))
        coord_ya = float(input("Введите координату y для A: "))
        coord_xb = float(input("Введите координату x для B: "))
        coord_yb = float(input("Введите координату y для B: "))
    except:
        print("Введите числовое значение!")
        myfunc()

    sumA = abs(coord_xa) + abs(coord_ya)
    sumB = abs(coord_xb) + abs(coord_yb)

    if sumA == sumB:
        print("Точки находятся на одном отдалении")
    else:
        if sumA < sumB:
            print("Точка А ближе к началу координат")
        else:
            print("Точка B ближе к началу координат")

    c = input("Продолжить тестирование программы? Y/N")
    if c == 'Y' or c == 'y':
        myfunc()
    else:
        return ()

myfunc()