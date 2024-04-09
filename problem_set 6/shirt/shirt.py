from PIL import Image , ImageOps
import sys

def main():
    if len(sys.argv) > 3 :
        sys.exit('Too many command-line arguments ')
    elif len(sys.argv) < 3 :
        sys.exit('Too few command-line arguments ')
    elif sys.argv[1][-4:] != sys.argv[2][-4:]:
        sys.exit('Input and output have different extensions ')
    try:
        a = Image.open(sys.argv[1])
        b = Image.open('shirt.png')
        a = ImageOps.fit(a , (600,600))

        a.save(sys.argv[2] , a.paste(b,b))
    except FileNotFoundError:
        sys.exit('Invalid Input')






if __name__ == '__main__':
    main()