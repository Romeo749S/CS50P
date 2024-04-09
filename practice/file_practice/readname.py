def main():
    with open('name.txt' , 'r') as file:
        for name in file:
            print(name.strip())
main()