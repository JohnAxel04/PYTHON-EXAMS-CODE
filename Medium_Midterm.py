#Medium Part 1

num = eval(input("Put a Number to Start: "))

for i in range(1,11):
    for l in range(1,num + 1):
        print(f"{l:<2} x {i:>2} = {l * i:>3}",end="   ") #:<3/2 to make it align better and also spaces ratter than \t
    print()

#Medium Part 2

for x in range(1,6):
    for n in range(6,x,-1):#For Space
        print(" ",end=" ")
    for t in range(0,x):#0 starter so that no space above
        print("*  ",end=" ") #Add two spaces to make it like that
    print()