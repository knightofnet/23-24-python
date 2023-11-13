s=int(input("entrer un entier entre 1 et 10 :"))

for i in range(1,10) :
	if s < 500 :
		s=s+i**3
	
print("s=",s)


i = 0
while i < 10 and s < 500 :
	i = i + 1
	s = s + i ** 3

print("s=",s)

assert s == 794
