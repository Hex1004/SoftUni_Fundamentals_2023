main_list = input().split(' ')
searched_palindrome = input()

palindrome_lst = [word for word in main_list if word == word[::-1]]

print(f"{palindrome_lst}")
print(f"Found palindrome {palindrome_lst.count(searched_palindrome)} times")


# def palindrome_filtered(word):
#     if word == word[::-1]:
#         return word
#
#
# words = input().split(' ')
# palindrome = input()
#
# palindrome_lst = [word for word in words if palindrome_filtered(word)]
# palindrome_counter = palindrome_lst.count(palindrome)
#
# print(palindrome_lst)
# print(f"Found palindrome {palindrome_counter} times")