size = int (input("Enter size of pattern: "))
i = 0
while i < size:
    j = 0
    while j < size:
        print("*", end="")
        j += 1
    print ()
    i +=1