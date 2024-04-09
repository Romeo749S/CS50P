def main():
    menu = {
        "baja taco": 4.25,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00
    }
    meal_sum(menu)
    

def meal_sum(menu):
    sum = 0
    while True:
        try:
            meal_order = input('Item: ').lower()
            if meal_order == '' :
                return round(sum , 2)
            else:
                sum += menu[meal_order]
                print('Total: ${:.2f}'.format(sum))
        except (ValueError , KeyError):
            pass
        except(EOFError):
            return 0
main()

        
