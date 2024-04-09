def main():
    regular_word = input('Input: ')
    print('Output:',shorten_word(regular_word))
def shorten_word(word):
    vovel_list = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
    return ''.join(['' if n in vovel_list else n for n in word])
main()

