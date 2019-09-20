print("Даниленко Кірілл Артурович \nЛабораторна робота №1 \nВаріант 2 \nОбчислення виразу в залежності від значення \n")


def myfunc():
    try:
        user_input_x = float(input("Введите значение x: "))
    except:
        print("Введите числовое значение!")
        myfunc()

    if user_input_x >= 3 :

        print("x = %.4f" %(user_input_x**2 - 3*user_input_x +9))
        c = input("Продолжить тестирование программы? Y/N")
        if c == 'Y' or c == 'y':
            myfunc()
        else:
            return ()

    else:
        print("x = %.4f" %(1/(user_input_x**3-6)))
        c = input("Продолжить тестирование программы? Y/N")
        if c == 'Y' or c == 'y':
            myfunc()
        else:
            return ()


myfunc()