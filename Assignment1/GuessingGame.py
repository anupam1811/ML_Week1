import random

print("Enter a number between 1 to 10")
num=random.randint(1,10)
guess=0
count=0

while count<5:

    guess=int(input("Enter Guess: "))

    if(guess<num):
        print("Guess Higher!")
        count+=1
    elif(guess>num):
        print("Guess Lower!")  
        count+=1  
    else:
        print("You won!")
        break  
if(count>5):
    print("You are left with no Chance")    




