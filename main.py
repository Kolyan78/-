'''
1. Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
В исходном списке минимум 2 элемента.
'''
def change(lst):
    l = len(lst)
    if l < 2:
        return "Ошибка - в списке меньше двух элементов"
    else:
        lst[0], lst[l - 1] = lst[l - 1], lst[0]
        return lst

list_ = list(range(10))
print(change(list_))