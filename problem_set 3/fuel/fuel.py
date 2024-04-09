def main():
    a = round(percent_fuel())
    if 1 < a <= 90 :
        print('{}%'.format(a))
    elif 1 >= a :
        print('E')
    else :
        print('F')
    
def percent_fuel():
    while True :
        try:
            fuel_left = input('Fraction: ')    
            a,b = fuel_left.split('/')
            if ((int(a) / int(b)) * 100) > 100 :
                t = 1/0
        except (ZeroDivisionError , ValueError):
            pass   
        else:
            return (int(a) / int(b)) * 100
            
main()
    

