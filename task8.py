'''
8. Требуется определить индексы первого и последнего вхождения буквы в строке.
Для этого нужно написать функцию first_last(letter, st), включающую 2 параметра: letter – искомый символ, st – целевая строка.
В случае отсутствия буквы в строке, нужно вернуть кортеж (None, None), если же она есть, то кортеж будет состоять
из первого и последнего индекса этого символа.
'''

def first_last(letter, st):
    a = st.split(letter)
    first = len(a[0])
    last = len(st) - len(a[len(a) - 1]) - 1
    if last == -1:
        first, last = None, None
    b = (first, last)
    return b

print(first_last(" ", "Do you speak English or no?"))