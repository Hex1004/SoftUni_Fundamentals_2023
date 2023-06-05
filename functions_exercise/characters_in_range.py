def all_characters(first,second):
    character = []

    for all_char in range(ord(first) + 1, ord(second)):
        character.append(chr(all_char))
    return character


first_string = input()
second_string = input()

result = all_characters(first_string,second_string)

print(" ".join(result))