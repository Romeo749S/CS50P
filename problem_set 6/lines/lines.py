import sys

def main():
    list1 = []

    if len(sys.argv) < 2 :
        sys.exit('Too few command-line arguments ')
    elif len(sys.argv) > 2 :
        sys.exit('Too many command-line arguments ')
    elif not sys.argv[1].endswith('.py'):
        sys.exit('Not a Python file ')
        
    try:
        with open(sys.argv[1]) as file:
            for row in file :
                if row.strip() != '' and not row.strip().startswith('#'):
                    list1.append(row.strip())
            print(len(list1))
    except FileNotFoundError :
        sys.exit('File does not exist ')


main()
