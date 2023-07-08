# խնդիր 1
'''
def divide():
    try:
        return 10 / 2

    except:
        return None


print(divide())

def divide2():
    try:
        return 10 / 0

    except:
        return None


print(divide2())
'''

# խնդիր 2
'''
def sum_numbers():
    try:
        l = []
        inp = int(input("Enter count of numbers:\t"))
        for x in range(inp):
            l.append(int(input(f"Enter {x + 1} number:\t")))
            print(l)
        return sum(l)
    except ValueError:
        return None
#TypeError-ov areci ValueError er talis, senc anum em ashxatuma bayc vor grum em TypeError chi ashxatum

print(sum_numbers())
'''

# խնդիր 3
'''
def file_error():
    try:
        with open("python.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return None


print(file_error())
'''
# խնդիր 4
import math


def index_error():
    l = []
    inp = int(input("Enter count of numbers:\t"))
    for x in range(inp):
        l.append(int(input(f"Enter {x + 1} number:\t")))
    print(l)
    if len(l) <= 2:
        return None
    try:
        first_num = l[0]
        last_num = l[-1]
        product = first_num * last_num
        return product
    except IndexError:
        return None


print(index_error())
