# Խնդիր 1
'''
a = int(input("Input count of numbers:\t"))
b = []
for i in range(a):
    b.append(int(input(f"Input {i} number:\t")))
    print(b)
for x in range(len(b)):
    print("Square = ", x ** 2)
# Չեղավ
#Երկրորդ ձև
a = int(input("Input count of numbers:\t"))
b = []
for i in range(a):
    a[i] = a[i] ** 2
print(a)
# Էլի Չեղավ(
#Վերջապես եղավ
count = int(input("Input the count of your list:\t"))
l = []
for x in range(count):
    l.append(int(input(f"Input {x+1} number:\t")))
print(l)
for index in range(len(l)):
    l[index] = l[index] ** 2
print(l)
'''
'''
# Խնդիր 2
a = int(input("Input count of number:\t"))
b = []
for x in range(a):
    b.append(int(input(f"Input {x} number:\t")))
    print(b)
c = 0
for x in b:
    c += x
print(c)
'''
# Խնդիր 3
'''
a = int(input("Input count of number:\t"))
b = []
for x in range(a):
    b.append(int(input(f"Input {x} number:\t")))
    print(b)
c = 1
for x in b:
    c *= x
print(c)
'''
# Խնդիր 4
'''
list = [45, 78, 20, 108, 56, 80, 20 ]
if 20 in list:
    list[list.index(20)] = 200
    print("Number 20 replaced with 200")
else:
    print("Number 20 not found")
'''
# Խնդիր 4 սա էլ input-ից
'''
a = int(input("input number:\t"))
b = []
for x in range(a):
    b.append(int(input(f"Input {x} number")))
    print(b)
for x in b:
    if 20 in b:
        b[b.index(20)] = 200
        break
else:
    print("number 20 not found")

if 200 in b:
    print(b)
'''
'''
age = int(input("Input your age:\t"))
name = input("Input you name:\t")
country = input("Input your country:\t")
gender = input("Input boy or girl:\t")
print(f"You are {name}, from {country}, and you are {age} years old {gender}, nice to meet you :D")
'''
numbers = [1, 6, 2, 90, 45, 60, 74, 26, 57, 28]
maximum = numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number
print(maximum)