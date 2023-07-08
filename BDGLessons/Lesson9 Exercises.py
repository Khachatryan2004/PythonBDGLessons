'''
# Exercise 1
for x in range(1, 6):
    for i in range(1, x + 1):
        print(i, end=" ")
    print()

# Exercise 2
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)

# Exercise 3
a = (input("Input numbers:\t"))
print(len(a))
'''
'''
# Exercise 4
start = int(input("Input the starting point:\t"))
end = int(input("Input the ending point:\t"))
prime_numbers = []
for x in range(start, end):
    if x > 1:
        if x % 2 == 0:
            continue
        for i in range(3, (x // 2) + 1):
            if x % i == 0:
                break
        else:
            prime_numbers.append(x)
print(prime_numbers)
print(len(prime_numbers))
'''
'''
# Exercise 5
a = 5
for x in range(1, a + 1):
    for i in range(x):
        print("*", end=" ")
    print()
for i in range(a - 1, 2, -1):
    for j in range(i):
        print("*", end=" ")
    print()
'''
# Exercise 6
'''
# Exercise 7
a = input("Input words:\t").split()
print(a)
count = {}
for word in a:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)
for key, value in count.items():
    print(f"word: {key}, count: {value}")
'''
'''
# Exercise 9
import random

a = int(input("Input numbers for your list:\t"))
b = []
for x in range(a):
    b.append(random.randint(-10, 10))
    print(b)
negative = 0
positive = 0
for i in b:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
print("Positive =", positive,",", "Negative =", negative)
'''

# Exercise 10
l = [23, 65, 19, 90]
print(l)

first_position = int(input("Enter the position of the first element:\t"))
second_position = int(input("Enter the position of the second element\t"))

l[first_position], l[second_position] = l[second_position], l[first_position]
print("Changed =", l)
