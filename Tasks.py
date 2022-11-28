# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# - Для n = 4: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

# 4. Реализуйте алгоритм перемешивания списка.

# 5. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в фавйле file.txt
# в одно строке одно число.

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
        n = int(input())
        print('{', end='')
        for i in range(1, n):
            result = round((1 + 1 / i) ** i, 2)
            print(f'{i}: {result}, ', end='')
        print(f'{n}: {round((1 + 1 / n) ** n, 2)}', end='')
        print('}')
    case 4:
        import random
        try:
            variation = int(input('Введите способ решения (1 - ввод списка в одну строку, 2 - в ручную, 3 - без shuffle): '))
        except ValueError:
            print('Не корректный ввод')
            raise SystemExit
        match variation:
            case 1:
                array = list(input('Введите данные списка: '))
                print(array)
                random.shuffle(array)
                print(array)
            case 2:
                n = int(input('Введите длинну списка: '))
                array = list()
                for i in range(n):
                    array.append(input('Вводите данные списка: '))
                print(array)
                random.shuffle(array)
                print(array)
            case 3:
                n = int(input('Введите длинну списка: '))
                array = list()
                for i in range(n):
                    array.append(input('Вводите данные списка: '))
                print(array)
                for i in range(len(array)):
                    num = random.randrange(0, len(array))
                    temp = array[i]
                    array[i] = array[num]
                    array[num] = temp
                print(array)
    case 5:
        print('Задачка с файлом')     
    case _:
        print('Нет задачи с таким номером')