import re

variable = input("Enter a number: ")
#res = (re.match("^[-]?[0]{2,}[0-9]*$", first))
def valid_number():

    # matches a decimal string, and checks for leading zeroes
    if(re.match("^[-]?[0]{2,}", variable)):
        return "None"
    # checks if valid base 10 integer
    if(re.match("^[-]?[0-9]*$", variable)):
        return "int"

    # matches a binary string, and checks for leading zeroes
    if(re.match("^[-]?[0][bB][0]{2,}", variable)):
        return "None"
    if(re.match("^[-]?[0][bB][01]*$", variable)):
        return "int"

    # matches an octal string, and checks for leading zeroes
    if(re.match("^[-]?[0][oO][0]{2,}", variable)):
        return "None"
    if(re.match("^[-]?[0][oO][0-7]*$", variable)):
        return "int"

    # matches a hexadecimal string, and checks for leading zeroes
    if(re.match("^[-]?[0][xX][0]{2,}", variable)):
        return "None"
    if(re.match("^[-]?[0][xX][A-Fa-f0-9]*$", variable)):
        return "int"

    # general case for float first, then prune it after
    if(re.match("^[-]?[0-9]*[.]?[0-9]*[e]?[-]?[1-9]*$", variable)):
        return "float"
    return "None"
print(valid_number())


