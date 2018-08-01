def replaceSlice(string, l_index, r_index, replaceable):
    string = string[0:l_index] + string[r_index - 1:]
    string = string[0:l_index] + replaceable + string[r_index:]
    return string

def correctSpaces(expression):
    return expression.replace(" ", "")

def replaceAlternateOperationSigns(expression):
    return expression.replace("**", "^")

def correctUnaryBraces(expression):
    pass