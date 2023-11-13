#tri A
print("triA")
nombres = [1, -1, 2, -2, 3, -3, 0]
tries = sorted(nombres)
triesDec = reversed(tries)
triesDec = tries[::-1]
print(tries)
print(nombres)

#tri B
print("triB")
nombres = [1, -1, 2, -2, 3, -3, 0]
tries = nombres.sort()
nombres.reverse()
print(tries)
print(nombres)