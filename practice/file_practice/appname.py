def main():
    name = input('cjo? ')

    with  open('name.txt' , 'a') as file:
        file.write(f'{name}\n')
    

main()