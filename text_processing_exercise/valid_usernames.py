def characters_in_username(username):
    for character in username:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True

def  is_no_symbols(username):
    if " " in username:
        return False
    return True

def username_len(username):
    if 3 <= len(username) <= 16:
        return True
    return False

def username_is_valid(username):
    if username_len(username) and characters_in_username(username) and is_no_symbols(username):
        return True
    return False
usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)




