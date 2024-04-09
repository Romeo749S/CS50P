import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if search := re.search(r'^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$' , ip , re.IGNORECASE  ):
        for n in range(len(search.groups())):
            if int(search.group(n+1)) <= 255:
                continue
            else :
                return False
        return True
    else :
        return False
            
       





if __name__ == "__main__":
    main()