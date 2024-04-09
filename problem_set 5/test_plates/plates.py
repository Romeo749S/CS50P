def main():
    is_valid('as')

def is_valid(s='bb'):
    if 2 > len(s) or len(s) > 6 :
        return 0
    elif not s[:2].isalpha():
        return 0
    elif s[-2].isdigit() and not s[-1].isdigit():
        return 0
    elif not s.isalnum():
        return 0 
    elif '0' in s and s[s.index('0')-1].isalpha():
        return 0
    else:
        return 1
    


if __name__ == "__main__":
    main()