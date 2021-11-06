'''
9. На вход функция more_than_five(lst) получает список из целых чисел.
Результатом работы функции должен стать новый список, в котором содержатся только те числа, которые больше 5 по модулю.
'''
import random

def more_than_five(lst):
    print(lst)
    b = [abs(x) for x in lst if abs(x) > 5]
    return b

def gen_list(num):
    a = [random.randint(-10, 10) for _ in list(range(num))]
    return a

a = gen_list(30)
print (more_than_five(a))