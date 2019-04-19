import re

def valid_number(variable):
    if(variable == "0"):
        return "int"
    if(variable == "-" or variable == "" or variable == "-0"):
        return "None"
    if(re.match("^[-]?[0][bBoOxX][0]{2,}", variable)):
        return "None"
    if(re.match("^[-]?[0][bB][01]+$", variable)):
        return "int"
    elif(re.match("^[-]?[0][oO][0-7]+$", variable)):
        return "int"
    elif(re.match("^[-]?[0][xX][A-Fa-f0-9]+$", variable)):
        return "int"
    if(re.match("^[-]?[0-9]*$", variable)):
        return "int"
    if(re.match("^[-]?[0]{1,}[0-9]+", variable)):
        return "None"
    if(re.match("^[-]?[0-9]*[.]?[0-9]*$", variable)):
        return "float"
    if(re.match("^[-]?[0-9]*[.]?[0-9]*[e]?[-]?[0-9]+$", variable)):
        return "float"
    return "None"

var = input("Enter a number: ")
print(valid_number(var))