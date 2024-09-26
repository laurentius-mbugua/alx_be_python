def greeting():
    name = input("What is your name? ")
    print(f"Hello {name}")
greeting()

def area():
    Length=int(input("Enter the length of the square: "))
    Width=int(input("Enter the width of the square: "))
    area = Length*Width
    print(f"The area of the square is {area}")
area()

def even():
    number=int(input("Enter the number: "))
    if number % 2 == 0:
        print ("Even")
    else:
        print("Odd")

    again=input("Would you like to play again?(y/n)")
    if again == "y":
        even()
    else:
        print("Bye")

even()