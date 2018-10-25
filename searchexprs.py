from collections import namedtuple
import re

ExprSlice = namedtuple("ExprSlice", ["content", "start_pos", "end_pos"])
Calculation = namedtuple("Calculation", ["left_operand", "operation", "right_operand", "left_boundary", "right_boundary"])

PATTERN = re.compile(r"[\$0-9.]")

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

    # print(ExprSlice(expression[opening_brace_pos + 1:closing_brace_pos], opening_brace_pos, closing_brace_pos))
    return ExprSlice(expression[opening_brace_pos + 1:closing_brace_pos], opening_brace_pos, closing_brace_pos-1) # + 1 because the it has to be all-exclusive where as string slicing is in-inclusive

def getOperandsAndOperationFromIndex(expression, index):
    operation = expression[index]


    left_boundary = -1
    right_boundary = -1

    for i in range(index - 1, -1, -1):
        if PATTERN.match(expression[i]):
            left_boundary = i
        else:
            break

    for i in range(index + 1, len(expression)):
        if PATTERN.match(expression[i]):
            right_boundary = i + 1
        else:
            break
    MAGIC_CONSTANT: int
    if "." in expression[index + 1:right_boundary] or "." in expression[left_boundary:index]:
        MAGIC_CONSTANT = 2
    else:
        MAGIC_CONSTANT = 1
    a = Calculation(expression[left_boundary:index], operation, expression[index + 1:right_boundary], left_boundary, right_boundary - MAGIC_CONSTANT)
    return a

print(getOperandsAndOperationFromIndex("4*3+2", 1))