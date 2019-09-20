print("Даниленко Кірілл Артурович \nЛабораторна робота №1 \nВаріант 2 \nОбчислення відсотку від числа \n")

def myfunc():
    try:
        user_float_input_a = float(input("Введите число a: "))
        user_float_input_b = float(input("Введите число b: "))
        if user_float_input_a > 0 and user_float_input_b > 0:
            print("x = %.2f"  %((user_float_input_b / user_float_input_a) * 100))



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

