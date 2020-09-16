while True:

    try:
        a = input("add first number,print 'q' to quit.. ")
        if a == 'q':
            break
        a = int(a)
        b = input("add another number")
        if b == 'q':
            break
        b = int(b)

    except ValueError:
        print("Your input should be in number")

    else:
        c = a + b
        print(c)



