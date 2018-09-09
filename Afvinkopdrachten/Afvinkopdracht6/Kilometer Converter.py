#opdracht 1 kilometer converter
"""
def vraag():
    A = int(input("Aantal kilometers:"))
    B = A*0.6214
    print ("Aantal miles:" ,B)

vraag()
"""

#opdracht 17 prime Numbers
"""
def is_prime():
    A = int(input("Getal:"))
    if A > 1:
        for i in range(2,A):
            if (A % i) == 0:
                print(A, "is geen prime nummer")
                break
            else:
                print(A, "is een prime nummer")
    else:
        print(A, "is geen prime nummer")


is_prime()
"""

#opdracht 21 rock, paper, scissors game

def game():
    import random
    A = str(random.randint(1,3))
    print(A)
    if A == 1:
        #rock = A
        print("rock")
    elif A == 2:
        #paper = A
        print("paper")
    elif A == 3:
        #scissors = A
        print("scissors")
game()
