import json
def get_stored_username():
    filename="username.json"
    try:
        with open(filename) as f_object:
            content = json.load(f_object)
    except FileNotFoundError:
        pass
    else:
        return content


def get_new_username():
    name=input("what is your name?")
    filename="username.json"
    with open(filename,'w') as f_object:
        json.dump(name,f_object)
        return name

def greet_user():
    username=get_stored_username()
    if username:
        question=input('Are you '+ username+"?")
        if question=='y':
            print("welcome "+username)
        else:
            question=get_new_username()
            print(question + ", your name has been stored!!")

    else:
        username=get_new_username()
        print(username+", your name has been added!!")

greet_user()
