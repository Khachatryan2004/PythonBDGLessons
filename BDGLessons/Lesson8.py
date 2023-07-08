print(
    "Variable",
    "Declaration",
    "Assignment",
    "Data types",
    "Integer",
    "String",
    "Boolean",
    "true",
    "else",
    "array",
    "if",
    "false",
)

dictionary = {
    "variable": "Փոփոխական",
    "declaration": "Հայտարարում",
    "assignment": "Վերագրում",
    "data types": "Տվյալների տիպեր",
    "integer": "Թվային տիպ",
    "string": "Տողային տիպ",
    "boolean": "Բուլյան տիպ",
    "true": "Ճշմարիտ",
    "else": "Հակառակ դեպքում",
    "array": "Զանգված",
    "if": "Եթե",
    "false": "Կեղծ"
}
translate = input("Input the word to translate from the top:\t").lower()
if translate in dictionary:
    print(f"{translate} is {dictionary[translate]}")
else:
    print("There is no such word")

#seperated_list = list(map(int, input("Input numbers seperated by space:\t").split()))
#print(seperated_list)
