def mafct(n) :
    s=0
    for i in range(1,n+1) :
        s = s + i*3
        print("au tour",i, "on a s =",s)
    return s
    
print(mafct(3))
print(mafct(4))
print(mafct(10))