def chek_palindrome(palindrome_number):
    if palindrome_number == palindrome_number [::-1]:
        return True
    return False

numbers = input().split(", ")
for numbers in numbers:
    print(chek_palindrome(numbers))