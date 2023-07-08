'''
import math
#kloracnuma nerqev
print(math.floor(5.821))
#kloracnuma verev
print(math.ceil(5.123))

#int-ova tpum
print(math.isqrt(25))

#float-ova tpum
print(math.sqrt(25))
#Tvi astichan hashvelu dzev
print(math.pow(25, 2))

#tpuma himikva jamanaky
import datetime

now = datetime.datetime.now()
print(now)


import random
import time

time.sleep(3)
print(random.randint(1, 10))
'''
'''
import random
def number():
    l = int(input("Numbers:\t"))
    r = random.randint(1, 10)
    print("random:\t", r)
    if l == r:
        return True
    else:
        return False

print(number())
'''


def upp_low_case():
    lower = []
    upper = []
    text = input("Your text:\t")
    for i in text:
        if i.islower():
            lower.append(i)
        if i.isupper():
            upper.append(i)
    print("Lower letters count is", len(lower), "Lower letters is", lower)
    print("Upper letters count is", len(upper), "Upper letters is", upper)


upp_low_case()
