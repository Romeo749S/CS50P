import random


def main():
    level = get_level()
    points = 0
    mistakes = 0
    for n in range(10):
        mistakes = 0
        rand_int1 ,rand_int2 = generate_integer(level) , generate_integer(level)
        while True:
            while True:
                try:
                    print (f'{rand_int1} + {rand_int2} = ' , end = '')           
                    users_int = int(input())
                    break
                except ValueError:
                    pass
            rand_int_sum = rand_int1 + rand_int2
            if users_int == rand_int_sum :
                points += 1
                break
            else :
                print('EEE')
                mistakes += 1
                if mistakes == 3:
                    print (f'{rand_int1} + {rand_int2} = {rand_int_sum}' )
                    break
    print(f'Points: {points}')


def get_level():
    while True:
        level = input('Level: ')
        if level.isdigit() and 4 > int(level) > 0:
            return int(level)


def generate_integer(level):
    if level == 1:
        a = random.randint(0 , 9)
    elif level == 2:
        a = random.randint(10 , 99)
    elif level == 3:
        a = random.randint(100 , 999)
    return a
    

if __name__ == "__main__":
    main()