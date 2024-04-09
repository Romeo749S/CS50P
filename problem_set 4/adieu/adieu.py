def main():
    list1 = []
    try:
        while True:
            a = input()
            list1.append(a)
    except (EOFError , KeyboardInterrupt):
        if len(list1) > 2:
            list1 = ''.join([f'{n}, ' if n in list1[:-1] else f'and {n}' for n in list1])
        elif len(list1) == 2:
            list1 = ''.join([n if n == list1[0] else f' and {n}' for n in list1])
        else:
            list1 = str(list1[0])
        print('Adieu, adieu, to {}'.format(list1))
main()


    