def main():
    greet = input('Greeting: ')
    if type_greeting(greet) == 1:
        print ("$0")
    elif type_greeting(greet) == 2:
        print("$20")
    else:
        print("$100")
def type_greeting(g):
    if g.strip().lower().startswith('hello'):
        return 1
    elif g.strip().lower().startswith('h'):
        return 2
    else :
        return 0
    
main()

