print("Даниленко Кірілл Артурович \nЛабораторна робота №1 \nВаріант 2 \nОбчислення виразу в залежності від значення \n")


def myfunc():
    try:
        x = float(input("Введите значение x: "))
    except:
        print("Введите числовое значение!")
        myfunc()

    if x >= 3 :

        print("x = %.4f" %(x**2 - 3*x +9))
        c = input("Продолжить тестирование программы? Y/N")
        if c == 'Y' or c == 'y':
            myfunc()
        else:
            return ()

    else:
        print("x = %.4f" %(1/(x**3-6)))
        c = input("Продолжить тестирование программы? Y/N")
        if c == 'Y' or c == 'y':
            myfunc()
        else:
            return ()


myfunc()