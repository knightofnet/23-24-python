#Exo 1 :
def exo1() :
    mavar = {8,4,5,1,8,-2,4,8}
    print(len(mavar))
    print(mavar)
    print(type(mavar))

    #print(mavar[1])

    mavar.add(9)
    mavar.remove(5)

    ens = { i ** 2  for i in range(-10, 5 + 1)}
    print(ens)

    ens2 = { "bonjour", "sylvie", "et", "sylvia"}
    print(ens2)

def exo2() :
    e1 = {8,4,5}
    e2 = {-1,8,2}
    e3 = e1 | e2
    e4 = e1 & e2
    e5 = e1 - e2
    print("e1=",e1," e2=",e2)
    print("e1 | e2 = ",e3)
    print("e1 & e2 = ",e4)
    print("e1 - e2 = ",e5)

    e6 = {4,4,8,5,8}
    print("e1=e6 ? ",e1==e6)
    print("e4<=e1 ? ",e4<=e1)

def exo3() :
    d = {2:4,5:25,3:9,7:49}
    print(d)
    print(type(d))
    print(len(d))

    for c in d :
        print("clé : ",c," valeur : ",d[c])


    d2 = {7:49,5:25,2:4,3:9}
    print(d2)
    print(d==d2)

    d3 = {n:n**2  for n in range(1, 10 + 1)}
    print(d3)

def exo5() :
    di = {"léo" :10,"jo" :7, "lana" :9}
    print(di)
    print(di.get("jo",0))
    print(di.get("ilo",0))

exo5()







