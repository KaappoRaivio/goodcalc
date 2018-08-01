import calc, strmanip
"""
3 * (-2)
"""

EXPR = "3.2**2"

# EXPR = "3 * 2 + 5 ^ (1 + (-2))"
# EXPR = "4 ^ 3 - 6"
# EXPR = "2"

def evaluateExpression(expression):
    expression = strmanip.replaceAlternateOperationSigns(expression)
    result = calc.recursiveCaclulating(expression)

    if result.startswith("$"):
        result = result[1:]
        result = "-" + result

    return result


if __name__ == '__main__':
    # print(strmanip.correctSpaces(EXPR))
    print(evaluateExpression(EXPR))
