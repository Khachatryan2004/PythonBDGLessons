# Խնդիր 1
list1 = []
list2 = []
for i in range(3):
    a = int(input(f"Input {i + 1} number for list1:\t"))
    list1.append(a)
    b = int(input(f"Input {i + 1} number for list2:\t"))
    list2.append(b)
list1 = set(list1)
list2 = set(list2)
# Խնդիր 1.1
print(list1)
print(list2)
# Խնդիր 1.2
if list1 == list2:
    print("List1 is equal to list2")
else:
    print("list1 is not equal to list2")
# Խնդիր 1.3
union = list1.union(list2)
print("Union = ", union)

# Խնդիր 1.4
Intersection = list1.intersection(list2)
if list1.intersection(list2):
    print("I was able to find Intersection")
else:
    print("I was not able to find Intersection")
print("The number is  =", Intersection)
# Խնդիր 1.5
difference1 = list1 - list2
difference2 = list2 - list1
print("list1 - list2 = ", difference1)
print("list2 - list1 = ", difference2)

#i did it)
