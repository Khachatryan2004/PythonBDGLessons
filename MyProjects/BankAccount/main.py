from base import BankAccount
import random

account_number = 553612
balance = random.randint(1, 5000)
selfaccount = BankAccount(account_number, balance)
if account_number == 553612:
    press = int(input(
        "Մուտքագրման համար սեղմեք.\t" + "1\n""Ելքագրման համար սեղմեք.\t" + "2\n" "Հաշվի մնացորդը տեսնելու համար սեղմեք․\t" + "3\n" + "Click:\t"))

    if press == 1:
        selfaccount.deposit()
    elif press == 2:
        selfaccount.withdraw()
    elif press == 3:
        print("Հաշվի մնացորդ:\t", selfaccount.balance)
    else:
        print(print("\n Որևէ բան սխալ է:\n Խնդրում ենք փորձել ավելի ուշ.\n Շնորհակալություն!"))
