import time

import calc, strmanip
"""
3 * (-2)
"""

EXPR = "(5 + 7) / (2.3 + 4.7)"

# EXPR = "3 * 2 + 5 ^ (1 + (-2))"
# EXPR = "4 ^ 3 - 6"
# EXPR = "2"

def evaluateExpression(expression):
    expression = strmanip.replaceAlternateOperationSigns(expression)
    result = calc.recursiveCalculating(expression)

    if result.startswith("$"):
        result = result[1:]
        result = "-" + result

    return result

def evaluateExpressionWithGenerate(expression):
    gen = calc.recursiveCalculatingGenerate(expression)
    yield next(gen).replace("$", "-")
    for i in gen:
        yield ''.join(["= ", i]).replace("$", "-")


if __name__ == '__main__':
    print(strmanip.correctSpaces(EXPR))
    print(evaluateExpression(EXPR))
    # for i in evaluateExpressionWithGenerate(EXPR):
    #     print(i)
    # pass