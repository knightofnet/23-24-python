s= 10
"""
for i in range(1,10) :
	s=s+i**3
	if s>=500 :		
		break
"""
"""
i = 1
while s < 500 and i < 10:
	s=s+i**3
	i+= 1

"""
for i in range(1,10) :
	if s < 500 :
		s=s+i**3	
	

print("s=",s)

assert s == 794
