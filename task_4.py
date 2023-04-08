# 4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:**
# 1) используя функцию sort()
# 2) без функции sort()
def my_func(x, y, z):
    data_list = [x, y, z]
    data_list.sort()
    print(data_list[1] + data_list[2])
my_func(int(input('Введите первое число: ')),int(input('Введите второе число: ')), int(input('Введите третье число: ')))

# def my_func(x, y, z):
#     data_list = [x, y, z]
#     sort_list = []
#     max_number_1 = max(data_list)
#     sort_list.append(max_number_1)
#     data_list.remove(max_number_1)
#     max_number_2 = max(data_list)
#     sort_list.append(max_number_2)
#     print(sum(sort_list))
# my_func(int(input('Введите первое число: ')),int(input('Введите второе число: ')), int(input('Введите третье число: ')))