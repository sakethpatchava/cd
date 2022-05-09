lines = "int a = b * c ;"

keywords    = ["void", "main", "int", "float", "bool", "if", "for", "else", "while", "char", "return"]
operators   = ["=", "==", "+", "-", "*", "/", "++", "--", "+=", "-=", "!=", "||", "&&"]
punctuations= [";", "(", ")", "{", "}", "[", "]"]

def is_int(x):
    try:
        int(x)
        return True
    except:
        return False

for i in lines.strip().split(" "):
    if i in keywords:
        print (i, " is a keyword")
    elif i in operators:
        print (i, " is an operator")
    elif i in punctuations:
        print (i, " is a punctuation")
    elif is_int(i):
        print (i, " is a number")
    else:
        print (i, " is an identifier")
