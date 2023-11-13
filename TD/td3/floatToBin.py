from decimal import Decimal, getcontext
def floatToBinary(flt, precision) :
	getcontext().prec = precision
	d = Decimal(flt)
	i = int(d * (1 << (precision - 1)))
	
	return bin(i)
    
print(floatToBinary(0.1, 24))
print(floatToBinary(0.1, 100))