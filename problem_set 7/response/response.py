from validator_collection import validators, checkers, errors

def main():
    email = input("What's your email address? ")
    try:

        email_address = validators.email(email)
        print('Valid')
    except errors.EmptyValueError:
        print("Empty String")
    except errors.InvalidEmailError:
        print("Invalid")

main()