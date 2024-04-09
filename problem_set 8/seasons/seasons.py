from datetime import date 
import re
import sys
import inflect

p = inflect.engine()


def main():
    my_date = input('Date of Birth: ').strip()
    year, month, day = list(map(int ,format_check(my_date)))
    my_date = date_time_check(year, month, day)
    diff = int((date.today() - my_date).total_seconds() / 60)
    print(nums_to_words(diff))
   

def format_check(date):
    if bang := re.fullmatch(r'([0-9]{4})-([0-9]{2})-([0-9]{2})' , date ):
        return bang.groups()
    else:   
        sys.exit('Invalid date')


def date_time_check(year , month , day):
    try:
        return date(year, month , day)
    except (ValueError , TypeError ):
        sys.exit('Invalid date')

'''def get_minutes(date):
    diff = str(date.today() - date)
    diff1 = re.match(r'([0-9]+) ' , diff)
    return int(diff1.group(1)) * 24 * 60'''

def nums_to_words(lived_minutes):
    return f'{p.number_to_words(lived_minutes)} minutes'.replace(' and', '').capitalize()




if __name__ == "__main__":
    main()