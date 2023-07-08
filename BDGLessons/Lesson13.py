# խնդիր 1
'''
def a():
    with open("poem.txt", "r") as f:
        for x in f:
            print(x, end="")
        f.close()
a()
'''
'''
# խնդիր 2
def word_count():
    with open("story.txt", "r") as f:
        a = f.read()
        count = len(a.split())
        print(f"Total count of words {count}")


word_count()
'''
'''
# խնդիր 3
def b():
    with open("poem.txt", "a") as f:
        f.write("Hello my name is\n")


def c():
    with open("poem.txt", "r") as f:
        print(f.read())
b()
c()
'''

# խնդիր 4
'''
def display_words():
    with open("story.txt", "r") as f:
        text_element = f.read().split()
    for word in text_element:
        if len(word) <= 4:
            print(word)


display_words()
'''
# խնդիր 5
with open("poem.txt", "r") as poem:
    with open("story.txt", "w") as story:
        for x in poem:
            story.write(x)

