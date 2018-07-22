
from collections import namedtuple
import re

EXPR = "3 - 5 +a 2"
PATTERN = re.compile(r"[0-9]")

ExprSlice = namedtuple("ExprSlice", ["content", "start_pos", "end_pos"])
Calculation = namedtuple("Calculation", ["left_operand", "operation", "right_operand", "left_boundary", "right_boundary"])

def replaceSlice(string, l_index, r_index, replaceable):
    string = string[0:l_index] + string[r_index - 1:]
    string = string[0:l_index] + replaceable + string[r_index:]
    return string

# print(replaceSlice("1234567890", 2, 6, "terve"))

def getContentInsideBraces(expression):
    if not expression:
        raise Exception("no argument provided !")

    opening_brace_pos = -1
    closing_brace_pos = -1

    opening_braces_encountered = 0

    for index in range(len(expression)):
        if expression[index] in ["(", "[", "{"]:
            opening_brace_pos = index
            opening_braces_encountered += 1
            break

    for index in range(opening_brace_pos, len(expression)):
        if expression[index] in ["(", "[", "{"]:
            opening_braces_encountered += 1
            continue

        if expression[index] in [")", "]", "}"]:
            opening_braces_encountered -= 1
            if opening_braces_encountered == 1:
                closing_brace_pos = index
                break

    if opening_brace_pos == -1 and closing_brace_pos == -1:
        return False

    print(ExprSlice(expression[opening_brace_pos + 1:closing_brace_pos], opening_brace_pos, closing_brace_pos - 1))
    return ExprSlice(expression[opening_brace_pos + 1:closing_brace_pos], opening_brace_pos, closing_brace_pos - 1) # + 1 because the it has to be all-exclusive where as string slicing is in-inclusive

def correctSpaces(expression):
    return expression.replace(" ", "")

def getOperandsAndOperationFromIndex(expression, index):
    operation = expression[index]

    # print(expression, operation, index, sep=", ")

    left_boundary = -1
    right_boundary = -1

    for i in range(index - 1, -1, -1):
        if PATTERN.match(expression[i]):
            left_boundary = i
        else:
            break

    for i in range(index + 1, len(expression)):
        # print(expression[i])
        if PATTERN.match(expression[i]):
            # print(f"match: {expression[i]}, i:{i}")
            right_boundary = i + 1
        else:
            break
    a = Calculation(expression[left_boundary:index], operation, expression[index + 1:right_boundary], left_boundary, right_boundary)
    print(a)
    return a



def recursiveCaclulating(expression, _negative=False):
    negative = False
    if expression.startswith("-") and not _negative:
        expression = expression[1:]
        negative=True

    print(f"expression: {expression}")
    ORDER_OF_OPERATIONS = [r"\^", r"[/|*]", r"[+|-]"]

    """
    Meta:
        1. Find braces and replace them with a recursive call with the braces' content as the argument.
        2. Start with the first item in the order of operations and find the first occurence of the operand-in-question.
        3. When an operand the same as the current being searched is found, take the surrounding numbers and perform the calculation and replace the whole thing with the result
        4. If nothing is replaced, return the argument as-is.
        5. Else, make a recursive call with the resulting string as the argument


    """
    #1.
    braces = getContentInsideBraces(expression)
    if braces is not False:
        return recursiveCaclulating(replaceSlice(expression, braces.start_pos, braces.end_pos, recursiveCaclulating(braces.content)))
    #2.
    for operation in ORDER_OF_OPERATIONS:
        regex = re.compile(operation)
        #3.
        match = regex.search(expression)
        if match:
            calculatable = getOperandsAndOperationFromIndex(expression, match.span()[0])
            # print(f"asd: {expression[calculatable.left_boundary:calculatable.right_boundary]}")
            #5.
            return recursiveCaclulating(replaceSlice(expression,
                                                     calculatable.left_boundary,
                                                     calculatable.right_boundary,

                                                     makeOneOperation(
                                                         calculatable.left_operand,
                                                         calculatable.operation,
                                                         calculatable.right_operand)), _negative=negative)
    #4.
    else:
        return expression if not (_negative or negative) else str(int(expression) * -1)

def makeOneOperation(left_operand, operation, right_operand):
    result = 0
    if operation is "+":
        result = int(left_operand) + int(right_operand)
    elif operation is "-":
        result = int(left_operand) - int(right_operand)
    elif operation is "*":
        result = int(left_operand) * int(right_operand)
    elif operation is "/":
        result = int(left_operand) / int(right_operand)
    elif operation is "^":
        result = int(left_operand) ** int(right_operand)
    else:
        raise Exception("error!")

    return str(result)
print(correctSpaces(EXPR))
print(recursiveCaclulating(correctSpaces(EXPR)))
