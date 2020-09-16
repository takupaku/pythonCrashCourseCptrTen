with open('learning_python.txt') as f_object:
    contents= f_object.readlines()

for line in contents:
    print(line.replace('python','C').rstrip())
