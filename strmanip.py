import re

OPERATION = re.compile("[+\-*/^]{1}")
OPERAND = re.compile("[0-9]")


class Manipulation:
    pass
def replaceSlice(string, l_index, r_index, replaceable):
    string = string[0:l_index] + string[r_index - 1:]
    string = string[0:l_index] + replaceable + string[r_index:]
    return string


def correctSpaces(expression):
    return expression.replace(" ", "")


def replaceAlternateOperationSigns(expression):
    return expression.replace("**", "^")


def correctUnaryConfilicts(expression):

    conflict_start: int
    conflict_end: int

    for index in range(1, len(expression)):
        if OPERATION.match(expression[index]) and OPERATION.match(expression[index - 1]):
            print(expression[index], expression[index - 1])
            conflict_start = index
            break
    else:
        return expression


    for index in range(conflict_start + 1, len(expression)):
        if OPERAND.match(expression[index]):
            continue
        else:
            conflict_end = index + 1
            break
    else:
        conflict_end = len(expression) + 1

    expression = insert(expression, conflict_start, "(")
    expression = insert(expression, conflict_end, ")")
    return correctUnaryConfilicts(expression)

def insert(dest: str, index: int, string: str):
    return dest[:index] + string + dest[index:]


print(insert("asd", 2, "terve"))

print(correctUnaryConfilicts("3+-254675--4"))