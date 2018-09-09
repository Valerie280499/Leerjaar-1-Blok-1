# Voorbeelden behorend bij les 5

# Voorbeeld behorend bij slide 6
hello = "Hello World!"
print(hello[2])
print(hello.index("e"))


# Voorbeeld behorend bij slide 8
s = "Hello World!"

print(s[2])     #print index 2
print(s[:2])    #print index 0,1 (begin tot 2)
print(s[2:])    #print index 2,3,4 etc (2 tot en met eind)
print(s[2:4])   #print index 2 en 3 (2 tot 4)

print(s[-1])    #print index -1 (einde)
print(s[:-1])   #print vanaf 0 tot -1 (begin tot -1) (alles behalve einde)
print(s[-1:])   #print vanaf index -1 (einde tot en met einde)
print(s[-4:-1]) #print index -4 tot -1 (4 geteld vanaf einde tot -1)

print(s[-1:-4]) #que?


# Voorbeeld horend bij het onderwerk Tuples
# Zoals je ziet hebben tuples, net als strings en lists, ook indices
tup = ("a","b")
print(tup[0])
