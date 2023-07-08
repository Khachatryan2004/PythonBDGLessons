# Խնդիր 1
'''
print(list(i for i in range(10, 100) if i % 4 == 0 and float(1)))
'''
# Խնդիր 2
'''
t = int(input("Temperature °C:\t"))
if t <= 18:
    print("Cold")
elif 18 < t < 24:
    print("It's nice")
else:
    print("Hot")
'''
'''
# Խնդիր 3
x = 0
while x < 40:
    x += 4
    print(x)
'''
'''
# Խնդիր 4
print(list(x for x in range(100, 601) if x % 3 == 0 and x % 7 == 0 and x % 11 != 0))
'''

# Խնդիր 5
'''
a = int(input("Start:\t"))
b = int(input("End:\t"))
for i in range(a, b+1):
    if i % 7 == 0:
        print(i)
#ինչքան փորձեցի չեղավ ուզածս :D
'''
# Խնդիր 6
a = int(input("Input Your Number:\t"))
f = 1
for i in range(2, a + 1):
    f *= i
print(f)

