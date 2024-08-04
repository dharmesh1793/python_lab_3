class Calculator:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def add(self):
        return self.__num1 + self.__num2

    def subtract(self):
        return self.__num1 - self.__num2

# Create a Calculator object
calculator = Calculator(10, 5)

# Perform addition
print("Addition result:", calculator.add())

# Perform subtraction
print("Subtraction result:", calculator.subtract())