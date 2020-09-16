flag=True
while flag:
    name = input("What is your name? Type 'q' when done")
    filename = 'guestbook.txt'

    if name=='q':
        break
    else:
        with open(filename, 'a')as f_object:
            f_object.write(name+'\n')
            print('welcome,' + name + '!\n')




