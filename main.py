import time

import calc, strmanip
"""
3 * (-2)
"""

EXPR = "3+5/2^(3+(3 * (-5)))"

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



if __name__ == '__main__':
    for i in calc.recursiveCalculatingGenerate(EXPR):
        print(i)
        time.sleep(1)
    # pass