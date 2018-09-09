# voorbeeld uitwerking
# for loop
# op drie verschillende manieren dezelfde output maken
# mbv for loop


lijst1 = ["Hello ","World","!"]
lijst2 = ["H","e","l","l","o"," ","W","o","r","l","d","!"]
string = "Hello World!"

print("Lijst 1: ",lijst1)
print("Lijst 2: ",lijst2)
print("String: ",string)

print(40*"-")

for word in lijst1:
    for letter in word:
        print(letter)

print(40*"-")

for item in lijst2:
    print(item)

print(40*"-")

for letter in string:
    print(letter)

print(40*"-")
