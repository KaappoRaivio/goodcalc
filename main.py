import time

import calc, strmanip
"""
3 * (-2)
"""

EXPR = str(input())

# EXPR = "3 * 2 + 5 ^ (1 + (-2))"
# EXPR = "4 ^ 3 - 6"
# EXPR = "2"

def evaluateExpression(expression):
    expression = strmanip.replaceAlternateOperationSigns(expression)
    expression = strmanip.correctSpaces(expression)  # Remove all the spaces
    result = calc.recursiveCalculating(expression)

    if result.startswith("$"):
        result = result[1:]
        result = "-" + result

    return result

def evaluateExpressionWithGenerate(expression):
    expression = strmanip.replaceAlternateOperationSigns(expression)
    expression = strmanip.correctSpaces(expression)  # Remove all the spaces


    yield expression
    expression = calc.calculateOneStep(expression)


    new_expr: str = expression
    old_expr: str = ""

    while new_expr is not old_expr:
        old_expr = new_expr

        yield "= " + new_expr
        new_expr = calc.calculateOneStep(old_expr)

        if new_expr.startswith("$"):
            new_expr = new_expr[1:]
            new_expr = "-" + new_expr

    raise StopIteration


if __name__ == '__main__':
    # print(strmanip.correctSpaces(EXPR))
    # print(evaluateExpression(EXPR))
    #

    for i in evaluateExpressionWithGenerate(EXPR):
        print(i)

    print(list(evaluateExpressionWithGenerate(EXPR)))
    # print(calc.calculateOneStep(EXPR))
    # for i in evaluateExpressionWithGenerate(EXPR):
    #     print(i)
    # pass
