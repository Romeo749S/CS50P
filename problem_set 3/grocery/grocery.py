def main():
    list1 = [] 
    try:   
        while True : #loop for saving all groceries in a list
            meal = input()
            if meal == '':
                break
            list1.append(meal)
    except (EOFError , KeyboardInterrupt):
        a = items_sort(list1)
        for i in range(len(a[0])):#loof for displaying results
            print('{} {}'.format(a[0][i] , a[1][i].upper()))
    
    
    
#function that returns list for quantyty of griceries and list if griceries itself
def items_sort(list1):
    list1.sort() # sorts all griceries in alpha order
    
    list2 = [] 
    for n in list1 : 
        list2.append(list1.count(n))#putting the quant. in
        a = list1.count(n) - 1 
        while  a > 0:	#loop for removing duplicates
            list1.remove(list1[list1.index(n)+a])
            
            a -= 1
    
    return list2, list1 
    
                    
main()