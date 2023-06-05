def validate_password(password):
    is_valid = True

    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    counter_digit = 0

    for char in password:
        if char.isdigit():
            counter_digit += 1
    if counter_digit < 2:
            print("Password must have at least 2 digits")
            is_valid = False
    return  is_valid


random_password = input()
password_is_valid = validate_password(random_password)
if password_is_valid:
    print("Password is valid")