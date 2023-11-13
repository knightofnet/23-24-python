def f(n):
   print(f"f({n})")
   if (n < 10):
       return 1 
   else:
       return 2+f(n-7)

print(f(23))
print()

def h(n):
   print(f"h({n})")
   if (n > 2):
      n = n-6 
      print(n) 
      h(n)

h(25)