from turtle import *
from random import randint, random
reset()

avancerTotale = 0

while avancerTotale < 500 :

	nbAvancer = randint(10,50)
	forward(nbAvancer)
	avancerTotale += nbAvancer

	angle = randint(20,90)
	sens = random()
	if sens < 0.5 :
		left(angle)
	else :
		right(angle)
		


while(True) :
	pass
