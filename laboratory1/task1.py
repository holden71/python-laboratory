print("Даниленко Кірілл Артурович \nЛабораторна робота №1 \nВаріант 2 \nОбчислення відсотку від числа \n")

def myfunc():
    try:
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))
        if a > 0 and b > 0:
            print("x = %.2f"  %((b / a) * 100))



            c = input("Продолжить тестирование программы? Y/N")
            if c == 'Y' or c == 'y':
                myfunc()
            else:
                return



        else:
            print("Введите положительные числа!")
            myfunc()
    except:
        print("Введите числовое значение!")
        myfunc()

myfunc()

