def main():
    camel_name = input("camelCase: ")
    print(changer_to_snake(camel_name))

def changer_to_snake(nigga):
    return ''.join(['_' + n.lower() if n.isupper() else n for n in nigga])
    '''for n in nigga:
        if n.isupper():
            nigga = nigga[:(nigga.index(n))] + '_' + n.lower() + nigga[(nigga.index(n)+1):]
    return nigga'''


    
main()
    
            