import re
import keyword

def validate_identifier():
    variable = input("Enter a string: ").strip()
    if(len(variable)==0):
        return False
    else:
        if(len(variable)==1):
            return (variable[0].isalpha() or variable[0] == "_")
        else:
            if((variable[1:]).isidentifier() and not keyword.iskeyword(variable[1:])):
                return True
            else:
                return False


print(validate_identifier())