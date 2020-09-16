filename="The_Koran_(Al-Qur'an)_by_G._Margoliouth_and_J._M._Rodwell.txt"
with open(filename,encoding='utf-8') as f_object:
    contents=f_object.read()
    noOfthe=contents.lower().count('the')
    print(noOfthe)
    noOfThe=contents.count('the')
    print(noOfThe)
    