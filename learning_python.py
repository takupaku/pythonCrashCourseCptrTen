print("print the entire loop")
with open('learning_python.txt') as f_object:
    contents= f_object.read()
    print(contents)

print("\nprinting contents with loop!!")
with open('learning_python.txt') as f_object:
    for line in f_object:
        print(line.rstrip())

print("storing files to work with!!")
with open('learning_python.txt') as f_object:
    contents= f_object.readlines() #readlines() stores lines in a list


for line in contents:
    print(line.rstrip())








