def main():
    print(gauge(convert('4/4')))


def convert(fraction):
    x,y = map(int , fraction.split('/'))
    if y == 0 :
        raise ZeroDivisionError
    elif x > y:
        raise ValueError
    else:
        return int(x / y * 100)
    


def gauge(percentage):
    if percentage <= 1 :
        return 'E'
    elif percentage >= 99 :
        return 'F'
    else :
        return f'{percentage}%'
    


if __name__ == "__main__":
    main()