def is_string(word):
    if("\\" in word or len(word)<2):
        return False
    if(word[0] == '"' and word[len(word)-1] == '"' and not ('"' in word[1:len(word)-1])):
        return True
    elif(word[0] == "'" and word[len(word)-1] == "'" and not ("'" in word[1:len(word)-1])):
        return True
    return False

def validate_strings(str1, str2):
    if(str1 == "" and str2 == ""):
        return False
    elif(str1 != "" and str2 != ""):
        if(str1[len(str1)-1] == "\\"):
            str1 = str1[:len(str1)-1]
            str1 = str1.replace("\\\\", '').replace('\\"', '').replace("\\'", '')
            str2 = str2.replace("\\\\", '').replace('\\"', '').replace("\\'", '')
            if("\\" in str1 or "\\" in str2):
                return False
            else:
                return is_string(str1+str2)
    elif(str1 != ""):
        str1 = str1.replace("\\\\", '').replace('\\"', '').replace("\\'", '')
        return is_string(str1)
    else:
        str2 = str2.replace("\\\\", '').replace('\\"', '').replace("\\'", '')
        return is_string(str2)
    return False

line1 = input("Enter first string: ")
line2 = input("Enter second string: ")
print(validate_strings(line1, line2))