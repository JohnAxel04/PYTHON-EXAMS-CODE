#Easy A

print("Easy Part 1")

for i in range(1,5):
    for m in range(5,i,-1):
        print(" ",end="")
    for n in range(1,i * 2):
        print("*",end="")
    print()

#Easy B

print("Easy Part 2")

for q in range(1,6):
    for s in range(0,q):
        print(q,end="")
    print()