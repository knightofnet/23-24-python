from turtle import *
from random import randint, random
reset()

nbMetreTotal = 0

while nbMetreTotal < 500 :

	nbMetreAvance = randint(10,50)
	sens = random()
	angle = randint(20, 90)

	if (sens < 0.5) :
		left(angle)
	else :
		right(angle)

	forward(nbMetreAvance)
	
	nbMetreTotal += nbMetreAvance


while(True) :
	pass
