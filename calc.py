import searchexprs, strmanip
import  re

def makeOneOperation(left_operand, operation, right_operand):
    result = 0
    left_operand = left_operand.replace("$", "-")
    right_operand= right_operand.replace("$", "-")
    if operation is "+":
        result = float(left_operand) + float(right_operand)
    elif operation is "-":
        result = float(left_operand) - float(right_operand)
    elif operation is "*":
        result = float(left_operand) * float(right_operand)
    elif operation is "/":
        result = float(left_operand) / float(right_operand)
    elif operation is "^":
        result = float(left_operand) ** float(right_operand)
    else:
        raise Exception("error!")

    if result.is_integer():
        result = int(result)
    print(f"result is: {result}")
    return str(result)


def recursiveCaclulating(expression):
    expression = strmanip.correctSpaces(expression)  # Remove all the spaces

    if expression.startswith("-"):  # Replace the ambiguous unary minus with a dollar sign
        expression = expression[1:]
        expression = "$" + expression

    print(f"expression: {expression}")
    ORDER_OF_OPERATIONS = [r"\^", r"[/|*]", r"[+|-]"]  # 1. ^, 2. / and *, 3. + and -

    """
    Meta:
        1. Find braces and replace them with a recursive call with the braces' content as the argument.
        2. Start with the first item in the order of operations and find the first occurence of the operand-in-question.
        3. When an operand the same as the current being searched is found, take the surrounding numbers and perform the calculation and replace the whole thing with the result
        4. If nothing is replaced, return the argument as-is.
        5. Else, make a recursive call with the resulting string as the argument


    """
    # 1.
    braces = searchexprs.getContentInsideBraces(expression)
    if braces is not False:
        replaced_slice = strmanip.replaceSlice(expression, braces.start_pos, braces.end_pos,
                                               recursiveCaclulating(braces.content))

        return recursiveCaclulating(replaced_slice)

    # 2.
    for operation in ORDER_OF_OPERATIONS:
        regex = re.compile(operation)

        # 3.
        match = regex.search(expression)
        if match:
            calculatable = searchexprs.getOperandsAndOperationFromIndex(expression, match.span()[0])

            # 5.
            return recursiveCaclulating(strmanip.replaceSlice(expression,
                                                              calculatable.left_boundary,
                                                              calculatable.right_boundary,

                                                              makeOneOperation(
                                                                  calculatable.left_operand,
                                                                  calculatable.operation,
                                                                  calculatable.right_operand)))

    # 4.
    else:
        return expression

