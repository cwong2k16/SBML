import re

variable = input("Enter a number: ")

# float will always have a "." or "e" in it
# check for float first
def valid_number():
    if("." in variable):
        arr = variable.split(".")
        if(len(arr)>2):
            return "None"
        else:
            first = arr[0]
            second = arr[1]

            # if res matches leading zeros, return None
            res = (re.match("^[-]?[0]{2,}[0-9]*$", first))
            if(res != None):
                return "None"
            res = re.match("^[-]?[0-9]*$", first)
            if(res == None):
                return "None"
            return "good"
        
print(valid_number())


