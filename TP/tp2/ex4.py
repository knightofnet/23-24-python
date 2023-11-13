import sys

print(type(sys.argv))
print(sys.argv)

if len(sys.argv) != 3 :
	print("Erreur : 3 paramètres sont attendus")
	exit()

n = int(sys.argv[1])
p = int(sys.argv[2])

print( sum( [ i ** p    for i in range(1, n + 1) ]) )
