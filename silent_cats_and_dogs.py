filenames = ['cats.txt','dogs.txt']
for filename in filenames:
    try:
        with open(filename,encoding='utf-8') as f_object:
            contents=f_object.read()
            print(contents)

    except FileNotFoundError:
        pass
