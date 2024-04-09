import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    search = re.findall(r'(\bum\b)' , s , re.IGNORECASE)
    return len(search)
        
    





if __name__ == "__main__":
    main()