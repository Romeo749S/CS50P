def main():
    
    coin_status()

def coin_status():
    i=0 

    while i  <= 50:
        coins = input("Insert Coins: ")
        while True:
            match coins:
                case '5' | '10' | '25' :
                    i+=int(coins) 
                    if i >= 50:
                        print ('Change Owed: {}'.format(i-50))
                        return 0
                    print ('Amount Due: {}'.format(50-i))
                    break
                case _:
                    print ('Amount Due: {}'.format(50-i))
                    break
    return 0
main()
                        