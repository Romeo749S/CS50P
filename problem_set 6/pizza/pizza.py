from tabulate import tabulate
import sys
import csv

def main():
    list1 = []
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments ')
    elif len(sys.argv) < 2:
        sys.exit('Too few command-line arguments ')
    elif not sys.argv[1].endswith('.csv'):
        sys.exit('Not a CSV file ')

    try:
        with open(sys.argv[1]) as file:
            for row in file:
                list1.append(row.strip().split(','))
            print(tabulate(list1 , headers = 'firstrow' , tablefmt = 'grid') )
                
                
    except FileNotFoundError :
        sys.exit('File doesn\'t exist ')

if __name__ == '__main__':   
    main()