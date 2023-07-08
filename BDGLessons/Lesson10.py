'''
# Exercise 1
def perimeter_rectangle():
    length = float(input("Input the rectangle length:\t"))
    width = float(input("Input the rectangle width:\t"))

    perimeter = 2 * (length + width)
    return perimeter


perimeter = perimeter_rectangle()
print("Your rectangle  perimeter = ", perimeter)


# Exercise 2
def perimeter_square():
    side = float(input("Input the side of square:\t"))

    perimeter = 4 * side

    return perimeter


perimeter = perimeter_square()
print("Your square perimeter = ", perimeter)


# Exercise 3
def area_rectangle():
    length = float(input("Input the rectangle length:\t"))
    width = float(input("Input the rectangle width:\t"))

    area = length * width
    return area


area = area_rectangle()
print("Your rectangle surface = ", area)


# Exercise 4
def area_square():
    side = float(input("Input the side of square:\t"))
    area = side ** 2
    return area


area = area_square()
print("Your square area = ", area)

import random


def random_list():
    numbers = []
    for i in range(10):
        numbers.append(random.randint(-20, 20))

    return numbers


def negatives_count(l):
    negatives = []
    for neg_count in l:
        if neg_count < 0:
            negatives.append(neg_count)
    return len(negatives)


def positives_count(i):
    positive = []
    for pos_num in i:
        if pos_num > 0:
            positive.append(positives_count)
    return len(positive)


nums = random_list()
print(nums)
print("Negatives count:\t", negatives_count(nums))
print("Positive count:\t", positives_count(nums))
'''
import random


def random_even_List():
    even_numbers = []
    for i in range(10):
        even_numbers.append(random.randint(1, 20))
    return even_numbers


def even_list(a):
    for numbers in a:
        if numbers % 2 == 0:
            print(numbers)


n = random_even_List()
print(n)
even_list(n)
