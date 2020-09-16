name=input('what is your name?')
filename= 'guest.txt'
with open(filename,'w') as f_object:
    f_object.write(name)


