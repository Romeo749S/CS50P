def main():
    a = date_transition()
    print('{}-{:02}-{:02}'.format(int(a[2]),int(a[0]),int(a[1])))
    
def date_transition():
    months = {
    "January" : 1 ,
    "February": 2 ,
    "March" : 3 ,
    "April" : 4,
    "May" : 5 ,
    "June" : 6 ,
    "July" : 7 ,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12,
    }
    while True :
        date = input("Date: ")
        try :
            list1 = date.split('/')
            if len(list1) == 3 :
                #a  = list1[0],list1[1],list1[2]
                list1 = [int(n) for n in list1]
                if list1[1] > 30 or list1[0] > 12:
                    pass
                else:
                    return list1
                
            elif len(list1) == 1 :
                list1 = date.split()
                if list1[0] in months and ',' in list1[1]:
                    list1[0] = months[list1[0]]
                    list1 = [int(n.strip(',')) if isinstance(n , str) else n for n in list1]
                    if list1[1] > 30 :
                        pass
                    else:
                        return list1
                else :
                    pass
        except ValueError:
            pass
        
                
            
main()