# խնդիր 1
'''
a = int(input("Input count of number in your list:\t"))
l = []
for i in range(a):
    l.append(int(input(f"Input your {i + 1} number:\t")))
print("your list is", l)
for x in range(1, len(l)):
    for y in range(x + 1):
        if l[x] < l[y]:
            l[x], l[y] = l[y], l[x]
print("in ascending order", l)
for x in range(1, len(l)):
    for y in range(x + 1):
        if l[x] > l[y]:
            l[x], l[y] = l[y], l[x]
print("in descending order", l)
'''
# խնդիր 2
'''
a = int(input("Input count of word in your list:\t"))
l = []
for i in range(a):
    l.append(str(input(f"Input your {i + 1} word:\t")))
print("Your words in list is", l)
words_length = [len(word) for word in l]
print("words length is", words_length)
'''
# խնդիր 3
'''
a = int(input("Input count of number in your list:\t"))
l = []
for i in range(a):
    l.append(int(input(f"Input your {i + 1} number:\t")))
print("Your list is", l)
list_square_root = [z ** 2 for z in l]
print("List square is", list_square_root)
'''
'''
# խնդիր 4
a = int(input("Input count of number in your list:\t"))
l = []
for i in range(a):
    l.append(int(input(f"Input your {i + 1} number:\t")))
print("Your list is", l)
square = lambda square1: [j ** 2 for j in square1]
squared_list = square(l)
print("Your squared list", squared_list)
'''
'''
# խնդիր 6
a = int(input("Input count of string:\t"))
l = []
for i in range(a):
    l.append(str(input(f"Input your {i + 1} string:\t")))
print("Your list is", l)
list_with_only_one_element = [x for x in l if len(x) <= 1]
print(list_with_only_one_element)
'''

import random


def even(num):
    if num % 2 == 0:
        return True
    else:
        return False


a = [random.randint(1, 10) for x in range(10)]
print(a)
b = [i for i in a if even(i)]
print(b)
print(len(b))