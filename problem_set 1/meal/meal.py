def main():
    time = input('What time is it? ')
    if convert(time) == 0:
        print("fuck you nigga")
    elif 7 <= convert(time) <= 8:
        print('breakfast time')
    elif 12 <= convert(time) <= 13:
        print('lunch time')    
    elif 18 <= convert(time) <= 19:
        print('dinner time')
        
    

def convert(time):
    if ':' not in time :
        return 0
    a , b = time.split(':')
    if 'a' in b :
        b , c  = b.strip().split()
    elif 'p' in b:
        b , c = b.strip().split()
        a = int(a) + 12 
    b = (int(b) / 0.6 )/100
    return float(a) + b


    


if __name__ == "__main__":
    main()