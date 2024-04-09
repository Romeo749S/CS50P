def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if answer_check(answer):
        print('yes')
    else:
        print('no')

def answer_check(p):
    match p.strip().lower() :
        case '42' | 'forty two' | 'forty-two':
            return True
main()