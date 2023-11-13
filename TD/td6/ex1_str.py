s = "Once upon a time in a little town..."
print(s[2:8])
print(s[:5])
print(s[3:])

# syntaxe : s[a:b:c]
# où :
# - a : la borne de début du slicing : par défaut : 0
# - b : la borne de fin, exclue. Par défaut : la fin
# - c : le pas. Par défaut : 1

def fct1(ch1,ch2):
    s = ""
    for i in range(4):
        s = s + ch1 + ch2*2
    s = s + ch1
    return s

s1 = fct1("*","£")
print(s1)

#s1[6] = "~"
#s1 = s1[0:6] + s1[6:].replace("*", "~", 1)
s1 = s1[0:6] + "~" + s1[7:]

lst = list(s1)
lst[6] = "~"
s1 = "".join(lst)

print(s1)