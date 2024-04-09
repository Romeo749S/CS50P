def main():
    print(shorten('fga,'))


def shorten(word):
    a = ''
    for n in word.lower():
        if n not in ['a' , 'e' ,'i' ,'o' ,'u']:
            a = a + n
    return a

    
    


if __name__ == "__main__":
    main()