def multiples(a, b, n) :
    retList =[]
    
    for i in range(1, n + 1) :
        if i%a == 0 or i%b == 0 :
            retList.append(i)
            
    return retList
    
def multiples_comp(a,b,n) :
    return [ i for i in range(1, n + 1) if i%a == 0 or i%b == 0 ]

assert multiples_comp(7,3,30) == [3, 6, 7, 9, 12, 14, 
                             15, 18, 21, 24, 27, 28, 30]