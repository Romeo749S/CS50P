def calculation(mass):
    return pow(300000000,2) * mass
def main():
    mass = int(input("m: "))
    print('E: {}'.format(calculation(mass)))
main()