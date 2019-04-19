import re
import keyword

def validate_identifier():
    variable = input("Enter a string: ").strip()
    if(variable.isidentifier() and not keyword.iskeyword(variable)):
        return True
    else:
        return False

print(validate_identifier())