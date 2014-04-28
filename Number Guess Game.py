import random

COMPUTERGUESS = random.randint(1, 20)

print ("You have 10 tries to guess a number between 1 and 20\n\n")

PLAYERGUESS = int(input("Enter a guess? "))

COUNTER = 1

if PLAYERGUESS == COMPUTERGUESS:
    print("You got it right on the FIRST try!!!!")
    COUNTER = 11
else:
    print ("Wrong!")
    

while COUNTER < 10:
    
    PLAYERGUESS = int(input("Enter another guess?"))
    if PLAYERGUESS == COMPUTERGUESS:
        print("You got it this time!")
        COUNTER = 11
    else:
        print ("Wrong Again!")
        COUNTER +=1
        
print ("\n\nThe Game is over.")

if COUNTER == 11:
    print ("\nYou Won!")
else:
    print ("\nYou LOST, the number was", COMPUTERGUESS)
