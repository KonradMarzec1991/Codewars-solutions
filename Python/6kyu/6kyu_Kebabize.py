def kebabize(string):
    import re
    mystring = ""
    for x in string:
        if x == x.lower() and x.isalpha():
            mystring += x
        elif x == x.upper() and x.isalpha():
            mystring += '-' + x
    return mystring.strip('-').lower()