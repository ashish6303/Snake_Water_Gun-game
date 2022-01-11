import random

def gameWin(computer,you):
    if computer==you:
        return None
    elif computer=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif computer=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
    elif computer=='w':
        if you=='g':
            return False
        elif you=='s':
            return True

print("Coumuter turn : snake(s) water(w) gun(g)? ")
randNo=random.randint(1,3)
if randNo==1:
    computer='s' 
elif randNo==2:
    computer= 'w'
elif randNo==3:
    computer='g'

you = input("Coumuter turn : snake(s) water(w) gun(g)? ")
print(f"Computer chose {computer}")
print(f"You chose {you}")

a=gameWin(computer,you)
if a== None:
    print("Game is tie")
elif a:
    print("You win")
else:
    print("You lose")