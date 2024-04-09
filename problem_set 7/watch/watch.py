import re

def main():
    print(parse(input("HTML: ")))
    

def parse(s):
    if search := re.search(r'\<iframe.*https?://(?:www.)?youtube.com/embed/(xvFZjo5PgG0)' , s):
        return 'https://youtu.be/{}'.format(search.group(1))
    else:
        return None
    



if __name__ == "__main__":   
    main()