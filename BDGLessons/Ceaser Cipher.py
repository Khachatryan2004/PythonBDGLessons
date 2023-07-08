import string


def alphabet():
    alphabet = list(string.ascii_lowercase)
    return alphabet


def decode():
    str_ = ""
    alpha = string.ascii_lowercase
    for i in range(len(text)):
        index_of_alpha = alpha.index(text[i])
        print("Index of letter", index_of_alpha)
        print("The index that was obtained", index_of_alpha + key)
        if index_of_alpha + key >= len(alpha):
            str_ += alpha[index_of_alpha + key - len(alpha)]
        else:
            str_ += alpha[index_of_alpha + key]
    print("Obtained letter", str_)


key = int(input("Number:\t"))
text = input("Encode:\t").lower()
decoded = decode()
if decoded:
    print(decoded)


def encode():
    str_ = ""
    alpha = string.ascii_lowercase
    for i in range(len(text)):
        index_of_alpha = alpha.index(text1[i])
        print("Index of Letter", index_of_alpha)
        print("The index that was obtained", index_of_alpha - key1)
        if index_of_alpha - key1 < 0:
            str_ += alpha[index_of_alpha - key1 + len(alpha)]
        else:
            str_ += alpha[index_of_alpha - key1]
    print("Obtained letter", str_)


key1 = int(input("Number:\t"))
text1 = input("Decode:\t").lower()
encoded = encode()
if encoded:
    print(encoded)
