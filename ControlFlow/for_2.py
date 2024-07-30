# Create a sample collection
usersG = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
print(" ---------- Original : users = ")
print(usersG)

def del_inactive(users):
    # Strategy:  Iterate over a copy
    for user, status in users.copy().items():
        if status == 'inactive':
            del users[user]
    print(" ----------- After del inactive : users = ")
    print(users)

def get_active(users):
    # Strategy:  Create a new collection
    active_users = {}
    for user, status in users.items():
        if status == 'active':
            active_users[user] = status
    print(" ---------- active_users = ")
    print(active_users)

del_inactive(usersG)
#get_active(usersG)    

print(" ---------- Final : usersG = ")
print(usersG)