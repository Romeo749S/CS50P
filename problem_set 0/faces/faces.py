def convert(string):
    if ':)' in string :
        string = string.replace(':)' , '🙂') 
    if ':(' in string :
        string = string.replace(':(' , '🙁')
    return string

def main():
    input1 = input()
    print(convert(input1))
main()


