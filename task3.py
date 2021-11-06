'''
3. Требуется создать функцию list_sort(lst), которая сортирует список чисел по убыванию их абсолютного значения.
'''
import random
def list_sort(lst):
    return sorted([abs(x) for x in lst], reverse=True)

def gen_list(n, min, max):
    return [random.randint(min, max) for _ in range(n)]

a = (gen_list(10, -100, 100))
print(a)
print(list_sort(a))