import random
# print(random.randint(0,2))
def check(comp,user):
    if comp==user:
        return 0
    elif (comp==1 and user==0 ):
        return -1
    elif (comp==0 and user==1 ):
        return -1
    elif (comp==1 and user==2 ):
        return -1
    else:
        return 1

comp = random.randint(0,2)
user = int(input("Enter 0 for snake 1 for water 2 for gun: "))
print(f"Computer has selected {comp}")
score=check(comp, user)
if score==0:
    print ("The game is draw")
elif score==-1:
    print ("You loose the game")
else:
    print ("You won the game")
    




