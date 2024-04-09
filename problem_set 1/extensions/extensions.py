def main():
    file_name = input('File name: ')
    print(suffix_checker(file_name))

def suffix_checker(nigga):
    if '.' not in nigga:
        return 'application/octet-stream'
    
    a = nigga.strip().lower().split('.')
    match a[-1] :
        case 'jpeg' | 'jpg' | 'gif' | 'png' :
            if a[-1] == 'jpg':
                a[-1] = 'jpeg'
            return 'image/' + a[-1] 
        case 'txt' :
            return 'text/plain'
        case 'pdf' | 'zip':
            return 'application/' + a[-1]
        case _:
            return 'application/octet-stream'
main()

   