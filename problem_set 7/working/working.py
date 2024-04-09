import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    if search := re.search(r'^([0-9]+)(?::([0-9]+))? (AM|PM){1} to ([0-9]+)(?::([0-9]+))? (AM|PM){1}$' , s ):
        list1 = search.groups()
        #print(list1)
        if 0 <= int(list1[0]) <= 12 and 0 <= int(list1[3]) <= 12:
            return f'{time_transformer(list1[0] , list1[1] , list1[2])} to {time_transformer(list1[3] , list1[4] , list1[5])}'
        else :
            raise ValueError
    else:
        raise ValueError
    
def time_transformer(hours , minutes , day_time):
    if day_time == 'PM':
        hours = int(hours) + 12
        if hours == 24:
            hours = 12
    else:
        hours = int(hours)
        if hours == 12 :
            hours = 0
    if minutes == None:
        return f'{hours:02}:00'
    elif int(minutes) < 60 :
        return f'{hours:02}:{minutes:02}'
    else:
        raise ValueError

                             

if __name__ == "__main__":
    main()