import json
favoriteNumber=input('what is your favourite number?')
favoriteNumber=str(favoriteNumber)
filename = 'favoriteNumber.json'
with open(filename,'w') as f_object:
    json.dump(favoriteNumber,f_object)

with open(filename) as f_object:
    content=json.load(f_object)

print("I know your favourite number is "+content)


