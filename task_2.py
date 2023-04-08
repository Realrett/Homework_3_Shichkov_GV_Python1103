# 2. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль (try except).

# Пример:
# Введите первое число: 10
# Введите второе число: 0
# Вы что? Пытаетесь делить на 0!

# Process finished with exit code 0

# Пример:
# Введите первое число: 10
# Введите второе число: 10
# 1.0

# Process finished with exit code 0

def calculator (number_1, number_2):
    try:
        division = number_1 / number_2
        return division
    except ZeroDivisionError:
        print('Вы что? Пытаетесь делить на 0!')
    except ValueError:
        print('Вводите только числа!')

print(calculator(int(input("Введите первое число: ")), int(input("Введите второе число: "))))

