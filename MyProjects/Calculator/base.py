class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        return x + y

    def substract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y

        else:
            return "Cant divide by zero, please try again"
