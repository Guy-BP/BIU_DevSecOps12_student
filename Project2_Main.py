from Project2_Class import MyUser
import json
import requests
import time

# create an empty list to store MyUser objects
user_list = []

# make a get request to the specified page
response = requests.get('https://jsonplaceholder.typicode.com/users')

# convert the page response into json format
page_data = json.loads(response.text)

while True:
    # specify the name you want to check
    name_received = str(input('\nPlease enter your name: ')).title()

    # check if the name appears in the data and if already added to list
    user_found = False
    for user in page_data:
        if user['name'] == name_received:
            mofa = MyUser(user['id'], user['name'], user['username'], user['email'])
            already_added = False
            for u in user_list:
                if u.id == mofa.id:
                    already_added = True
                    break
            if not already_added:
                user_list.append(mofa)
                print('The user was found and added to the list.')
            else:
                print('The user was already found.')
            user_found = True
            break

    if not user_found:
        print('User not found.')

    time.sleep(2)
    print(*user_list)