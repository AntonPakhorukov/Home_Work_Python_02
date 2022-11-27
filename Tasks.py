# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# 4. Реализуйте алгоритм перемешивания списка.

try:
    task = int(input('Введите номер задачи: '))
except ValueError:
    print('Не корректный ввод')
    raise SystemExit
match task:
    case 1:
        try:
            number = float(input('Введите число: '))
        except ValueError:
            print('не корректный ввод')
            raise SystemExit
        if number < 0:
            number *= (-1)
        value = list(str(number))
        print(value)
        print(type(value))
        value.remove('.')
        print(value)
        result = 0
        for i in value:
            result += int(i)
        print(result)   
    case 2:
        try:
            number = int(input('Введите число: '))
        except ValueError:
            print('Не корректный ввод')
            raise SystemExit
        if number < 0:
            number *= (-1)
        n = 1
        print('[ ', end='')
        for i in range(1, number):
            n *= i
            print(n, end=', ')
        print(n * (i + 1), end='')
        print(' ]')
    case 3:
        print('3')
    case 4:
        print('4')
    case _:
        print('Нет задачи с таким номером')