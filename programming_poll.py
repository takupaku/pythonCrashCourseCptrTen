while True:
    filename='Programming_pool.txt'
    lists = []
    response=input("Why do you like programming? type 'q' when done")
    lists.append(response)

    if response == 'q':
        break
    else:
        for answer in lists:
            with open(filename,'a') as f_object:
                f_object.write(answer+'\n')


