def main():
    expression = input('Expression: ')
    print('{:.1f}'.format(result(expression)))
def result(nigga):
    x,y,z = nigga.strip().split()
    match y :
        case '+' :
            return int(x) + int(z)
        case '-' :
            return int(x) - int(z)
        case '*' :
            return int(x) * int(z)
        case '/' :
            return int(x) / int(z)
main()