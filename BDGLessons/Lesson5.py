# Խնդիր 1
'''
a = "JohnDipPeta"
length = len(a) // 2
print(a[length - 1:length + 2])
b = "JaSonAy"
length = len(b) // 2
print(b[length - 1:length + 2])
# user-ից
word = input("Input your word:\t")
index = int(input("Input your index to be deleted:\t"))
print(word[:index] + word[index + 1:])
'''
# Խնդիր 2
'''
string = input("Input Your String:\t")
if len(string) < 3:
  print(string)
elif string[-3:] == "ing":
  print(string + "ly")
else:
  print(string + "ing")
'''
'''
# Խնդիր 3
word = input("Input your word:\t").lower()
print(word)
if word == word[::-1]:
    print("Your word is Palindrome")
else:
    print("Your word is not 'Palindrome'")
'''
# Խնդիր 4
'''
a = "How are you?"
b = a[:-1]
print(b)

c = "How are you?"
d = c[:3] + c[-5:]
print(d)
'''
# Խնդիր 5
'''
a = input("Input your String:\t")
print(a.lower())
a = input("Input your String:\t")
print(a.upper())
'''
s = "Hello"
b = "World"
sum = s + " " + b
print(sum)
print(b.join(s))