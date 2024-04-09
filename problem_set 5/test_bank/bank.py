def main():
    print(value('aellohitler'))


def value(greeting):
    
    if 'hello' in greeting.lower():
        return 0
    elif 'h' in greeting[0].lower():
        return 20
    else :
        return 100
    


if __name__ == "__main__":
    main()