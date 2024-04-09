def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    for t in s:
        if not (t.isdigit() or t.isalpha()):
            return False
    if not s[0:2].isalpha():
        return False
    elif not (2 <= len(s) <= 6):
        return False  
    elif has_digits(s): 
        digit_list = [n.isdigit() for n in s ]
        d = digit_list.count(1)
        if not (s[-d:].isdigit()) or s[-d] == '0':
            return False
        else :
            return True        
    else:
        return True
    
def has_digits(string):
    return any(char.isdigit() for char in string)

main()
            