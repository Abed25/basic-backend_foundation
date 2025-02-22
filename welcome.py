print("Morning")

def getName():
    name = input("Enter your name: ")
    return name

def welcome():
    print(f"Welcome {getName()}")


welcome()