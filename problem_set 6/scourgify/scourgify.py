import sys
import csv


def main():
    list1 = []
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments ')
    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments ')
    elif not sys.argv[1].endswith('.csv') and not sys.argv[2].endswith('.csv'):
        sys.exit('Not a csv file')
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['last'] , row['first'] = row['name'].split(', ')
                student = {'first' : row['first'].strip() ,'last' : row['last'].strip() , 'house' : row['house']}
                list1.append(student)

    except FileNotFoundError:
        sys.exit('Could not read 1.csv ')

    with open(sys.argv[2] , 'w') as file:
        writer = csv.DictWriter(file , fieldnames=[ 'first' , 'last' , 'house' ])
        writer.writeheader()
        writer.writerows(list1)


if __name__ == '__main__':
    main()