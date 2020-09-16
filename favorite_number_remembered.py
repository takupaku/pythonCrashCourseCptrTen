import json

filename = 'favoriteNumber.json'

try:
    with open(filename) as f_object:
        content = json.load(f_object)
        print("I know your favourite number is "+content)

except FileNotFoundError:
    favoriteNumber = input('what is your favourite number?')
    favoriteNumber = str(favoriteNumber)
    with open(filename, 'w') as f_object:
        json.dump(favoriteNumber, f_object)
        print("Your name has been stored in the database")

