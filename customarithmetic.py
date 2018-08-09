from decimal import Decimal, getcontext

getcontext().prec = 100

class CustomArithmetic:
    @staticmethod
    def add(operand1, operand2):
        return Decimal(operand1) + Decimal(operand2)

    @staticmethod
    def subtract(operand1, operand2):
        return operand1 - operand2

    @staticmethod
    def multiply(operand1, operand2):
        return operand1 * operand2

    @staticmethod
    def divide(operand1, operand2):
        return operand1 / operand2

    @staticmethod
    def power(operand1, operand2):
        return operand1 ** operand2


# print(CustomArithmetic.add(0.1, 0.2))