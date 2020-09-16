try:
    a = int(input("add first number"))
    b = int(input("add another number"))
    c=a+b
    print(c)
except ValueError:
    print("Your input should be in number")
